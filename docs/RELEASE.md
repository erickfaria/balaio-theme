# Instalar e atualizar — v0.2.0-rc.1

[English](en/RELEASE.md) · [Português](RELEASE.md)

[Baixar candidata no GitHub](https://github.com/erickfaria/balaio-theme/releases/tag/v0.2.0-rc.1).

Esta é uma **versão candidata**, ainda não a próxima estável validada. Vinte testes locais e CI passam; nova importação, controles do Designer e comportamento dos gadgets no Blogger seguem pendentes. [A v0.1.0 continua como alternativa estável](https://github.com/erickfaria/balaio-theme/releases/tag/v0.1.0). Consulte [evidências de validação](VALIDATION.md).

## O que mudou

- Texto de posts/páginas de 22px, entrelinha de 1,75, H2/H3 mais claros e as mesmas Inter/Newsreader abertas.
- Cabeçalho e assuntos compactos no celular, Páginas nativas no topo e busca móvel corrigida.
- Controles nativos de cores pastel/fontes; sem rodapé, Perfil ou Atribuição visíveis.
- Três cards e os demais posts recebidos em lista; guias para nove posts, páginas fixas e modo móvel antigo.

## Arquivos

| Arquivo | Uso |
| --- | --- |
| `balaio-0.2.0-rc.1.zip` | Pacote de instalação: templates, guias bilíngues, exemplos de páginas/posts, versão, changelog e avisos MIT/OFL |
| `balaio.xml` | Interface em português |
| `balaio.en.xml` | Interface em inglês |
| `SHA256SUMS.txt` | Checksums SHA-256 dos três arquivos acima |

O ZIP extrai para `balaio-0.2.0-rc.1/`. Escolha um XML em `theme/`; não envie o ZIP como tema Blogger. O pacote não inclui scripts, testes de desenvolvimento, backups nem prévias geradas. Os arquivos de código automáticos do GitHub incluem os arquivos de desenvolvimento rastreados.

## Atualizar a partir da v0.1.0

1. Faça backup do XML atual do Blogger e registre gadgets, links e valores do Designer personalizados. Use primeiro um blog de teste separado.
2. Em **Tema → menu → Editar HTML**, cole o XML completo da candidata no idioma escolhido e salve. O comentário do CSS identifica `v0.2.0-rc.1`.
3. Em **Layout → Páginas**, selecione Sobre mim, Contato e Privacidade publicados e confira a posição do gadget. **Menu** recebe links extras. Crie o conteúdo em Páginas; o XML não cria nem substitui esses registros.
4. Confira Apresentação e gadgets da lateral. Os links de rodapé não são mais exibidos: mova links necessários para Páginas/Menu antes de atualizar. Blocos herdados de Perfil/Atribuição ficam ocultos.
5. Em **Tema → Personalizar → Avançado**, confira cores e **Fonte de posts e páginas**. Valores salvos podem preservar um tamanho anterior; escolha 22px se necessário. Largura de leitura e padrões pastel estão em [CUSTOMIZATION.md](CUSTOMIZATION.md).
6. Se aparecer o tema móvel antigo separado, escolha **Computador** nas configurações móveis. O próprio tema se adapta ao celular. Comece com nove posts em **Configurações → Postagens**; o Blogger pode paginar antes. Consulte [INSTALLATION.md](INSTALLATION.md).
7. Teste home, artigos completos, páginas estáticas, busca, paginação e comentários antes de atualizar o blog principal. Restaure seu backup para reverter a apresentação, se necessário.

Posts, imagens e URLs não são migrados pelo tema. Guarde os backups personalizados fora do repositório. Não sobrescreva a tag ou os arquivos estáveis existentes ao preparar uma futura versão estável.

## Conferir os downloads

Baixe os três arquivos e o checksum na mesma pasta:

```sh
sha256sum -c SHA256SUMS.txt
```

## Licenças e pacote reproduzível

Código/design/exemplos próprios são MIT. Inter e Newsreader são SIL OFL 1.1; os avisos ficam em `licenses/`. Google Fonts é hospedagem opcional e Blogger é uma plataforma externa. [Inventário de recursos](PROVENANCE.md).

Na tag correspondente, com Python 3.10+ e Git:

```sh
make check
python3 scripts/build_release.py --output /tmp/balaio-release
```

O script exige checkout limpo e com commit, usa lista permitida de arquivos rastreados e entradas determinísticas no ZIP, e cria checksums SHA-256. Gere fora do repositório ou em `dist/`, ignorado pelo Git.
