# Instalar e atualizar — v0.2.0-rc.17

[English](en/RELEASE.md) · [Português](RELEASE.md)

**v0.2.0-rc.17** simplifica o cabeçalho e a abertura da home, integra Assuntos ao menu e define 24px como padrão de leitura. O gadget Páginas entrega os links no HTML inicial. A descoberta automática é opcional. [Configuração do menu](PAGES.md).

Artigos e páginas estáticas mostram o título do conteúdo primeiro. O Blogger fornece canonical e descrições de pesquisa. As miniaturas oferecem 320w e 640w quando disponíveis. A continuação da home curta usa prioridade baixa, e a seção lateral legada fica reservada ao editor de Layout. [SEO](SEO.md) · [Performance](PERFORMANCE.md).

Use um blog de teste separado antes de atualizar a produção. [Downloads da versão](https://github.com/erickfaria/balaio-theme/releases/tag/v0.2.0-rc.17) · [Validação](VALIDATION.md).

## Outros recursos

- Dois destaques e paginação nativa. Uma home curta pode consultar até quatro páginas adicionais em direção à meta de dez posts. [Home](HOME.md)
- Busca nativa, aparência configurável, contato opcional e Analytics quando configurado no Blogger. [Personalização](CUSTOMIZATION.md) · [Contato](CONTACT.md) · [Analytics](ANALYTICS.md)
- Inter e Newsreader sob SIL OFL 1.1, além de tema e exemplos sob MIT. [Autoria e licenças](PROVENANCE.md)

## Arquivos de build da candidata

| Arquivo | Uso |
| --- | --- |
| `balaio-0.2.0-rc.17.zip` | Pacote de instalação: templates, guias bilíngues, exemplos HTML/Markdown de páginas e materiais, versão, changelog e avisos MIT/OFL |
| `balaio.xml` | Interface em português |
| `balaio.en.xml` | Interface em inglês |
| `SHA256SUMS.txt` | Checksums SHA-256 dos três arquivos acima |

O ZIP extrai para `balaio-0.2.0-rc.17/`. Escolha um XML em `theme/`; não envie o ZIP como tema Blogger. O pacote não inclui scripts de desenvolvimento, testes de desenvolvimento, backups nem prévias geradas. Os arquivos de código automáticos do GitHub incluem os arquivos de desenvolvimento rastreados.

## Atualizar a partir de uma versão anterior

1. Faça backup do XML atual do Blogger e registre gadgets, links e valores do Designer personalizados. Use primeiro um blog de teste separado.
2. Em **Tema → menu → Editar HTML**, cole o XML completo da candidata no idioma escolhido e salve. O comentário do CSS identifica `v0.2.0-rc.17`.
3. Confira os links em **Layout → Páginas** e use **Menu** para links extras. Se dependia dos links descobertos pelo feed, configure-os no gadget ou [reative o modo automático](PAGES.md#páginas-automáticas-opcionais). Crie o conteúdo em Páginas.
4. Confira Apresentação, Assuntos e os gadgets legados no editor de Layout. Mova os links que ainda usa para Páginas ou Menu. Se quiser a home mais compacta, encurte uma apresentação já salva.
5. Em **Tema → Personalizar → Avançado**, confira cores e **Fonte de posts e páginas**. Valores salvos podem preservar um tamanho anterior; escolha 24px se necessário. Largura de leitura e padrões pastel estão em [CUSTOMIZATION.md](CUSTOMIZATION.md).
6. Se aparecer o tema móvel antigo separado, escolha **Computador** nas configurações móveis. O próprio tema se adapta ao celular. Comece com dez posts em **Configurações → Postagens**; o Blogger pode paginar antes. Consulte [INSTALLATION.md](INSTALLATION.md).
7. Confira se a home completa a lista e se o link de posts anteriores continua do ponto correto. Teste home, artigos completos, páginas estáticas, busca, paginação e comentários antes de atualizar o blog principal. Restaure seu backup para reverter a apresentação, se necessário.

Posts, imagens e URLs não são migrados pelo tema. Guarde os backups personalizados fora do repositório. Não sobrescreva a tag ou os arquivos estáveis existentes ao preparar uma futura versão estável.

### Conferir o tema importado

No blog de teste, confira título, canonical e descrição na home, em um artigo e em uma página estática, incluindo `?m=1`. Teste Assuntos por teclado, a busca, a paginação nativa e os tamanhos das miniaturas. Confira os gadgets legados no editor de Layout. [Auditor de SEO](SEO.md) · [Validação](VALIDATION.md).

## Conferir os downloads

Baixe os três arquivos e o checksum na mesma pasta:

```sh
sha256sum -c SHA256SUMS.txt
```

## Licenças e pacote reproduzível

Código/design/exemplos próprios são MIT. Inter e Newsreader são SIL OFL 1.1; os avisos ficam em `licenses/`. Google Fonts é hospedagem opcional e Blogger é uma plataforma externa. [Inventário de recursos](PROVENANCE.md).

Na tag correspondente, com Python 3.10+, Node.js 22+ (checks de sintaxe) e Git:

```sh
make check
python3 scripts/build_release.py --output /tmp/balaio-release
```

O script exige checkout limpo e com commit, usa lista permitida de arquivos rastreados e entradas determinísticas no ZIP, e cria checksums SHA-256. Gere fora do repositório ou em `dist/`, ignorado pelo Git.

## Configurar os materiais web

Em **Layout → Guias e projetos**, escolha até três URLs publicadas, como sua Biblioteca, apostila ou projeto. **Assuntos** configura os marcadores no cabeçalho. Os [modelos e o contrato de publicação](MATERIALS.md) mostram como usar HTML comum ou um publicador Markdown para gerar índices. A instalação do XML não cria conteúdo nem altera agendamentos. A foto do autor é opcional e depende dos campos fornecidos pelo Blogger.

Use a [configuração curta do Layout](LAYOUT.md) para selecionar cinco a sete assuntos, poucos links no menu e até três destaques. O tema não impõe nomes de categorias nem corta links automaticamente.
