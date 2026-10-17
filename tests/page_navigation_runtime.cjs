// Execute the embedded production script. Browser layout is verified separately.
const vm = require('node:vm');
const assert = require('node:assert/strict');
const source = JSON.parse(require('node:fs').readFileSync(0, 'utf8'));
function node(tag, attrs = {}, text = '') {
  const value = {tag, attrs, children: [], textContent: text,
    getAttribute(name) { return this.attrs[name] ?? null; },
    setAttribute(name, data) { this.attrs[name] = String(data); },
    append(child) { this.children.push(child); }};
  Object.defineProperty(value, 'href', {get() {return this.attrs.href;}, set(href) {this.attrs.href = href;}});
  Object.defineProperty(value, 'innerHTML', {set() {throw Error('Received HTML must never execute');}});
  return value;
}
function entry(title, href) { return {title: {$t:title}, link:[{rel:'alternate', href}]}; }
const standard = [entry('Sobre', '/p/about.html'), entry('Contato', '/p/contact.html'), entry('Privacidade', '/p/privacy.html')];
async function run(options = {}) {
  const list = node('ul');
  for (const [href, text] of options.native || [['/', 'Home']]) {
    const item = node('li'); item.append(node('a', {href}, text)); list.append(item);
  }
  const links = () => list.children.flatMap(item => item.children);
  const widget = {querySelector: () => list};
  const nav = {dataset: {pagesFeed: options.feedURL}, querySelector: () => options.noWidget ? null : widget,
    querySelectorAll: () => links()};
  const events = [];
  const document = {readyState:options.loading ? 'loading' : 'complete',
    addEventListener(type, run, config) {events.push({type,run,config});},
    documentElement: {lang:'pt-BR'}, createElement: node,
    querySelector: () => options.manual ? null : nav};
  const calls = [], timers = [], stored = [];
  const fetch = async (url, config) => {
    calls.push({url, config});
    if (options.error) throw Error('offline');
    return {ok:!options.httpError, json:async () => {
      if (options.invalidJSON) throw SyntaxError('bad JSON');
      return options.data !== undefined ? options.data : {feed:{entry:standard}};
    }};
  };
  const storage = {getItem() {if (options.noStorage) throw Error('blocked'); return options.cache ?? null;},
    setItem(key, data) {if (options.noStorage) throw Error('blocked'); stored.push({key, data});}};
  const pathname = options.path || '/';
  vm.runInNewContext(source, {window:{fetch, AbortController}, fetch, AbortController, URL, document,
    sessionStorage:storage, location:{origin:'https://example.com', href:'https://example.com'+pathname, pathname},
    setTimeout(run, delay) {timers.push({run, delay}); return timers.length;}, clearTimeout() {}});
  await new Promise(setImmediate);
  return {links:links(), getLinks:links, calls, timers, stored, events};
}
(async () => {
  const waiting = await run({loading:true});
  assert.equal(waiting.calls.length, 0);
  assert.equal(waiting.events[0].type, 'DOMContentLoaded');
  assert.equal(waiting.events[0].config.once, true);
  waiting.events[0].run();
  await new Promise(setImmediate);
  assert.equal(waiting.getLinks().length, 4);
  const success = await run();
  assert.deepEqual(success.links.map(a=>a.textContent), ['Home','Contato','Privacidade','Sobre']);
  assert.equal(success.calls.length, 1);
  assert.equal(new URL(success.calls[0].url).pathname, '/feeds/pages/summary');
  assert.equal(new URL(success.calls[0].url).searchParams.get('max-results'), '150');
  assert.equal(success.calls[0].config.credentials, 'omit');
  assert.equal(success.calls[0].config.redirect, 'error');
  assert.equal(success.calls[0].config.priority, 'low');
  assert.equal(success.timers[0].delay, 6000);
  const saved = JSON.parse(success.stored[0].data);
  assert.ok(saved.pages.every(page=>Object.keys(page).sort().join(',')==='href,title'));
  for (const options of [{manual:true},{noWidget:true},{feedURL:'https://external.org/feed'}]) {
    assert.equal((await run(options)).calls.length, 0);
  }
  for (const options of [{error:true},{httpError:true},{invalidJSON:true}, {data:null},
                         {data:{}}, {data:{feed:{entry:{}}}}, {data:{feed:{}}}]) {
    assert.deepEqual((await run(options)).links.map(a=>a.textContent), ['Home']);
  }
  const selected = await run({native:[['/','Home'],['/p/about.html?m=1','My title'],['https://external.org','Extra']]});
  assert.deepEqual(selected.links.map(a=>a.textContent), ['Home','My title','Extra','Contato','Privacidade']);
  const malicious = await run({data:{feed:{entry:[...standard,
    entry('Duplicate','/p/contact.html?m=0'), entry('External','https://external.org/p/page.html'),
    entry('Script','javascript:alert(1)'), entry('Post','/2026/10/post.html'), entry('Empty',''),
    entry('','/p/empty.html'), entry('<img onerror=alert(1)>','/p/text.html'), null]}}});
  assert.equal(malicious.links.length, 5);
  assert.ok(malicious.links.some(a=>a.textContent==='<img onerror=alert(1)>'));
  assert.ok(!malicious.links.some(a=>['Duplicate','External','Script','Post','Empty'].includes(a.textContent)));
  const current = await run({path:'/p/privacy.html'});
  assert.equal(current.links.find(a=>a.textContent==='Privacidade').getAttribute('aria-current'), 'page');
  assert.equal(current.links.filter(a=>a.getAttribute('aria-current')==='page').length, 1);
  const cached = await run({cache:success.stored[0].data});
  assert.equal(cached.calls.length, 0);
  assert.deepEqual(cached.links.map(a=>a.textContent), success.links.map(a=>a.textContent));
  for (const cache of ['bad JSON', JSON.stringify({time:Date.now()-61000,pages:[]}),
                       JSON.stringify({time:Date.now()+5000,pages:[]})]) {
    assert.equal((await run({cache})).calls.length, 1);
  }
  assert.equal((await run({noStorage:true})).links.length, 4);
  const unsafeCache = await run({cache:JSON.stringify({time:Date.now(), pages:[
    {title:'Injected',href:'javascript:alert(1)'}, {title:'External',href:'https://external.org/p/unsafe.html'},
    {title:'Cached',href:'/p/cached.html'}]})});
  assert.deepEqual(unsafeCache.links.map(a=>a.textContent), ['Home','Cached']);
})().catch(error=>{console.error(error);process.exitCode=1;});
