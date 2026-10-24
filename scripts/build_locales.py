#!/usr/bin/env python3
"""Build the English template from the Portuguese source; use --check in CI."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TRANSLATIONS = {
    "Formulário de contato": "Contact form",
    "Envie uma mensagem": "Send a message",
    "Nome (opcional)": "Name (optional)",
    "E-mail (obrigatório)": "Email (required)",
    "Mensagem (obrigatória)": "Message (required)",
    "Enviar mensagem": "Send message",
    "Seu nome é opcional. O Blogger processa seu e-mail e sua mensagem para encaminhar o contato aos responsáveis pelo blog.": "Your name is optional. Blogger processes your email and message to forward your inquiry to the blog administrators.",
    "Ative o JavaScript para usar o formulário de contato do Blogger.": "Enable JavaScript to use Blogger’s contact form.",
    "Explore o blog": "Explore the blog",
    "Assuntos": "Topics",
    "Denunciar abuso": "Report abuse",
    "Controles do Designer do Blogger.": "Blogger Designer controls.",
    "Fundo da página": "Page background",
    "Texto principal": "Main text",
    "Texto secundário": "Secondary text",
    "Links e botões": "Links and buttons",
    "Divisórias suaves": "Soft dividers",
    "Superfície verde pastel": "Pastel green surface",
    "Card areia pastel": "Pastel sand card",
    "Card azul pastel": "Pastel blue card",
    "Fonte da interface": "Interface font",
    "Fonte de posts e páginas": "Post and page font",
    "Pular para o conteúdo": "Skip to content",
    "Cabeçalho": "Header",
    "Buscar no blog": "Search this blog",
    "Navegação principal": "Main navigation",
    "Páginas": "Pages",
    "Início": "Home",
    "Apresentação": "Introduction",
    "Um espaço para a curiosidade": "A space for curiosity",
    "Conhecimento começa com uma boa pergunta.": "Knowledge starts with a good question.",
    "Um lugar para reunir descobertas, conectar ideias e compartilhar o que aprendemos.": "A place to gather discoveries, connect ideas and share what we learn.",
    "Postagens": "Posts",
    "Nenhuma publicação encontrada.": "No posts found.",
    "Voltar ao início": "Back to home",
    "Últimas publicações": "Latest posts",
    "Mais leituras": "More to read",
    "Publicação sem título": "Untitled post",
    "Voltar às publicações": "Back to posts",
    "Escrito por": "Written by",
    "Comentários": "Comments",
    "Escrever um comentário": "Write a comment",
    "Paginação": "Pagination",
    "Publicações mais recentes": "Newer posts",
    "Publicações anteriores": "Older posts",
    "código original": "original code",
    "Edite as variáveis abaixo para personalizar a identidade do blog.": "Edit the variables below to customize your blog identity.",
}


def build(check=False):
    source = (ROOT / "theme/balaio.xml").read_text(encoding="utf-8")
    for original, translated in TRANSLATIONS.items():
        if original not in source:
            raise ValueError(f"Translation source missing: {original}")
        source = source.replace(original, translated)
    target = ROOT / "theme/balaio.en.xml"
    if check:
        if not target.exists() or target.read_text(encoding="utf-8") != source:
            raise ValueError("English template is stale. Run python3 scripts/build_locales.py")
        print("OK: English template matches the source.")
    else:
        target.write_text(source, encoding="utf-8")
        print(f"English template generated: {target}")


if __name__ == "__main__":
    try:
        build(check="--check" in sys.argv[1:])
    except (ValueError, OSError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        sys.exit(1)
