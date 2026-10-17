# Performance e um tema Blogger limpo

[English](en/PERFORMANCE.md) · [Português](PERFORMANCE.md)

A rc.7 mantém a base da rc.6 e recupera os gadgets e a continuação da rc.3, mantendo o layout pastel, leitura de 22px e Inter/Newsreader abertas. Não há biblioteca JavaScript externa, analytics ou carrossel. A importação portuguesa e a continuação da home foram confirmadas pelo proprietário e verificadas no blog público. [Status e evidências](VALIDATION.md).

## Como o tema limita o trabalho

- Uma folha Google Fonts, duas pré-conexões, `display=swap` e alternativas locais. Inter 400–750 e Newsreader 400–700 usam intervalos variáveis. [Google Fonts CSS2](https://developers.google.com/fonts/docs/css2).
- Dois destaques em HTML e lista de continuação com meta de dez posts. O script recuperado inicia dentro de Blog1, depois do HTML dos posts, consultando no máximo quatro páginas sequenciais. Cada requisição tem timeout de oito segundos; não baixa o arquivo inteiro. [Configuração da home](HOME.md).
- Parsing em template inerte; as entradas são reconstruídas com nós de texto, links e miniaturas. Scripts, eventos e estilos recebidos não são inseridos no documento ativo. A paginação nativa permanece disponível em caso de falha.
- Miniaturas decorativas com dimensões, carregamento lento e decodificação assíncrona. Artigos sem miniatura continuam legíveis.
- Título, canonical e metadados nativos, com microdados do conteúdo visível. Sem scripts especiais para rastreadores ou metadados duplicados.
- Lateral legada oculta por CSS para preservar a estrutura importável. Isso não elimina seu HTML: remova no Layout gadgets opcionais que não usa, como busca duplicada, arquivo por data ou destaque repetido. Os gadgets centrais de Cabeçalho, Páginas, Menu e Postagens são necessários.

As otimizações experimentais da rc.4 — agendamento após load/ociosidade, prioridade baixa, escopo Blog1 e limpeza dos parâmetros móveis — não fazem parte do script recuperado. A prioridade desta candidata é recuperar o comportamento confirmado; futuras mudanças precisam preservar a lista de posts em testes de importação reais.

## Medições anteriores

Em 11/10/2026, as respostas oficiais de fontes mostraram 13.667 → 3.772 bytes de CSS descomprimido ao solicitar intervalos variáveis. Apontavam para os mesmos dez URLs de arquivos de fontes: é redução da folha CSS, sem comprovação de menos fontes baixadas. Respostas variam com navegador e cache.

O HTML inicial da home rc.3 tinha 37.049 bytes descomprimidos (9.744 em gzip). Um artigo tinha 44.477 bytes (11.048 em gzip), incluindo 10.086 bytes da lateral oculta. Os recursos nativos de CSS/JavaScript de widgets do Blogger tinham 36.892/152.070 bytes descomprimidos e continuam habilitados. Essas observações não são notas Lighthouse, Core Web Vitals ou prova de melhoria de ranking. Não houve comparação de velocidade em produção com a recuperação.

## Manter sua instalação rápida

1. Comece com dez posts nas configurações e mantenha o orçamento padrão de continuação. Defina `data-page-limit='0'` para desligar as requisições adicionais. Metas maiores aumentam tráfego.
2. Revise no Layout os gadgets opcionais herdados. O Blogger pode preservá-los ao instalar um tema.
3. Redimensione/comprima imagens antes do envio, informe dimensões e texto alternativo. Mantenha imagens iniciais do artigo com carregamento imediato; use carregamento lento nas posteriores. [Imagens no navegador](https://web.dev/articles/browser-level-image-lazy-loading).
4. Evite larguras fixas e excesso de estilos/scripts nos posts. Use o [exemplo de postagem](POSTS.md) e uma quebra de expansão depois de introduções longas.
5. Para fontes do dispositivo, remova os três links Google Fonts do cabeçalho XML. Ao hospedar fontes, preserve seus avisos OFL. [Licenças](PROVENANCE.md).
6. Preencha descrições de pesquisa do blog e de cada post. O tema usa o cabeçalho nativo; ele não inventa resumos. [SEO](SEO.md).

## Conferir no blog publicado

Após importar, confira dois destaques e posts abaixo, paginação correta, artigo, página fixa, busca, celular, ausência de rolagem horizontal e console sem erros. Teste uma conexão lenta e JavaScript desligado. Use resultados reais de PageSpeed Insights/Search Console para avaliar velocidade e indexação; conteúdo, imagens, anúncios, gadgets e a plataforma afetam o resultado.

`make check` valida XML, idiomas, documentação e código. `make preview` gera casos visuais e de continuação, incluindo uma home que começa com apenas dois posts. A prévia não compila o XML no Blogger. O Actions executa checks e gera artefatos identificados pelo commit.

## Menu automático — rc.8

O menu consulta o feed público resumido de páginas, uma vez por carregamento sem cache, com prioridade baixa e timeout de seis segundos. Guarda somente títulos/URLs por 60 segundos na sessão; sem armazenamento disponível, continua funcionando pela rede. A resposta observada do blog com quatro páginas foi de 6.659 bytes, variando com o conteúdo. Não há biblioteca externa, API key ou polling.

O modo automático acrescenta links por JavaScript; mantenha links essenciais também no gadget nativo para funcionamento sem script e HTML inicial. Use `data-auto-pages='false'` para um menu totalmente manual sem essa consulta. [Modos e limites](PAGES.md).
