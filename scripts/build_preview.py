#!/usr/bin/env python3
"""Gera fixtures visuais com o CSS real. Não compila as tags do Blogger."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET
import re
import json
from validate_theme import preview_css

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "preview"
SOURCE = (ROOT / "theme/balaio.xml").read_text(encoding="utf-8")
TREE = ET.fromstring(SOURCE)
# Blogger preserves CDATA delimiters in published HTML; do not strip them here.
HOME_SCRIPT = re.search(
    r"(<script id='home-continuation'\s.*?</script>)",
    SOURCE, flags=re.S
).group(1)
PAGES_SCRIPT = re.search(r"(<script id='page-navigation'\s.*?</script>)", SOURCE, flags=re.S).group(1)
FONT_LINKS = "".join(ET.tostring(link, encoding="unicode").replace("html:", "").replace("ns0:", "") for link in TREE.findall(".//{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}link"))
CSS = preview_css(TREE.find(
    ".//{http://www.google.com/2005/gml/b}skin"
).text)

POSTS = [
    ("Ciência", "O que uma pergunta pode mudar?", "Observar, investigar e aceitar novas respostas: uma conversa sobre como construímos conhecimento.", True),
    ("Ambiente", "Um mundo inteiro em uma gota", "O cotidiano oferece pequenas portas de entrada para pensar a vida em outras escalas.", False),
    ("Método", "Quando os dados contam uma história", "Um número pode abrir uma conversa. Entender como ele foi produzido é parte dela.", True),
    ("Leituras", "Anotações de uma mente curiosa", "Livros, perguntas e ideias que vale a pena guardar para voltar mais tarde.", False),
    ("Dados", "Do caderno à planilha", "Pequenas escolhas tornam as observações mais fáceis de conferir.", False),
    ("Saúde", "Perguntas sobre o lugar onde vivemos", "Uma leitura sobre ambiente e cuidado coletivo.", True),
    ("Pesquisa", "O caminho de uma hipótese", "Como registrar incertezas e revisar uma explicação.", False),
    ("Tecnologia", "Ferramentas para pensar com clareza", "A tecnologia como apoio ao trabalho de investigar.", False),
    ("Educação", "Aprender juntos", "Uma conversa sobre perguntas e experiências compartilhadas.", True),
    ("Ideias", "Voltar às primeiras perguntas", "Revisar o que aprendemos ajuda a continuar.", False),
]

HEADER = '''<a class="skip" href="#content">Pular para o conteúdo</a>
<header class="masthead"><div class="wrap"><div class="masthead-top">
<div><a class="brand" href="index.html">Balaio Científico</a><p class="description">Ciência, cultura e outras boas perguntas.</p></div>
<form class="search" action="empty.html" role="search"><input aria-label="Buscar no blog" name="q" placeholder="Buscar no blog" type="search"><button>Buscar</button></form></div>
<nav class="navigation" aria-label="Navegação principal" data-auto-pages="false"><div class="navbar section" id="navigation"><div class="widget PageList" id="PageList1"><ul><li><a href="index.html">Início</a></li><li><a href="article.html">Leitura</a></li><li><a href="about.html">Sobre mim</a></li><li><a href="contact.html">Contato</a></li><li><a href="privacy.html">Privacidade</a></li><li><a href="empty.html">Busca sem resultados</a></li></ul></div></div></nav></div></header>'''


# Use the actual theme form so visual fixtures track its icon and accessible label.
SEARCH_FORM = re.search(r"<form class='search'.*?</form>", SOURCE, flags=re.S).group(0)
HEADER = re.sub(r'<form class="search".*?</form>',
                SEARCH_FORM.replace("action='/search'", "action='empty.html'"), HEADER, flags=re.S)


def page(title, content, home=False):
    script = (HOME_SCRIPT if home else "") + PAGES_SCRIPT
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} · Balaio</title>{FONT_LINKS}<style>.navbar{{height:30px}}</style><style>{CSS}</style></head><body>{HEADER}<main class="wrap" id="content" tabindex="-1">{content}</main><footer class="site-footer wrap"><a href="https://www.blogger.com/go/report-abuse" rel="nofollow">Denunciar abuso</a></footer>{script}</body></html>'


def build():
    OUT.mkdir(exist_ok=True)
    # Geometria original: asset de teste, sem imagens de terceiros.
    (OUT / "observation.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360"><rect width="480" height="360" fill="#e5edf0"/><g stroke="#365b7b" fill="none" stroke-width="2"><circle cx="240" cy="180" r="100"/><ellipse cx="240" cy="180" rx="150" ry="45" transform="rotate(35 240 180)"/><ellipse cx="240" cy="180" rx="150" ry="45" transform="rotate(-35 240 180)"/></g><circle cx="240" cy="180" r="12" fill="#365b7b"/></svg>''')
    cards = []
    for index, (label, title, summary, picture) in enumerate(POSTS):
        image = '<a class="post-image-link" href="article.html" tabindex="-1" aria-hidden="true"><img class="post-image" src="observation.svg" alt="" width="480" height="360"></a>' if picture else ''
        cards.append(f'<article class="post-card"><div class="post-copy"><div class="labels">{escape(label)}</div><h2><a href="article.html">{escape(title)}</a></h2><p class="post-summary">{escape(summary)}</p><div class="meta"><span>Equipe Balaio</span><span>11 de outubro de 2026</span></div></div>{image}</article>'.replace('href="article.html"', f'href="post-{index + 1}.html"'))
    intro = '<div class="intro"><div class="eyebrow">Um espaço para a curiosidade</div><h1>Conhecimento começa com uma boa pergunta.</h1><p>Um lugar para reunir descobertas, conectar ideias e compartilhar o que aprendemos.</p></div>'
    def listing(entries, next_page=None, home=False):
        opening = '<h2 class="section-title">Últimas publicações</h2><div class="opening-cards">' + ''.join(entries[:2]) + '</div>' if home else ''
        remaining = entries[2:] if home else entries
        title = '<h2 class="section-title more-title">Mais leituras</h2>' if home and remaining else ''
        attrs = ' id="postlist" data-home-posts="10" data-page-limit="4" data-list-title="Mais leituras"'
        pager = '<nav class="pager" aria-label="Paginação"><span></span><span><a href="' + next_page + '" rel="next">Publicações anteriores</a></span></nav>' if next_page else ''
        return '<div class="content-grid"><div class="main section"><div class="widget Blog" id="Blog1">' + opening + title + '<div class="posts"' + attrs + '>' + ''.join(remaining) + '</div>' + pager + '</div></div>' + '</div>'
    (OUT / "index.html").write_text(page("Início", intro + listing(cards, home=True), home=True))
    # Reproduce Blogger delivering only two posts despite a higher configured maximum.
    (OUT / "short-home.html").write_text(page("Home paginada", intro + listing(cards[:2], "older-1.html", home=True), home=True))
    frames = ''.join(f'<iframe id="width-{width}" src="short-home.html" width="{width}" height="900" title="Home {width}px" style="display:block;border:0"></iframe>' for width in (320, 360, 768, 1440))
    (OUT / "responsive-home.html").write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Home responsiva</title><body>' + frames + '</body></html>')
    reading_frames = ''.join(f'<iframe id="{name}-{width}" src="{name}.html" width="{width}" height="900" title="{name} {width}px" style="display:block;border:0"></iframe>' for name in ('article', 'privacy', 'stress') for width in (320, 360, 768, 1440))
    (OUT / "responsive-reading.html").write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Leitura responsiva</title><body>' + reading_frames + '</body></html>')
    (OUT / "short-nojs.html").write_text(page("Sem JavaScript", intro + listing(cards[:2], "older-1.html", home=True)))
    for index in range(4):
        next_page = f"older-{index + 2}.html"  # Last link stays crawlable after reaching the target.
        (OUT / f"older-{index + 1}.html").write_text(page("Publicações anteriores", listing(cards[2 + index * 2:4 + index * 2], next_page)))
    (OUT / "older-5.html").write_text(page("Fim do arquivo", listing([])))
    for name, next_page in [("failure", "missing-page.html"), ("partial-failure", "partial-page.html"), ("duplicates", "duplicate-page.html"), ("cycle", "cycle-page.html"), ("external", "https://example.org/older")]:
        (OUT / f"short-{name}.html").write_text(page(name, intro + listing(cards[:2], next_page, home=True), home=True))
    (OUT / "partial-page.html").write_text(page("Falha parcial", listing(cards[2:4], "missing-page.html")))
    (OUT / "duplicate-page.html").write_text(page("Duplicações", listing(cards[:4], "older-2.html")))
    (OUT / "cycle-page.html").write_text(page("Ciclo", listing(cards[2:4], "cycle-page.html")))
    (OUT / "short-budget.html").write_text(page("Uma página extra", intro + listing(cards[:2], "older-1.html", home=True).replace('data-page-limit="4"', 'data-page-limit="1"'), home=True))
    (OUT / "short-target.html").write_text(page("Meta sem cortar página", intro + listing(cards[:2], "older-1.html", home=True).replace('data-home-posts="10"', 'data-home-posts="3"'), home=True))
    (OUT / "short-disabled.html").write_text(page("Carregamento desligado", intro + listing(cards[:2], "older-1.html", home=True).replace('data-page-limit="4"', 'data-page-limit="0"'), home=True))
    (OUT / "short-end.html").write_text(page("Fim antecipado", intro + listing(cards[:2], "end-page.html", home=True), home=True))
    (OUT / "end-page.html").write_text(page("Fim", listing(cards[2:4])))
    unsafe = cards[2].replace('<p class="post-summary">', """<p class="post-summary"><img src="missing.png" onerror="document.body.setAttribute('data-attack','ran')">""")
    (OUT / "unsafe-page.html").write_text(page("Conteúdo inerte", listing([unsafe])) + '<script>document.body.setAttribute("data-attack","ran")</script>')
    (OUT / "short-unsafe.html").write_text(page("Conteúdo inerte", intro + listing(cards[:2], "unsafe-page.html", home=True), home=True))
    # Query cleanup must preserve unrelated parameters and fragments.
    mobile_card = cards[2].replace('post-3.html', 'post-3.html?m=0&amp;ref=fixture#reading').replace(
        '<div class="labels">Método</div>',
        '<div class="labels"><a href="empty.html?m=1&amp;ref=label#topics">Método</a></div>')
    (OUT / "mobile-links-page.html").write_text(page("Links de conteúdo", listing([mobile_card])))
    (OUT / "short-mobile-links.html").write_text(page("Links móveis", intro + listing(cards[:2], "mobile-links-page.html", home=True), home=True))
    decoy = '<section class="posts">' + cards[9] + '</section><nav class="pager"><a rel="next" href="https://example.org/older">Outro gadget</a></nav>'
    (OUT / "mixed-page.html").write_text(page("Gadgets fora do Blog1", decoy + listing(cards[2:4])))
    (OUT / "short-mixed.html").write_text(page("Gadgets fora do Blog1", intro + listing(cards[:2], "mixed-page.html", home=True), home=True))
    (OUT / "missing-blog-page.html").write_text(page("Página sem Blog1", decoy))
    (OUT / "short-missing-blog.html").write_text(page("Resposta incompleta", intro + listing(cards[:2], "missing-blog-page.html", home=True), home=True))
    # Native Blogger applies a 30px navbar height. The theme must contain full-height
    # wrapped navigation, including when feed entries augment a home-only widget.
    page_entries = [
        {"title": {"$t": title}, "link": [{"rel": "alternate", "href": href}]}
        for title, href in [("Sobre mim", "/p/about.html"), ("Contato", "/p/contact.html"),
                            ("Privacidade", "/p/privacy.html"), ("Membros", "/p/members.html")]
    ]
    (OUT / "pages-feed.json").write_text(json.dumps({"feed": {"entry": page_entries}}, ensure_ascii=False))
    (OUT / "pages-empty.json").write_text('{"feed":{}}')
    (OUT / "pages-invalid.json").write_text('{broken')
    unsafe_entries = page_entries + [
        {"title": {"$t": "Duplicate"}, "link": [{"rel": "alternate", "href": "/p/contact.html?m=1"}]},
        {"title": {"$t": "External"}, "link": [{"rel": "alternate", "href": "https://example.org/p/external.html"}]},
        {"title": {"$t": "Unsafe"}, "link": [{"rel": "alternate", "href": "javascript:alert(1)"}]},
        {"title": {"$t": '<img src=x onerror="alert(1)">'}, "link": [{"rel": "alternate", "href": "/p/text.html"}]}
    ]
    (OUT / "pages-unsafe.json").write_text(json.dumps({"feed": {"entry": unsafe_entries}}))
    def menu_fixture(feed, manual=False, automatic=True):
        content = page("Menu automático", intro + listing(cards[:2], "older-1.html", home=True), home=True)
        home = '<li><a aria-current="page" href="menu-auto.html">Início</a></li>'
        links = home + ('<li><a href="/p/about.html">Quem sou</a></li>' if manual else '')
        content = re.sub(r'(<div class="widget PageList" id="PageList1">)<ul>.*?</ul>',
                         r'\g<1><ul>' + links + '</ul>', content, count=1, flags=re.S)
        mode = 'true' if automatic else 'false'
        return content.replace('data-auto-pages="false"', f'data-auto-pages="{mode}" data-pages-feed="{escape(feed)}"', 1)
    for slug, feed in [('auto', 'pages-feed.json'), ('empty', 'pages-empty.json'),
                       ('failure', 'pages-missing.json'), ('invalid', 'pages-invalid.json'),
                       ('unsafe', 'pages-unsafe.json')]:
        (OUT / f"menu-{slug}.html").write_text(menu_fixture(feed))
    (OUT / "menu-manual.html").write_text(menu_fixture('pages-feed.json', manual=True, automatic=False))
    (OUT / "menu-selected.html").write_text(menu_fixture('pages-feed.json', manual=True))
    pages_dir = OUT / "p"
    pages_dir.mkdir(exist_ok=True)
    for slug, title in [('about','Sobre mim'), ('contact','Contato'), ('privacy','Privacidade'), ('members','Membros')]:
        content = menu_fixture('../pages-feed.json').replace('aria-current="page" href="menu-auto.html"', 'href="../menu-auto.html"')
        body = '<main class="wrap" id="content" tabindex="-1"><div class="content-grid article-grid"><article class="article" itemscope itemtype="https://schema.org/WebPage"><h1>' + escape(title) + '</h1><div class="post-body"><p>Lorem ipsum dolor sit amet.</p></div></article></div></main>'
        content = re.sub(r'<main class="wrap".*?</main>', lambda _: body, content, count=1, flags=re.S)
        content = content.replace(HOME_SCRIPT, '').replace('href="index.html"', 'href="../index.html"')
        content = content.replace("action='empty.html'", "action='../empty.html'")
        (pages_dir / f'{slug}.html').write_text(content.replace('Menu automático', title))
    frames = ''.join(f'<iframe id="width-{width}" src="menu-auto.html" width="{width}" height="900" title="Menu {width}px" style="display:block;border:0"></iframe>' for width in (320,360,768,1440))
    (OUT / "responsive-menu.html").write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><title>Menu responsivo</title><body>'+frames+'</body></html>')
    article = '''<div class="content-grid article-grid"><div><article class="article"><div class="labels">Ciência</div><h1>O que uma pergunta pode mudar?</h1><div class="meta"><span>Equipe Balaio</span><span>11 de outubro de 2026</span></div><div class="post-body"><p>Às vezes, aprender começa com uma pausa. Olhamos para algo familiar e percebemos que ainda há uma pergunta a fazer.</p><h2>O espaço entre observar e entender</h2><p>A curiosidade aproxima ideias distantes. Podemos começar com um detalhe cotidiano, reunir observações e comparar explicações.</p><blockquote>Uma boa pergunta abre espaço para continuar pensando.</blockquote><p>Este texto é fictício e serve para avaliar a tipografia do tema.</p><h2>Um pequeno registro</h2><table><thead><tr><th>Etapa</th><th>Pergunta</th></tr></thead><tbody><tr><td>Observação</td><td>O que aconteceu?</td></tr><tr><td>Investigação</td><td>Como podemos conferir?</td></tr></tbody></table><pre><code>perguntas = ["Como?", "Por quê?", "Como conferir?"]</code></pre><h2>Para continuar</h2><ul><li>Registrar o que sabemos.</li><li>Identificar o que ainda falta descobrir.</li><li>Revisitar as primeiras hipóteses.</li></ul><p><a href="index.html">Voltar às publicações</a></p></div></article></div></div>'''
    (OUT / "article.html").write_text(page("Leitura", article))
    for index in range(len(cards)):
        (OUT / f"post-{index + 1}.html").write_text(page(POSTS[index][1], article))
    (OUT / "empty.html").write_text(page("Busca", '<div class="content-grid"><div><h1>Busca</h1><p class="empty">Nenhuma publicação encontrada. <a href="index.html">Voltar ao início</a>.</p></div>' + '</div>'))
    for slug, title in [('about', 'Sobre'), ('contact', 'Contato'), ('privacy', 'Privacidade')]:
        body = (ROOT / f'examples/pages/{slug}.pt-BR.html').read_text(encoding='utf-8')
        rendered = page(title, '<div class="content-grid article-grid"><article class="article" itemscope itemtype="https://schema.org/WebPage"><h1 itemprop="name">' + title + '</h1><div class="post-body" itemprop="text">' + body + '</div></article></div>')
        rendered = rendered.replace(f'href="{slug}.html"', f'href="{slug}.html" aria-current="page"')
        (OUT / f'{slug}.html').write_text(rendered)
    sample = (ROOT / 'examples/post.pt-BR.html').read_text(encoding='utf-8')
    media = '<figure><img src="observation.svg" alt="Ilustração geométrica de órbitas" width="480" height="360"><figcaption>Imagem original para teste de layout.</figcaption></figure><div class="video"><iframe src="about:blank" title="Contêiner de vídeo de teste"></iframe></div>'
    (OUT / 'media.html').write_text(page('Post sample', '<div class="content-grid article-grid"><article class="article"><h1>Modelo de postagem responsiva</h1><div class="post-body">' + sample + media + '</div></article></div>'))
    stress = '<div class="content-grid article-grid"><div><article class="article"><h1>' + ('Conhecimento' * 10) + '</h1><div class="post-body"><p>' + ('https://example.org/long-reference-' * 20) + '</p><pre><code>' + ('long_code_without_breaks_' * 30) + '</code></pre><table><tr><td>' + ('measurement_' * 30) + '</td></tr></table></div></article></div></div>'
    (OUT / "stress.html").write_text(page("Responsive stress fixture", stress))
    print(f"Preview generated in {OUT}. This does not validate Blogger import.")


if __name__ == "__main__":
    build()
