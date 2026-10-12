# Balaio — Tema Blogger gratuito e minimalista

**Candidata rc.5 em desenvolvimento:** o script de continuação fica fora dos includables dos gadgets. A renderização real no Blogger está em investigação; checks locais não validam o compilador da plataforma.

**[English](README.md) · [Português brasileiro](README.pt-BR.md)**

Um **template XML gratuito para Blogger**: minimalista, responsivo, open source e fácil de personalizar. Design editorial próprio, com verde, areia e azul pastel, tipografia confortável e uma base técnica preparada para SEO em blogs pessoais e científicos.

**Licença MIT.** Você pode usar, modificar e redistribuir o código, inclusive em projetos comerciais. Preserve os avisos de autoria e licença nas cópias ou partes substanciais do código. A MIT não exige crédito visível no site nem autorização paga. O software é fornecido sem garantia. [Leia a licença](LICENSE) · [MIT na Open Source Initiative](https://opensource.org/license/mit).

> **Versão atual:** `v0.2.0-rc.4` (candidata). Prioriza o conteúdo inicial, reduz o CSS das fontes e evita a lateral oculta em posts/páginas. Vinte e quatro checks locais passaram; a continuação da rc.3 foi confirmada pelo proprietário e observada no blog. A candidata otimizada precisa de nova importação no Blogger. [Baixar candidata](https://github.com/erickfaria/balaio-theme/releases/tag/v0.2.0-rc.4) · [Evidências de performance](docs/PERFORMANCE.md) · [Guia de atualização](docs/RELEASE.md) · [Escopo da validação](docs/VALIDATION.md).
>
> **Alternativa estável:** [v0.1.0](https://github.com/erickfaria/balaio-theme/releases/tag/v0.1.0), com importação confirmada pelo proprietário. Seus templates diferem da candidata atual.

**O GitHub Actions está ativo.** PRs, pushes na main e tags de versão validam o tema e geram XML, ZIP de instalação, checksums e preview para download. Os checks locais continuam disponíveis. [Política de manutenção](https://github.com/erickfaria/balaio-theme/blob/main/MAINTAINERS.md).

## Escolha o idioma

| Interface | Arquivo |
| --- | --- |
| Português brasileiro | [theme/balaio.xml](theme/balaio.xml) |
| Inglês | [theme/balaio.en.xml](theme/balaio.en.xml) |

Configure o idioma do blog no Blogger de acordo com a interface escolhida. O tema não traduz o conteúdo das suas publicações.

## Instalar no Blogger

Não precisa compilar nem instalar ferramentas para usar o tema.

1. Baixe o pacote ou XML separado da versão candidata indicada acima. O ZIP do código também está disponível em **Code → Download ZIP**.
2. Escolha um **blog de teste** no Blogger. Faça backup do tema atual em **Tema → menu → Fazer backup**.
3. Abra **Tema → menu → Editar HTML**. Substitua o conteúdo do editor pelo XML completo e salve.
4. Configure título, descrição e idioma em **Configurações**.
5. Em **Layout → Páginas**, selecione Sobre mim, Contato e Privacidade publicados para o topo. Use **Menu** para links extras, como marcadores.
6. Edite **Apresentação** (português) ou **Introduction** (inglês) para mudar a abertura. Use o Menu para links de assuntos; este layout em desenvolvimento não tem lateral.
7. Comece com 10 posts por página em **Configurações → Postagens**; o Blogger pode paginar antes. Confira artigos, páginas, busca, paginação e comentários no celular e no computador antes de usar no blog principal.

[Guia de performance](docs/PERFORMANCE.md) · [Posts da home e paginação](docs/HOME.md) · [Instalação e solução de problemas](docs/INSTALLATION.md) · [Personalização](docs/CUSTOMIZATION.md)

## Recursos

- Dois cards de abertura na home, seguidos da lista editorial. Quando o Blogger entrega uma página curta, um pequeno script próprio segue a paginação nativa em direção a 10 posts, sem duplicações.
- Layout responsivo para celulares, tablets e computadores; miniaturas opcionais e entradas com largura completa quando não há imagem.
- Busca nativa, marcadores, paginação, artigos e páginas estáticas.
- Comentários básicos e link para comentar; formulário incorporado e respostas encadeadas ainda pendentes.
- Apresentação, navegação de Páginas e Menu de links extras editáveis; sem lateral e com uma busca no cabeçalho.
- Foco de teclado, link para pular ao conteúdo, rolagem contida em código/tabelas e estilos para impressão.
- **Inter** para interface e **Newsreader** para títulos e leitura, via Google Fonts com fallback local e `display=swap`. Posts/páginas usam 22px e entrelinha de 1,75 por padrão. Ambas usam SIL OFL 1.1; suas licenças são separadas da MIT.
- Sem bibliotecas JavaScript de terceiros ou dependências externas de pacotes Python. A continuação da home é código próprio MIT; a paginação nativa funciona sem JavaScript.

A v0.2.0-rc.4 inclui controles nativos de cores/fontes; a conferência no Designer publicado permanece pendente. Logo em imagem e layout específico de 404 ainda não estão implementados. A prévia usa o CSS real com conteúdo de exemplo; não compila expressões do Blogger.

## Desenvolvimento local

Requer Python 3.10+; `make` é opcional. Node.js 22+ executa as quatro regressões de sintaxe/ciclo de carregamento JavaScript; sem Node, esses checks são pulados localmente. O workflow os inclui quando o Actions está habilitado. A instalação não exige Python nem Node.

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

**Posso mudar cores e layout?** Sim. Comece pelos gadgets de Layout e pelos controles nativos de cores/fontes da v0.2.0-rc.4. A largura de leitura continua como opção avançada de CSS. [Guia de personalização](docs/CUSTOMIZATION.md).

**O tema é preparado para SEO?** Oferece metadados nativos do Blogger, títulos semânticos, links rastreáveis e microdados de artigos. O [guia de busca](docs/SEO.md) cobre Google, Bing, DuckDuckGo, SearXNG e descoberta por IA. Indexação e compatibilidade publicadas ainda precisam de verificação.

**Como escrever posts responsivos?** Use o [guia de postagens e exemplo HTML editável](docs/POSTS.md). Títulos, resumos, tabelas, imagens e vídeos respeitam a coluna de leitura sem exigir scripts nos posts.

## Páginas básicas

[Modelos de Sobre, Contato e Privacidade](docs/PAGES.md) usam Lorem ipsum. Crie e publique as páginas no Blogger e selecione-as em **Layout → Páginas**. O tema não fixa endereços de páginas nem dados de contato. Código e recursos visuais incluídos são MIT; Inter e Newsreader são fontes abertas sob SIL OFL.

## Contribuir por pull requests

Forks públicos e contribuições são bem-vindos. Mudanças de contribuidores na `main` exigem CI e revisão do mantenedor; somente `@erickfaria` integra alterações. Consulte a [política de manutenção](https://github.com/erickfaria/balaio-theme/blob/main/MAINTAINERS.md) e o [guia de contribuição](CONTRIBUTING.md).
