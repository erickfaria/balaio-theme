# Páginas básicas do Blogger e navegação

[English](en/PAGES.md) · [Português](PAGES.md)

O Balaio inclui modelos editáveis de corpo das páginas **Sobre**, **Contato** e **Privacidade**. Sobre/Privacidade usam Lorem ipsum; o exemplo de privacidade não é uma política de privacidade. O exemplo de Contato contém `class="balaio-contact-page"`, que exibe o formulário nativo incluído no tema, com qualquer endereço gerado pelo Blogger. [Ativação simples](CONTACT.md).

| Título da página | Corpo para copiar no Blogger |
| --- | --- |
| Sobre | [about.pt-BR.html](../examples/pages/about.pt-BR.html) |
| Contato | [contact.pt-BR.html](../examples/pages/contact.pt-BR.html) |
| Privacidade | [privacy.pt-BR.html](../examples/pages/privacy.pt-BR.html) |

## Crie as páginas após importar o tema

1. Abra **Blogger → Páginas → Nova página**. Preencha o título separadamente.
2. No modo HTML do editor, cole o conteúdo do exemplo. Não cole um documento HTML inteiro: o tema fornece o contêiner da página e o H1.
3. Visualize e salve como rascunho enquanto estiver usando placeholders. Substitua o texto antes de publicar no blog público.
4. Depois de publicar, copie a URL real fornecida pelo Blogger. O endereço depende da plataforma e dos títulos; o tema não presume caminhos `/p/` fixos.
5. Em **Layout → Páginas**, escolha quais páginas publicadas aparecem no menu e defina a ordem. Use **Menu** para links extras e mantenha Início em um só lugar.

Use **Páginas** para criar conteúdo e **Layout → Páginas** para selecionar links. Se usava a descoberta por feed numa versão anterior, coloque os links desejados nos gadgets Páginas ou Menu antes de atualizar. [Instruções do Blogger](https://support.google.com/blogger/answer/165955?hl=pt-BR).

## Formato das páginas

Páginas estáticas usam a mesma coluna responsiva dos artigos, sem autor/data de postagem nem comentários. Seus dados estruturados usam `WebPage`, em vez de `BlogPosting`. O corpo começa em H2; o título fornece o H1. Imagens, figuras, tabelas e contêineres de vídeo compartilham os [estilos de posts](POSTS.md).

O menu superior usa links comuns, quebra linhas em telas pequenas e destaca a página atual com sublinhado e peso de fonte, sem fundo colorido. A altura acompanha as linhas, inclusive quando o CSS nativo do Blogger define 30px para a classe navbar. Não há dependência de script de dropdown ou menu hambúrguer. Prefira nomes curtos e URLs corretas; aliases, parâmetros e diferenças de barra final podem impedir o destaque de página atual.

Teste cada página e o menu superior em celular após importar. As prévias usam conteúdo fictício e não verificam o comportamento real no Blogger.

## Escolher somente algumas páginas ou ordenar todo o menu

Em **Layout → Páginas → Editar**, selecione as páginas que deseja mostrar e ajuste a ordem. Se o gadget mostrar **Adicionar novo item**, use a URL publicada e o nome desejado. Salve o gadget e o Layout.

## Links importantes para buscas e funcionamento sem JavaScript

Os dois gadgets nativos entregam os links no HTML inicial. Coloque Sobre, Contato e Privacidade em um deles para dar a leitores e rastreadores um link direto.

## Apostilas, projetos e pequenas Wikis

O [guia de conteúdo de referência](REFERENCE.md) descreve a curadoria de links na home e o [modelo de página longa](../examples/pages/guide.pt-BR.html), com índice nativo e âncoras. Um conteúdo pilar pode continuar sendo um post com o permalink atual.
