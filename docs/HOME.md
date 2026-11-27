# Posts da home e paginação

[English](en/HOME.md) · [Português](HOME.md)

O tema mostra até **dois destaques** e lista os demais posts abaixo. Quando o Blogger entrega uma home curta com link para posts antigos, a continuação pode seguir a paginação nativa em direção a **dez posts**.

## Por que apareciam apenas dois posts?

Na inspeção de `www.balaiocientifico.com` em 11/10/2026, a home da v0.2.0-rc.1 tinha dois posts, mesmo com o link seguinte pedindo `max-results=20`. Os demais apareciam na paginação. Isso é compatível com a [paginação automática do Blogger](https://blogger.googleblog.com/2010/02/auto-pagination-on-blogger.html): a plataforma pode reduzir o número entregue conforme o volume de HTML e imagens. O tema não recebe um terceiro post para mostrar se ele não veio na resposta inicial.

A v0.2.0-rc.2 foi observada publicada no mesmo blog com `max-results=50`, mas sua continuação não executava: o Blogger preservou `<![CDATA[` e `]]>` dentro do script e o navegador acusou `Unexpected token '<'`. A **rc.3 corrige os dois marcadores como comentários JavaScript**. Uma reprodução do HTML publicado confirmou dois destaques e oito posts abaixo após apenas essa correção. A prévia antiga retirava os marcadores ao ler o XML e, por isso, não detectou a falha.

A configuração de quantidade é um máximo. Em **Configurações → Postagens**, comece com **10**. Em posts longos, uma **quebra de expansão** após a introdução também pode ajudar a paginação nativa. Ela preserva o artigo completo no permalink. [Ajuda de configurações](https://support.google.com/blogger/answer/9691230?hl=pt-BR) · [Editor de posts](https://support.google.com/blogger/answer/154172?hl=pt-BR).

A rc.3 foi confirmada pelo proprietário e observada funcionando no blog em 11/10/2026, com dez posts distintos e console sem erros. A rc.6 recupera a estrutura e o script dessa versão. A importação da rc.6 foi confirmada pelo proprietário em 12/10/2026; a inspeção do blog público mostrou dois destaques e oito posts antigos, sem erros no console. [Performance e medições](PERFORMANCE.md).

## Como a continuação funciona

1. Os posts recebidos inicialmente aparecem em HTML: dois cards e, quando disponíveis, as entradas seguintes na lista.
2. O gadget Blog1 inclui o script só na home com posts abaixo da meta, link para posts antigos e limite de páginas maior que zero. Ele espera o HTML inicial e usa um período ocioso quando disponível. As requisições usam prioridade baixa e pedem a quantidade restante.
3. O tema reconstrói texto, autoria, data, marcadores e miniaturas somente das entradas recebidas em `Blog1`. Permalinks já visíveis não são repetidos. Scripts, estilos e eventos do HTML recebido não são inseridos na página.
4. Cada página é mostrada por completo antes de atualizar o link de publicações anteriores. A meta não corta uma página pela metade, evitando saltar posts; uma resposta maior pode ultrapassar dez entradas.
5. O carregamento para ao atingir a meta, após quatro páginas adicionais, numa falha, num ciclo sem novidades ou no fim do arquivo. Cada requisição tem timeout de oito segundos. O link nativo continua disponível no primeiro trecho ainda não mostrado; desaparece quando o fim do arquivo foi confirmado.

O resultado depende da rede e da quantidade de posts disponíveis. Sem JavaScript, sem suporte a fetch ou com falha na rede, os posts iniciais e a paginação nativa continuam funcionando. Busca, marcadores, arquivos, artigos e páginas estáticas não fazem esse carregamento extra. URLs, conteúdo publicado e configurações do Blogger não são alterados.

## Personalizar ou desligar

Procure `homePostTarget` e `homePageLimit` dentro de Blog1 no XML. Esses valores controlam a renderização do template e o comportamento no navegador.

- `homePostTarget`: meta contando os destaques. Padrão 10, intervalo 2–40.
- `homePageLimit`: máximo de páginas adicionais. Padrão 4, intervalo 0–6. Use 0 para omitir o script e manter a paginação nativa.

Valores maiores podem aumentar o tráfego. Ao atualizar um tema personalizado, transfira os valores anteriores de `data-home-posts` e `data-page-limit` para essas variáveis.

## Conferir após importar

Confira dois destaques, a lista abaixo, ausência de posts repetidos e o destino de **Publicações anteriores**. Abra um post da lista, uma busca e uma página fixa. Teste também uma rede lenta ou JavaScript desligado. Se só houver dois posts, confirme a versão publicada e confira se o link nativo seguinte funciona. Em uma instalação antiga da rc.2, importe o XML completo da candidata atual; aumentar a quantidade de posts não corrige o erro de sintaxe. O console do navegador não deve apresentar `Unexpected token '<'` no script do tema.

Os artigos e links nativos continuam acessíveis aos rastreadores. A continuação por JavaScript é um complemento para leitores; sua execução por mecanismos de busca não é garantida. [SEO e rastreadores](SEO.md) · [Validação e limitações](VALIDATION.md) · [Instalação](INSTALLATION.md).
