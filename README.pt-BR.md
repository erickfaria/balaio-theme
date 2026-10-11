# Balaio — Tema Blogger gratuito e minimalista

**[English](README.md) · [Português brasileiro](README.pt-BR.md)**

Um **template XML gratuito para Blogger**: minimalista, responsivo, open source e fácil de personalizar. Design editorial próprio, com verde, areia e azul pastel, tipografia confortável e uma base técnica preparada para SEO em blogs pessoais e científicos.

**Licença MIT.** Você pode usar, modificar e redistribuir o código, inclusive em projetos comerciais. Preserve os avisos de autoria e licença nas cópias ou partes substanciais do código. A MIT não exige crédito visível no site nem autorização paga. O software é fornecido sem garantia. [Leia a licença](LICENSE) · [MIT na Open Source Initiative](https://opensource.org/license/mit).

> **Estado da versão:** `v0.1.0-alpha.1` é uma prévia experimental. Checks locais e CI passam; importação e funcionamento dos gadgets no Blogger não estão confirmados. Instale primeiro num blog de teste. [Baixar a release](https://github.com/erickfaria/balaio-theme/releases/tag/v0.1.0-alpha.1) · [Guia da versão](docs/RELEASE.md).

## Escolha o idioma

| Interface | Arquivo |
| --- | --- |
| Português brasileiro | [theme/balaio.xml](theme/balaio.xml) |
| Inglês | [theme/balaio.en.xml](theme/balaio.en.xml) |

Configure o idioma do blog no Blogger de acordo com a interface escolhida. O tema não traduz o conteúdo das suas publicações.

## Instalar no Blogger

Não precisa compilar nem instalar ferramentas para usar o tema.

1. Baixe o ZIP do repositório em **Code → Download ZIP** e extraia, ou baixe o XML desejado pela opção **Raw / Download raw file** do GitHub.
2. Escolha um **blog de teste** no Blogger. Faça backup do tema atual em **Tema → menu → Fazer backup**.
3. Abra **Tema → menu → Editar HTML**. Substitua o conteúdo do editor pelo XML completo e salve.
4. Configure título, descrição e idioma em **Configurações**.
5. Em **Layout**, edite **Menu** com links de páginas ou marcadores. Início já vem no código.
6. Edite **Apresentação** (português) ou **Introduction** (inglês) para mudar a abertura. Configure os gadgets de marcadores, lateral e rodapé.
7. Confira artigos, páginas, busca, paginação e comentários no celular e no computador antes de usar no blog principal.

[Instalação e solução de problemas](docs/INSTALLATION.md) · [Personalização](docs/CUSTOMIZATION.md)

## Recursos

- Três cards de abertura na home, seguidos da lista editorial sem repetir posts.
- Layout responsivo para celulares, tablets e computadores; miniaturas opcionais e entradas com largura completa quando não há imagem.
- Busca nativa, marcadores, paginação, artigos e páginas estáticas.
- Comentários básicos e link para comentar; formulário incorporado e respostas encadeadas ainda pendentes.
- Apresentação, menu, lateral e rodapé editáveis por gadgets.
- Foco de teclado, link para pular ao conteúdo, rolagem contida em código/tabelas e estilos para impressão.
- **Inter** para interface e **Newsreader** para títulos e leitura, via Google Fonts com fallback local e `display=swap`. Ambas usam SIL OFL 1.1; suas licenças são separadas da MIT.
- Sem JavaScript do tema ou dependências externas de pacotes Python.

Logo em imagem, controles do Designer de temas e layout específico de 404 ainda não estão implementados. A prévia usa o CSS real com conteúdo de exemplo; não compila expressões do Blogger.

## Desenvolvimento local

Requer Python 3.10+; `make` é opcional.

```sh
python3 scripts/validate_docs.py
python3 scripts/build_locales.py --check
python3 scripts/validate_theme.py
python3 -m unittest discover -s tests -v
python3 scripts/build_preview.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory preview
```

Abra `http://127.0.0.1:8765`. Encerre o servidor com Ctrl+C. Com Make instalado, use `make check` e `make serve`. Após editar o XML português, rode `make locales` ou `python3 scripts/build_locales.py` para atualizar a versão inglesa.

## Organização

| Caminho | Conteúdo |
| --- | --- |
| `theme/` | XMLs instaláveis; português é a fonte da variante inglesa |
| `examples/` | Modelos editáveis do corpo de posts em inglês e português |
| `scripts/` | Geração de idioma, validação e prévia |
| `tests/` | Verificações do validador |
| `docs/` / `docs/en/` | Guias e notas em português / inglês |
| `licenses/` | Avisos originais das fontes |
| `.github/` | CI e modelos de issue e PR |
| `preview/` | Arquivos locais gerados, ignorados pelo Git |

[Contribuir](CONTRIBUTING.md) · [Histórico](CHANGELOG.md) · [Design](docs/DESIGN.md) · [Plano](docs/ROADMAP.md) · [Validação](docs/VALIDATION.md) · [Autoria e licenças](docs/PROVENANCE.md)

Backups, credenciais e conteúdo privado não integram a distribuição. Fontes mantêm a licença OFL; posts e imagens têm direitos próprios. A automação do GitHub verifica os templates, as traduções e a geração da prévia; um check verde não confirma importação no Blogger.

## SEO e descoberta por IA

O tema preserva os metadados do Blogger e adiciona microdados de artigos ligados ao conteúdo visível. Consulte o [guia de SEO e auditoria](docs/SEO.md) para configurar descrições de pesquisa, indexação e acesso de robôs. Inclui auditor de HTML sem dependências; posição e citações por IA não são garantidas.

## Perguntas frequentes

**Este tema Blogger é gratuito mesmo?** Sim. A MIT permite uso pessoal e comercial, modificação e redistribuição com os avisos de licença preservados. Não exige compra nem crédito visível.

**Posso mudar cores e layout?** Sim. Comece pelos gadgets de Layout e pelas variáveis CSS documentadas para paleta pastel, fontes e largura de leitura. [Guia de personalização](docs/CUSTOMIZATION.md).

**O tema é preparado para SEO?** Oferece metadados nativos do Blogger, títulos semânticos, links rastreáveis e microdados de artigos. O [guia de busca](docs/SEO.md) cobre Google, Bing, DuckDuckGo, SearXNG e descoberta por IA. Indexação e compatibilidade publicadas ainda precisam de verificação.

**Como escrever posts responsivos?** Use o [guia de postagens e exemplo HTML editável](docs/POSTS.md). Títulos, resumos, tabelas, imagens e vídeos respeitam a coluna de leitura sem adicionar JavaScript ao tema.

## Páginas básicas

[Modelos de Sobre, Contato e Privacidade](docs/PAGES.md) usam Lorem ipsum. Crie as páginas no Blogger e adicione suas URLs reais ao Menu e aos Links do rodapé. O tema não fixa endereços de páginas nem dados de contato. Código e recursos visuais incluídos são MIT; Inter e Newsreader são fontes abertas sob SIL OFL.

## Contribuir por pull requests

Forks públicos e contribuições são bem-vindos. Mudanças de contribuidores na `main` exigem CI e revisão do mantenedor; somente `@erickfaria` integra alterações. Consulte a [política de manutenção](https://github.com/erickfaria/balaio-theme/blob/main/MAINTAINERS.md) e o [guia de contribuição](CONTRIBUTING.md).
