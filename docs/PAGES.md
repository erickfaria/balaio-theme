# Páginas básicas do Blogger e navegação

[English](en/PAGES.md) · [Português](PAGES.md)

O Balaio inclui modelos editáveis de corpo das páginas **Sobre**, **Contato** e **Privacidade**. Sobre e Privacidade contêm Lorem ipsum para desenvolver o layout. O exemplo de privacidade não é uma política de privacidade. Contato tem texto genérico pronto para editar e, na rc.11, um widget nativo separado, sem login do visitante. [Ativar o formulário](CONTACT.md).

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
5. Com a rc.8, as páginas publicadas aparecem automaticamente no menu após o carregamento do feed público. Em **Layout → Páginas**, você também pode definir links iniciais, nomes e ordem. Use **Menu** para links extras; evite repetir Início.

O XML instala layouts e gadgets, não registros de páginas. Os exemplos separados permitem importar o tema sem sobrescrever o conteúdo das páginas. Os links configurados no Layout mantêm seus nomes e sua ordem; o modo automático completa as demais páginas públicas. Para escolher exatamente quais páginas exibir, desligue o modo automático conforme abaixo. [Instruções do Blogger](https://support.google.com/blogger/answer/165955?hl=pt-BR).

## Formato das páginas

Páginas estáticas usam a mesma coluna responsiva dos artigos, sem autor/data de postagem nem comentários. Seus dados estruturados usam `WebPage`, em vez de `BlogPosting`. O corpo começa em H2; o título fornece o H1. Imagens, figuras, tabelas e contêineres de vídeo compartilham os [estilos de posts](POSTS.md).

O menu superior usa links comuns, quebra linhas em telas pequenas e destaca a página atual com sublinhado e peso de fonte, sem fundo colorido. A altura acompanha as linhas, inclusive quando o CSS nativo do Blogger define 30px para a classe navbar. Não há dependência de script de dropdown ou menu hambúrguer. Prefira nomes curtos e URLs corretas; aliases, parâmetros e diferenças de barra final podem impedir o destaque de página atual.

Teste cada página e o menu superior em celular após importar. As prévias usam conteúdo fictício e não verificam o comportamento real no Blogger.

## Páginas automáticas — rc.8

O elemento de navegação inclui `data-auto-pages='true'` por padrão. Um script próprio consulta o **feed público resumido de páginas do próprio blog**, sem chave de API ou login, e acrescenta até 150 páginas publicadas. Os links já configurados aparecem primeiro; os novos vêm em ordem alfabética. URLs repetidas, inclusive variantes móveis, são ignoradas. Rascunhos não fazem parte do feed público.

Na rc.9, o menu faz uma consulta ao abrir ou atualizar a página, revalidando o cache HTTP (`cache: no-cache`), sem guardar uma lista na sessão. **Publicar adiciona a página; voltar para rascunho remove o link automático na próxima atualização**, assim que o feed do Blogger refletir a mudança. Criar ou salvar somente um rascunho não o inclui no menu. Uma aba já aberta não muda sozinha: atualize-a; não há polling. Links adicionados manualmente no gadget continuam sob seu controle e devem ser removidos ali quando necessário.

O carregamento tem timeout de seis segundos e prioridade baixa. Falha de rede, feed indisponível ou JavaScript desligado preservam os links nativos configurados no gadget Páginas. O tema não fixa nomes, domínio ou endereços das páginas do Balaio Científico para outras instalações.

## Escolher somente algumas páginas ou ordenar todo o menu

No XML, altere **apenas** o atributo da navegação:

```xml
<nav aria-label='Navegação principal' class='navigation' data-auto-pages='false'>
```

Depois, em **Layout → Páginas → Editar**, adicione os itens com o título e a URL real da página publicada e ordene-os. Algumas interfaces mostram seleção de páginas; outras usam **Adicionar novo item**. Salve o gadget e o Layout. Esse modo respeita exatamente a lista configurada e não consulta o feed.

No modo automático, desmarcar uma página apenas no gadget não a exclui da descoberta do feed público. Use o modo manual para controlar quais páginas públicas aparecem no menu.

## Links importantes para buscas e funcionamento sem JavaScript

Os itens configurados no gadget são renderizados no HTML inicial. Os itens descobertos automaticamente dependem de JavaScript. Para Sobre, Contato e Privacidade sempre estarem disponíveis também sem script, configure esses links no gadget; o modo automático evita duplicá-los. Isso não garante indexação ou posição em buscas.
