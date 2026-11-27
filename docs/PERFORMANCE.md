# Performance e um tema Blogger limpo

[English](en/PERFORMANCE.md) · [Português](PERFORMANCE.md)

A rc.7 mantém a base da rc.6 e recupera os gadgets e a continuação da rc.3, mantendo o layout pastel, leitura de 22px e Inter/Newsreader abertas. A base não inclui biblioteca JavaScript externa ou carrossel. O Analytics é opcional desde a rc.16 e só é chamado com ID configurado no Blogger. [Configuração](ANALYTICS.md). A importação portuguesa e a continuação da home foram confirmadas pelo proprietário e verificadas no blog público. [Status e evidências](VALIDATION.md).

## Como o tema limita o trabalho

- Uma folha Google Fonts, duas pré-conexões, `display=swap` e alternativas locais. Inter 400–750 e Newsreader 400–700 usam intervalos variáveis. [Google Fonts CSS2](https://developers.google.com/fonts/docs/css2).
- Dois destaques em HTML e lista de continuação com meta de dez posts. Quando a home precisa de mais posts, a continuação espera o HTML inicial e um período ocioso quando disponível, consultando no máximo quatro páginas sequenciais com prioridade baixa. Cada requisição tem timeout de oito segundos; não baixa o arquivo inteiro. [Configuração da home](HOME.md).
- Parsing em template inerte; o tema lê somente o widget Blog1 da resposta e reconstrói as entradas com nós de texto, links e miniaturas. Scripts, eventos e estilos recebidos não são inseridos no documento ativo. A paginação nativa permanece disponível em caso de falha.
- Miniaturas decorativas com dimensões, carregamento lento e decodificação assíncrona. Quando o Blogger oferece dois tamanhos distintos, o navegador escolhe entre 320w e 640w. A URL original continua disponível como alternativa. Artigos sem miniatura continuam legíveis.
- Título por página, canonical e metadados do Blogger, com microdados do conteúdo visível. Sem scripts especiais para rastreadores ou metadados duplicados.
- A seção lateral legada é reservada ao editor de Layout para manter o local dos gadgets durante a migração. Confira o editor e o HTML público após importar o XML.

Compare a home curta e a paginação nativa após importar o tema. Meça o carregamento em uma conexão móvel para avaliar o efeito do agendamento e da prioridade declarada.

## Medições anteriores

Em 11/10/2026, as respostas oficiais de fontes mostraram 13.667 → 3.772 bytes de CSS descomprimido ao solicitar intervalos variáveis. Apontavam para os mesmos dez URLs de arquivos de fontes: é redução da folha CSS, sem comprovação de menos fontes baixadas. Respostas variam com navegador e cache.

O HTML inicial da home rc.3 tinha 37.049 bytes descomprimidos (9.744 em gzip). Um artigo tinha 44.477 bytes (11.048 em gzip), incluindo 10.086 bytes da lateral oculta. Os recursos nativos de CSS/JavaScript de widgets do Blogger tinham 36.892/152.070 bytes descomprimidos e continuam habilitados. Essas observações não são notas Lighthouse, Core Web Vitals ou prova de melhoria de ranking. Não houve comparação de velocidade em produção com a recuperação.

## Manter sua instalação rápida

1. Comece com dez posts nas configurações e mantenha o orçamento padrão de continuação. Defina `data-page-limit='0'` para desligar as requisições adicionais. Metas maiores aumentam tráfego.
2. Confira os gadgets opcionais herdados no editor de Layout após instalar o tema.
3. Redimensione/comprima imagens antes do envio, informe dimensões e texto alternativo. Mantenha imagens iniciais do artigo com carregamento imediato; use carregamento lento nas posteriores. [Imagens no navegador](https://web.dev/articles/browser-level-image-lazy-loading).
4. Evite larguras fixas e excesso de estilos/scripts nos posts. Use o [exemplo de postagem](POSTS.md) e uma quebra de expansão depois de introduções longas.
5. Para fontes do dispositivo, remova os três links Google Fonts do cabeçalho XML. Ao hospedar fontes, preserve seus avisos OFL. [Licenças](PROVENANCE.md).
6. Preencha descrições de pesquisa do blog e de cada post. O tema usa o cabeçalho nativo; ele não inventa resumos. [SEO](SEO.md).

## Conferir no blog publicado

Após importar, confira dois destaques e posts abaixo, paginação correta, artigo, página fixa, busca, celular, ausência de rolagem horizontal e console sem erros. Teste uma conexão lenta e JavaScript desligado. Use resultados reais de PageSpeed Insights/Search Console para avaliar velocidade e indexação; conteúdo, imagens, anúncios, gadgets e a plataforma afetam o resultado.

`make check` valida XML, idiomas, documentação e código. `make preview` gera casos visuais e de continuação, incluindo uma home que começa com apenas dois posts. A prévia não compila o XML no Blogger. O Actions executa checks e gera artefatos identificados pelo commit.

## Menu automático — rc.9

Na rc.9, o menu consulta o feed público resumido uma vez por carregamento, com prioridade baixa e timeout de seis segundos. Revalida o cache HTTP, permitindo respostas condicionais, e não acessa armazenamento de sessão. Isso troca a economia de consultas da rc.8 pela atualização de páginas publicadas/rascunhos ao recarregar. A resposta observada do blog com quatro páginas foi de 6.659 bytes, variando com o conteúdo. Não há biblioteca externa, API key ou polling.

O modo automático acrescenta links por JavaScript; mantenha links essenciais também no gadget nativo para funcionamento sem script e HTML inicial. Use `data-auto-pages='false'` para um menu totalmente manual sem essa consulta. [Modos e limites](PAGES.md).

## Contato opcional — rc.13

O widget nativo é declarado apenas para páginas estáticas, em seção própria. Um marcador no conteúdo ativa sua apresentação por CSS `:has()`, sem detecção de URL, JavaScript adicional, consulta de feed ou biblioteca nova. O markup do formulário também existe, oculto, nas demais páginas estáticas; não é renderizado na home nem nos posts. O envio depende do runtime nativo do Blogger, que o tema não copia nem substitui. [Configuração](CONTACT.md).
