# Posts da home e paginação

[English](en/HOME.md) · [Português](HOME.md)

A v0.2.0-rc.3 preserva até **dois destaques** e mostra os demais posts numa lista sóbria abaixo. Quando o Blogger entrega poucos posts, o tema segue as próximas páginas do próprio blog para tentar completar **dez posts no total**. Não usa feed público, biblioteca externa, carrossel ou rolagem infinita.

## Por que apareciam apenas dois posts?

Na inspeção de `www.balaiocientifico.com` em 11/10/2026, a home da v0.2.0-rc.1 tinha dois posts, mesmo com o link seguinte pedindo `max-results=20`. Os demais apareciam na paginação. Isso é compatível com a [paginação automática do Blogger](https://blogger.googleblog.com/2010/02/auto-pagination-on-blogger.html): a plataforma pode reduzir o número entregue conforme o volume de HTML e imagens. O tema não recebe um terceiro post para mostrar se ele não veio na resposta inicial.

A v0.2.0-rc.2 foi observada publicada no mesmo blog com `max-results=50`, mas sua continuação não executava: o Blogger preservou `<![CDATA[` e `]]>` dentro do script e o navegador acusou `Unexpected token '<'`. A **rc.3 corrige os dois marcadores como comentários JavaScript**. Uma reprodução do HTML publicado confirmou dois destaques e oito posts abaixo após apenas essa correção. A prévia antiga retirava os marcadores ao ler o XML e, por isso, não detectou a falha.

A configuração de quantidade é um máximo. Em **Configurações → Postagens**, comece com **10**. Em posts longos, uma **quebra de expansão** após a introdução também pode ajudar a paginação nativa. Ela preserva o artigo completo no permalink. [Ajuda de configurações](https://support.google.com/blogger/answer/9691230?hl=pt-BR) · [Editor de posts](https://support.google.com/blogger/answer/154172?hl=pt-BR).

## Como a continuação funciona

1. Os posts recebidos inicialmente aparecem em HTML: dois cards e, quando disponíveis, as entradas seguintes na lista.
2. Somente na home, um pequeno script próprio consulta o link nativo de publicações anteriores no mesmo domínio. Ele pede apenas a quantidade restante e seleciona o modo web `m=0` para receber a mesma apresentação responsiva.
3. O tema adiciona texto, autoria, data, marcadores e miniaturas das entradas recebidas. Permalinks já visíveis não são repetidos. Scripts, estilos e eventos do HTML recebido não são inseridos na página.
4. Cada página é mostrada por completo antes de atualizar o link de publicações anteriores. A meta não corta uma página pela metade, evitando saltar posts; uma resposta maior pode ultrapassar dez entradas.
5. O carregamento para ao atingir a meta, após quatro páginas adicionais, numa falha, num ciclo sem novidades ou no fim do arquivo. Cada requisição tem timeout de oito segundos. O link nativo continua disponível no primeiro trecho ainda não mostrado; desaparece quando o fim do arquivo foi confirmado.

O resultado depende da rede e da quantidade de posts disponíveis. Sem JavaScript, sem suporte a fetch ou com falha na rede, os posts iniciais e a paginação nativa continuam funcionando. Busca, marcadores, arquivos, artigos e páginas estáticas não fazem esse carregamento extra. URLs, conteúdo publicado e configurações do Blogger não são alterados.

## Personalizar ou desligar

No XML, procure o elemento `id='postlist'`:

```xml
<div class='posts' id='postlist' data-home-posts='10' data-page-limit='4' data-list-title='Mais leituras'>
```

- `data-home-posts`: meta total, contando os destaques. Padrão 10; limitada pelo código ao intervalo 2–40.
- `data-page-limit`: máximo de páginas adicionais. Padrão 4; intervalo 0–6. Defina **0** para desligar a continuação automática e manter apenas a paginação nativa.
- `data-list-title`: título usado quando a lista começa vazia. A variante inglesa já contém a tradução.

Meta alta pode aumentar tráfego e tempo de carregamento. Dez posts e quatro páginas são os padrões recomendados. O limite de requisições evita baixar todo o arquivo do blog. Os destaques continuam automáticos; o tema não escolhe posts por interesse nem altera sua ordem cronológica.

## Conferir após importar

Confira dois destaques, a lista abaixo, ausência de posts repetidos e o destino de **Publicações anteriores**. Abra um post da lista, uma busca e uma página fixa. Teste também uma rede lenta ou JavaScript desligado. Se só houver dois posts, confirme que o XML identifica `v0.2.0-rc.3` e que o link nativo seguinte funciona. Em uma instalação antiga da rc.2, importe o XML completo da rc.3; aumentar a quantidade de posts não corrige o erro de sintaxe. O console do navegador não deve apresentar `Unexpected token '<'` no script do tema.

Os artigos e links nativos continuam acessíveis aos rastreadores. A continuação por JavaScript é um complemento para leitores; sua execução por mecanismos de busca não é garantida. [SEO e rastreadores](SEO.md) · [Validação e limitações](VALIDATION.md) · [Instalação](INSTALLATION.md).
