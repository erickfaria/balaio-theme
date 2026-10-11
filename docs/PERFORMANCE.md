# Performance e um tema Blogger limpo

[English](en/PERFORMANCE.md) · [Português](PERFORMANCE.md)

A v0.2.0-rc.4 mantém o layout minimalista pastel, leitura de 22px e fontes abertas Inter/Newsreader. Não foram adicionados analytics, biblioteca JavaScript externa, carrossel ou dependência de execução. Importe o XML completo; este guia não altera seu conteúdo ou configurações do Blogger.

## O que o tema otimiza

- Solicita Inter nos pesos 400–750 e Newsreader 400–700 como intervalos variáveis, incluindo os pesos 650/750 existentes na interface. Mantém uma folha Google Fonts, duas pré-conexões, `display=swap` e alternativas locais. [Intervalos no Google Fonts CSS2](https://developers.google.com/fonts/docs/css2).
- Não renderiza a seção lateral no HTML de artigos/páginas estáticas, em vez de apenas ocultá-la. Home, busca, marcadores e arquivos por data mantêm a lateral. O CSS de Perfil/Atribuição continua como proteção para migrações.
- Inicia a continuação da home após `load` e uma oportunidade ociosa com timeout de um segundo; sem `requestIdleCallback`, cede um ciclo com timer. Os primeiros posts e a navegação nativa continuam disponíveis enquanto os demais chegam. O timeout começa após `load`; um recurso inicial lento pode atrasar a continuação. [Agendamento ocioso](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestIdleCallback).
- Indica prioridade baixa nas requisições; o navegador decide como aplicar a indicação. Mantém chamadas sequenciais, meta de dez posts, limite de quatro páginas, timeout de oito segundos, filtragem de duplicações e paginação nativa em caso de falha. Não antecipa o arquivo inteiro. [Opções de requisição](https://developer.mozilla.org/en-US/docs/Web/API/RequestInit#priority).
- Lê cards e paginação somente em `Blog1`. Reconstrói nós seguros de texto/links/miniaturas; scripts, estilos e eventos recebidos ficam inertes. Remove somente o parâmetro móvel `m` dos links adicionais de posts/marcadores; outros parâmetros e fragmentos são preservados.
- Preserva título/canonical/metadados nativos e microdados do conteúdo visível. Não adiciona scripts específicos para rastreadores nem metadados duplicados.

## Evidências medidas e limites

Medições em 11/10/2026 no blog público em português com rc.3 e nas respostas oficiais das fontes, antes de importar rc.4:

| Observação | Antes | Otimizado ou evitável |
| --- | --- | --- |
| CSS Google Fonts descomprimido, agente Chrome 130 | 13.667 bytes / 37 blocos font-face | 3.772 bytes / 10 blocos: cerca de 72% menos CSS |
| Mesma folha, resposta gzip | 847 bytes | 689 bytes nesta amostra |
| Lateral oculta no HTML do artigo inspecionado | 10.086 bytes / 192 tags de abertura | A condição candidata evita o bloco; HTML compilado precisa de nova importação |
| Posts distintos na reprodução local do HTML público | 10 na rc.3 funcionando | 10 com o script candidato: dois destaques e oito entradas |

As duas respostas de fontes apontavam para os **mesmos dez URLs únicos de arquivos de fontes**. É uma redução da folha CSS, sem comprovação de menos arquivos de fonte baixados. As respostas variam com navegador, cache e provedor. O tamanho da lateral depende dos gadgets salvos; o Blogger pode preservar gadgets de temas anteriores.

O HTML inicial da home tinha 37.049 bytes descomprimidos (resposta gzip de 9.744 bytes); o artigo, 44.477 bytes (gzip de 11.048 bytes). As respostas nativas de CSS e JavaScript de widgets do Blogger tinham 36.892 e 152.070 bytes descomprimidos. Elas dão suporte aos gadgets da plataforma e continuam habilitadas. Páginas adicionais trazem seu próprio HTML; o parser inerte não insere seus estilos/scripts no documento ativo, mas esse HTML ainda consome tráfego.

São observações de bytes/DOM/execução, **não** notas Lighthouse, Core Web Vitals ou prova de melhoria de ranking. Não houve teste com limitação móvel de rede nem comparação de tempo de carregamento antes/depois em produção. O XML otimizado ainda não foi importado; a variante inglesa e todos os gadgets nativos não foram conferidos independentemente no Blogger. [Escopo de validação](VALIDATION.md).

## Manter sua instalação rápida

1. Comece com dez posts nas configurações e mantenha o limite padrão de continuação. Aumentar a meta pode aumentar tráfego. Use `data-page-limit='0'` para desligar a continuação automática e manter os links nativos de posts anteriores. [Configuração da home](HOME.md).
2. No Layout, revise gadgets opcionais da lateral. Uma segunda busca, destaque repetido ou arquivo extenso adiciona HTML às listagens. Remova apenas gadgets que não utiliza. Reimportar o tema não garante remoção dos gadgets salvos.
3. Redimensione/comprima imagens antes do envio; informe dimensões e texto alternativo descritivo. Mantenha carregamento imediato em imagens iniciais do artigo; use carregamento lento nativo nas posteriores e em embeds. Miniaturas decorativas das listagens já têm dimensões e carregamento lento e decodificação assíncrona. [Carregamento de imagens](https://web.dev/articles/browser-level-image-lazy-loading).
4. Evite larguras fixas, excesso de estilos inline e scripts nos posts. Use o [exemplo de postagem](POSTS.md) e a quebra de expansão do Blogger após introduções longas.
5. Para usar somente fontes instaladas no dispositivo, remova os três links Google Fonts do cabeçalho XML. Isso encerra essas requisições externas; as fontes disponíveis variam por dispositivo. Ao hospedar fontes, mantenha os avisos OFL e atualize CSS/URLs. [Licenças das fontes](PROVENANCE.md).
6. Habilite e preencha as descrições de pesquisa do Blogger, inclusive por post. A home e o artigo auditados não tinham `meta name="description"`; o tema usa o cabeçalho nativo em vez de inventar resumos. [Configuração de SEO](SEO.md).

## Conferir no blog publicado

Após importar, teste o primeiro carregamento no celular e em conexão lenta; abra artigo, página fixa, busca e posts anteriores. Confira dez entradas distintas, destino correto da próxima página, navegação sem JavaScript, console sem erros e ausência de transbordamento horizontal. Registre resultados reais no PageSpeed Insights/Search Console antes de afirmar melhoria em Core Web Vitals; recursos iniciais, conteúdo, anúncios, gadgets e o próprio Blogger afetam o resultado.

Desenvolvedores devem rodar `make check` e `make preview` localmente. Quatro checks Node verificam as serializações CDATA e o agendamento com/sem suporte ocioso. `responsive-reading.html` verifica artigo/privacidade/stress; `responsive-home.html` exercita quadros de 320, 360, 768 e 1440px; `short-mobile-links.html`, `short-mixed.html` e `short-missing-blog.html` verificam os novos casos de links/escopo. As fixtures não compilam XML Blogger. O Actions continua desativado e o workflow salvo é apenas manual.
