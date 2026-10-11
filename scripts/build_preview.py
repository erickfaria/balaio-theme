#!/usr/bin/env python3
"""Gera fixtures visuais com o CSS real. Não compila as tags do Blogger."""
from html import escape
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "preview"
TREE = ET.parse(ROOT / "theme/balaio.xml").getroot()
FONT_LINKS = "".join(ET.tostring(link, encoding="unicode").replace("html:", "").replace("ns0:", "") for link in TREE.findall(".//{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}link"))
CSS = TREE.find(
    ".//{http://www.google.com/2005/gml/b}skin"
).text

POSTS = [
    ("Ciência", "O que uma pergunta pode mudar?", "Observar, investigar e aceitar novas respostas: uma conversa sobre como construímos conhecimento.", True),
    ("Ambiente", "Um mundo inteiro em uma gota", "O cotidiano oferece pequenas portas de entrada para pensar a vida em outras escalas.", False),
    ("Método", "Quando os dados contam uma história", "Um número pode abrir uma conversa. Entender como ele foi produzido é parte dela.", True),
    ("Leituras", "Anotações de uma mente curiosa", "Livros, perguntas e ideias que vale a pena guardar para voltar mais tarde.", False),
]

HEADER = '''<a class="skip" href="#content">Pular para o conteúdo</a>
<header class="masthead"><div class="wrap"><div class="masthead-top">
<div><a class="brand" href="index.html">Balaio Científico</a><p class="description">Ciência, cultura e outras boas perguntas.</p></div>
<form class="search" action="empty.html" role="search"><input aria-label="Buscar no blog" name="q" placeholder="Buscar no blog" type="search"><button>Buscar</button></form></div>
<nav class="navigation" aria-label="Navegação principal"><ul><li><a href="index.html">Início</a></li><li><a href="article.html">Leitura</a></li><li><a href="empty.html">Busca sem resultados</a></li></ul></nav></div></header>'''
FOOTER = '''<footer class="site-footer"><div class="wrap footer-line"><span>Balaio Científico</span><span>Prévia local · conteúdo fictício · MIT</span></div></footer>'''
SIDEBAR = '''<aside class="sidebar" aria-label="Explore o blog"><div class="widget"><h2>Explore os assuntos</h2><ul><li>Ciência</li><li>Ambiente</li><li>Método</li><li>Leituras</li></ul></div><div class="widget"><h2>Sobre este espaço</h2><p class="post-summary">Um caderno aberto para conectar perguntas, descobertas e pessoas.</p></div></aside>'''


def page(title, content):
    return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} · Balaio</title>{FONT_LINKS}<style>{CSS}</style></head><body>{HEADER}<main class="wrap" id="content" tabindex="-1">{content}</main>{FOOTER}</body></html>'


def build():
    OUT.mkdir(exist_ok=True)
    # Geometria original: asset de teste, sem imagens de terceiros.
    (OUT / "observation.svg").write_text('''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 360"><rect width="480" height="360" fill="#e5edf0"/><g stroke="#365b7b" fill="none" stroke-width="2"><circle cx="240" cy="180" r="100"/><ellipse cx="240" cy="180" rx="150" ry="45" transform="rotate(35 240 180)"/><ellipse cx="240" cy="180" rx="150" ry="45" transform="rotate(-35 240 180)"/></g><circle cx="240" cy="180" r="12" fill="#365b7b"/></svg>''')
    cards = []
    for label, title, summary, picture in POSTS:
        image = '<a class="post-image-link" href="article.html" tabindex="-1" aria-hidden="true"><img class="post-image" src="observation.svg" alt="" width="480" height="360"></a>' if picture else ''
        cards.append(f'<article class="post-card"><div class="post-copy"><div class="labels">{escape(label)}</div><h2><a href="article.html">{escape(title)}</a></h2><p class="post-summary">{escape(summary)}</p><div class="meta"><span>Equipe Balaio</span><span>11 de outubro de 2026</span></div></div>{image}</article>')
    intro = '<div class="intro"><div class="eyebrow">Um espaço para a curiosidade</div><h1>Conhecimento começa com uma boa pergunta.</h1><p>Um lugar para reunir descobertas, conectar ideias e compartilhar o que aprendemos.</p></div>'
    (OUT / "index.html").write_text(page("Início", intro + '<div class="content-grid"><div><h2 class="section-title">Últimas publicações</h2><div class="opening-cards">' + ''.join(cards[:3]) + '</div><h2 class="section-title">Mais leituras</h2><div class="posts">' + ''.join(cards[3:]) + '</div></div>' + SIDEBAR + '</div>'))
    article = '''<div class="content-grid article-grid"><div><article class="article"><div class="labels">Ciência</div><h1>O que uma pergunta pode mudar?</h1><div class="meta"><span>Equipe Balaio</span><span>11 de outubro de 2026</span></div><div class="post-body"><p>Às vezes, aprender começa com uma pausa. Olhamos para algo familiar e percebemos que ainda há uma pergunta a fazer.</p><h2>O espaço entre observar e entender</h2><p>A curiosidade aproxima ideias distantes. Podemos começar com um detalhe cotidiano, reunir observações e comparar explicações.</p><blockquote>Uma boa pergunta abre espaço para continuar pensando.</blockquote><p>Este texto é fictício e serve para avaliar a tipografia do tema.</p><h2>Um pequeno registro</h2><table><thead><tr><th>Etapa</th><th>Pergunta</th></tr></thead><tbody><tr><td>Observação</td><td>O que aconteceu?</td></tr><tr><td>Investigação</td><td>Como podemos conferir?</td></tr></tbody></table><pre><code>perguntas = ["Como?", "Por quê?", "Como conferir?"]</code></pre><h2>Para continuar</h2><ul><li>Registrar o que sabemos.</li><li>Identificar o que ainda falta descobrir.</li><li>Revisitar as primeiras hipóteses.</li></ul><p><a href="index.html">Voltar às publicações</a></p></div></article></div></div>'''
    (OUT / "article.html").write_text(page("Leitura", article))
    (OUT / "empty.html").write_text(page("Busca", '<div class="content-grid"><div><h1>Busca</h1><p class="empty">Nenhuma publicação encontrada. <a href="index.html">Voltar ao início</a>.</p></div>' + SIDEBAR + '</div>'))
    stress = '<div class="content-grid article-grid"><div><article class="article"><h1>' + ('Conhecimento' * 10) + '</h1><div class="post-body"><p>' + ('https://example.org/long-reference-' * 20) + '</p><pre><code>' + ('long_code_without_breaks_' * 30) + '</code></pre><table><tr><td>' + ('measurement_' * 30) + '</td></tr></table></div></article></div></div>'
    (OUT / "stress.html").write_text(page("Responsive stress fixture", stress))
    print(f"Preview generated in {OUT}. This does not validate Blogger import.")


if __name__ == "__main__":
    build()
