# Instalar e atualizar — v0.2.0-rc.11

[English](en/RELEASE.md) · [Português](RELEASE.md)

A rc.11 acrescenta o widget nativo de contato nas páginas `/p/contato.html` e `/p/contact.html`. Nome opcional, e-mail e mensagem obrigatórios, sem login do visitante. O envio usa o Blogger, sem API key no tema ou biblioteca adicional. Inclui modelos de página e guia de ativação nos dois idiomas. Preserva os gadgets e scripts da rc.10. Importação e entrega da rc.11 ainda precisam de conferência. [Baixar XML português](https://raw.githubusercontent.com/erickfaria/balaio-theme/main/theme/balaio.xml) · [Baixar XML inglês](https://raw.githubusercontent.com/erickfaria/balaio-theme/main/theme/balaio.en.xml). Use o XML atual da main; pacotes antigos contêm outras versões. [Validação](VALIDATION.md) · [Modo automático/manual](PAGES.md).

## O que a versão preserva

- Dois destaques e posts antigos abaixo, com script e gadgets da rc.3. Meta de dez posts e até quatro páginas adicionais, sem duplicações; paginação nativa de fallback. [Home](HOME.md).
- Menu de Páginas e links extras, busca no topo, leitura de 22px e controles de cores/fontes.
- Fontes abertas Inter/Newsreader SIL OFL, layout pastel sem lateral visível e denúncia de abuso no rodapé compacto.
- CI ativo com checks e artefatos de instalação. Base rc.8 instalada em português; nova importação da rc.11 pendente. Prévias não compilam Blogger XML.

## Arquivos de build da candidata

| Arquivo | Uso |
| --- | --- |
| `balaio-0.2.0-rc.11.zip` | Pacote de instalação: templates, guias bilíngues, exemplos de páginas/posts, versão, changelog e avisos MIT/OFL |
| `balaio.xml` | Interface em português |
| `balaio.en.xml` | Interface em inglês |
| `SHA256SUMS.txt` | Checksums SHA-256 dos três arquivos acima |

O ZIP extrai para `balaio-0.2.0-rc.11/`. Escolha um XML em `theme/`; não envie o ZIP como tema Blogger. O pacote não inclui scripts de desenvolvimento, testes de desenvolvimento, backups nem prévias geradas. Os arquivos de código automáticos do GitHub incluem os arquivos de desenvolvimento rastreados.

## Atualizar a partir da v0.1.0

1. Faça backup do XML atual do Blogger e registre gadgets, links e valores do Designer personalizados. Use primeiro um blog de teste separado.
2. Em **Tema → menu → Editar HTML**, cole o XML completo da candidata no idioma escolhido e salve. O comentário do CSS identifica `v0.2.0-rc.11`.
3. Confira as páginas publicadas no menu automático. **Layout → Páginas** define os links iniciais e sua ordem; para escolher somente algumas páginas, use o [modo manual](PAGES.md). **Menu** recebe links extras. Crie o conteúdo em Páginas; o XML não cria nem substitui esses registros.
4. Confira Apresentação e os links do menu. A lateral fica oculta por CSS. Os links de rodapé não são mais exibidos: mova links necessários para Páginas/Menu antes de atualizar. Blocos herdados de Perfil/Atribuição ficam ocultos.
5. Em **Tema → Personalizar → Avançado**, confira cores e **Fonte de posts e páginas**. Valores salvos podem preservar um tamanho anterior; escolha 22px se necessário. Largura de leitura e padrões pastel estão em [CUSTOMIZATION.md](CUSTOMIZATION.md).
6. Se aparecer o tema móvel antigo separado, escolha **Computador** nas configurações móveis. O próprio tema se adapta ao celular. Comece com dez posts em **Configurações → Postagens**; o Blogger pode paginar antes. Consulte [INSTALLATION.md](INSTALLATION.md).
7. Confira se a home completa a lista e se o link de posts anteriores continua do ponto correto. Teste home, artigos completos, páginas estáticas, busca, paginação e comentários antes de atualizar o blog principal. Restaure seu backup para reverter a apresentação, se necessário.

Posts, imagens e URLs não são migrados pelo tema. Guarde os backups personalizados fora do repositório. Não sobrescreva a tag ou os arquivos estáveis existentes ao preparar uma futura versão estável.

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
