# Instalar a versão v0.1.0-alpha.1

[English](en/RELEASE.md) · [Português](RELEASE.md)

[Baixar no GitHub](https://github.com/erickfaria/balaio-theme/releases/tag/v0.1.0-alpha.1).

Esta é uma **pré-release experimental**, ainda sem validação de plataforma para ser estável. XML, treze testes locais e CI passam; a importação no Blogger precisa de teste. Consulte [limites conhecidos](../CHANGELOG.md) e [evidências de validação](VALIDATION.md).

## Arquivos

- `balaio-0.1.0-alpha.1.zip`: pacote com os dois templates, exemplos de páginas/posts, documentação bilíngue, versão, changelog e avisos de licença. Sem testes de desenvolvimento, scripts, backups ou prévias geradas.
- `balaio.xml`: interface em português.
- `balaio.en.xml`: interface em inglês.
- `SHA256SUMS.txt`: checksums do ZIP e dos dois XMLs.
- Arquivos de código-fonte automáticos do GitHub: todo o código rastreado, incluindo scripts e testes úteis para desenvolvimento.

O ZIP extrai para `balaio-0.1.0-alpha.1/`. Escolha um XML em `theme/`; não envie o ZIP como tema Blogger. Os XMLs separados contêm os mesmos templates. Use o pacote para obter também os exemplos e avisos completos de licença.

## Instalação rápida

1. Faça backup do tema atual e use um blog de teste separado.
2. Em **Tema → Editar HTML**, cole o XML escolhido inteiro e salve.
3. Configure idioma, título e descrições. No Layout, configure Apresentação, Menu e Links do rodapé.
4. Crie as páginas seguindo [PAGES.md](PAGES.md); placeholders são modelos de layout para substituir antes de publicar.
5. Confira home, artigos, páginas, busca, paginação e comentários em celular e desktop. Consulte [INSTALLATION.md](INSTALLATION.md) e [SEO.md](SEO.md).

Para conferir integridade, baixe os três arquivos e o checksum na mesma pasta e execute:

```sh
sha256sum -c SHA256SUMS.txt
```

## Licenças e serviços

Código, design e exemplos próprios são MIT. Inter e Newsreader são SIL OFL 1.1; preserve os avisos ao distribuir fontes. Google Fonts é hospedagem opcional; Blogger é uma plataforma externa. [Inventário de recursos](PROVENANCE.md).

## Reproduzir o pacote

Na tag correspondente, com Python 3.10+ e Git:

```sh
make check
python3 scripts/build_release.py --output /tmp/balaio-release
```

O script usa uma lista permitida de arquivos rastreados, entradas determinísticas no ZIP e checksums SHA-256. Gere fora do repositório ou em `dist/`, ignorado pelo Git. Não publique artefatos de um checkout com mudanças sem commit.
