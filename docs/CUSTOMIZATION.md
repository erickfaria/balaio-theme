# Personalizar o Balaio

## Conteúdo e navegação

- **Título e descrição:** configurações do blog. O cabeçalho usa o texto configurado.
- **Abertura:** gadget **Apresentação** no Layout. Edite o texto, preservando uma única tag `<h1>`. Pode remover o gadget para uma home mais direta.
- **Menu:** gadget **Menu**, com links de páginas e marcadores. Início já está no código; evite cadastrar um segundo link para ele.
- **Assuntos:** gadget de marcadores na lateral.
- **Rodapé e lateral:** aceitam gadgets no Layout. Confira sempre o resultado em celular.

## Cards de abertura

Na home, as três primeiras publicações da página recebem o formato de card. Não há seleção manual por enquanto. Os posts seguintes aparecem uma única vez na lista. Busca, marcadores e arquivos usam apenas a lista comum.

Se houver menos de três posts, o tema exibe somente os disponíveis. Posts sem miniatura preservam título, resumo e autoria. Para mudar a quantidade, mantenha os limites dos dois loops coerentes no widget Blog: os cards usam `index < 3`, a lista começa em `index >= 3` e o título da lista aparece em `index == 3`.

## Paleta e tipografia

Edite as variáveis `:root` no bloco `b:skin` do XML. `--paper` controla o fundo, `--ink` o texto, `--muted` os textos secundários, `--accent` os links e botões, `--line` as divisórias e `--wash` as superfícies suaves. Os tons dos segundo e terceiro cards estão nas regras `nth-child` de `.opening-cards`.

`--sans` e `--serif` controlam as famílias de fonte. O tema solicita Inter e Newsreader ao Google Fonts e usa fontes locais se o serviço não responder. `display=swap` mantém texto disponível durante o carregamento. Essa configuração faz requisições a `fonts.googleapis.com` e `fonts.gstatic.com`.

Para usar somente fontes locais, remova os três links de fontes no `<head>` e substitua as variáveis por `system-ui,sans-serif` e `Georgia,serif`. Para hospedar fontes por conta própria, configure URLs HTTPS em `@font-face` e preserve as licenças em `licenses/`.

## Conferir mudanças

Gere novamente a prévia após editar o XML. Confira contraste, títulos longos, posts com e sem imagem e navegação por teclado. Mudanças nos dados ou widgets precisam ser verificadas também por importação num Blogger de teste.
