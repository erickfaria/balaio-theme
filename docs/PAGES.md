# Páginas básicas do Blogger e navegação

[English](en/PAGES.md) · [Português](PAGES.md)

O Balaio inclui modelos editáveis de corpo das páginas **Sobre**, **Contato** e **Privacidade**. Eles contêm Lorem ipsum para desenvolver o layout, sem conteúdo final. O exemplo de privacidade não é uma política de privacidade. O contato não inclui formulário, destinatário nem coleta de dados.

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
5. Em **Layout → Menu**, adicione as URLs na ordem desejada, por exemplo Sobre, Contato e Privacidade. Início já está presente; não duplique.

O XML instala layouts e gadgets, não registros de páginas. Os exemplos separados permitem importar o tema sem sobrescrever o conteúdo das páginas. Renomeie, reordene, remova links e adicione páginas pelo Layout sem editar o XML. [Instruções do Blogger](https://support.google.com/blogger/answer/165955?hl=pt-BR).

## Formato das páginas

Páginas estáticas usam a mesma coluna responsiva dos artigos, sem autor/data de postagem nem comentários. Seus dados estruturados usam `WebPage`, em vez de `BlogPosting`. O corpo começa em H2; o título fornece o H1. Imagens, figuras, tabelas e contêineres de vídeo compartilham os [estilos de posts](POSTS.md).

O menu superior usa links comuns, quebra linhas em telas pequenas e destaca o link atual quando sua URL corresponde exatamente à URL da página no Blogger. Não há dependência de script de dropdown ou menu hambúrguer. Prefira nomes curtos e URLs corretas; aliases, parâmetros e diferenças de barra final podem impedir o destaque de página atual.

Teste cada página e os dois menus em celular após importar. As prévias usam conteúdo fictício e não verificam o comportamento real no Blogger.
