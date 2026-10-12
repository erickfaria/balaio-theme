# Personalizar o Balaio

[English](en/CUSTOMIZATION.md) · [Português](CUSTOMIZATION.md)

## Conteúdo e navegação

- **Título e descrição:** configurações do blog. O cabeçalho usa o texto configurado.
- **Abertura:** gadget **Apresentação** no Layout. Edite o texto, preservando uma única tag `<h1>`. Se remover o gadget, mantenha um único H1 descritivo na home.
- **Páginas:** selecione páginas publicadas no Layout e ordene sua navegação no topo.
- **Menu:** adicione links extras de marcadores ou sites externos; evite duplicar Início.
- **Assuntos:** adicione links de marcadores no Menu.
- **Lateral:** removida no layout em desenvolvimento; a busca permanece no cabeçalho.

## Cards de abertura

Na home, as duas primeiras publicações da página recebem o formato de card. Não há seleção manual por enquanto. Os posts seguintes aparecem uma única vez na lista. Busca, marcadores e arquivos usam apenas a lista comum. A continuação automática é exclusiva da home; veja [HOME.md](HOME.md) para meta de posts, limite de requisições e como desativá-la.

Se houver menos de dois posts, os cards exibem somente os disponíveis. Posts sem miniatura preservam título, resumo e autoria. Para mudar a quantidade, mantenha os limites dos dois loops coerentes no widget Blog: os cards usam `index < 2`, a lista começa em `index >= 2` e o título da lista aparece em `index == 2`.

## Controles nativos de cores e fontes

A v0.2.0-rc.4 inclui controles em **Tema → Personalizar → Avançado**, usando [variáveis de cor e fonte documentadas pelo Blogger](https://support.google.com/blogger/answer/46871?hl=en). Importe o XML atualizado primeiro em um blog de teste. Estes controles ainda precisam de confirmação no Designer publicado. Eles não existem na v0.1.0 estável anterior.

Os controles abrangem fundo da página, textos principal e secundário, links/botões, divisórias, superfícies pastel verde/areia/azul, fonte da interface e fonte de posts/páginas. Escolha fundos claros e texto escuro. A paleta padrão passa na verificação de contraste mínimo de 4,5:1 para texto comum sobre as quatro superfícies de leitura/cards. Cores personalizadas precisam de nova conferência de contraste.

A interface começa em 17px e o corpo de posts/páginas em 22px, inclusive no celular. A fonte de leitura também se aplica aos títulos, preservando seus tamanhos responsivos. Largura de leitura, espaçamento e estrutura continuam definidos pelo tema: coluna centralizada, fundo simples e divisórias discretas.

Inter e Newsreader continuam como padrões abertos sob SIL OFL. Escolher outra fonte não adiciona seus arquivos ao repositório; confira a licença antes de redistribuir arquivos de fontes. Os links padrão do Google Fonts usam `display=swap` e fazem requisições a `fonts.googleapis.com` e `fonts.gstatic.com`.

### Editar diretamente o XML

No comentário CSS do início de `b:skin`, edite uma declaração `<Variable>`. Altere `default` e `value` ao definir um novo padrão no código; as escolhas do Designer instalado ficam em `value`. Exemplo:

```xml
<Variable name="washcolor" description="Superfície verde pastel" type="color" default="#edf5ef" value="#edf5ef"/>
```

Preserve a ligação entre as referências `$variavel` em `:root` e essas declarações. A prévia resolve os valores salvos e valida nomes ausentes ou duplicados. Para usar apenas fontes locais, remova os três links de fontes do `head` e configure `interfacefont` como `normal 400 17px system-ui, sans-serif` e `readingfont` como `normal 400 22px serif`. Fontes hospedadas por você podem usar URLs HTTPS em `@font-face`, preservando os avisos OFL.

`--reading-width:760px` e `--width:1120px` continuam como opções avançadas de CSS. Altere apenas após conferir o celular e o comprimento das linhas. No código do repositório, edite o português e regenere o inglês com `python3 scripts/build_locales.py`. Não precisa de ferramentas de build para editar diretamente um XML instalado no Blogger.

## Conferir mudanças

Gere novamente a prévia após editar o XML. Confira contraste, títulos longos, posts com e sem imagem e navegação por teclado. Mudanças nos dados ou widgets precisam ser verificadas também por importação num Blogger de teste.

## Idioma da interface

Use `theme/balaio.xml` para português ou `theme/balaio.en.xml` para inglês. Configure também o idioma do blog no Blogger. A versão inglesa é gerada com `python3 scripts/build_locales.py`; edite o português e regenere para preservar estilos iguais. Posts não são traduzidos pelo tema.

A MIT não exige crédito visível no site. Preserve os avisos de licença no código redistribuído.

## Páginas básicas

[Modelos de Sobre, Contato e Privacidade](PAGES.md) usam Lorem ipsum. Publique as páginas no Blogger e selecione-as em **Layout → Páginas**. O tema não fixa endereços de páginas nem dados de contato. Código e recursos visuais incluídos são MIT; Inter e Newsreader são fontes abertas sob SIL OFL.

## Layout compacto no celular

Em telas de até 800px, cabeçalho e apresentação usam espaçamento menor. Não há painel lateral ou arquivo mensal. As publicações usam a largura disponível do conteúdo. Posts e páginas estáticas preservam a estrutura de leitura e a paleta pastel.

## Fim dos posts e páginas

A branch em desenvolvimento remove a lateral de todas as páginas e mostra apenas Denunciar abuso num rodapé compacto. O último pacote publicado v0.2.0-rc.4 ainda mantém a lateral nas listagens. Gadgets herdados de Perfil, Atribuição, BlogSearch, BlogArchive, FeaturedPost e ReportAbuse ficam ocultos pelo CSS. Remova os gadgets antigos no Layout se o Blogger os preservar após importar, para eliminar também seu HTML. Selecione Contato e Privacidade no gadget Páginas do topo. Os avisos de licença permanecem no código e na distribuição. Importe novamente o XML atualizado para aplicar estas mudanças; o pacote estável v0.1.0 mantém o rodapé original.

O padrão de leitura é 22px com entrelinha de 1,75. Configurações salvas no Designer podem preservar um tamanho anterior: selecione 22px em **Fonte de posts e páginas** após importar, se necessário.
