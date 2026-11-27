# Performance e um tema Blogger limpo

[English](en/PERFORMANCE.md) · [Português](PERFORMANCE.md)

O tema atual usa navegação nativa, fontes abertas Inter e Newsreader e corpo de leitura em 24px. O Blogger chama a integração de Analytics quando existe um ID nas Configurações. [Analytics](ANALYTICS.md) · [Validação](VALIDATION.md).

## Como o tema limita o trabalho

- Uma folha Google Fonts e duas pré-conexões, com `display=swap` e fontes locais de reserva. Inter mantém os pesos 400–750. Newsreader mantém os pesos 400–700 e usa tamanho óptico fixo em 24 para reduzir o WOFF2. [Licenças](PROVENANCE.md).
- Dois destaques em HTML e paginação nativa. Uma home com posts abaixo da meta e link para publicações antigas pode incluir o script de continuação. Ele espera o HTML inicial e consulta até quatro páginas com prioridade baixa por padrão. [Configuração da home](HOME.md).
- Parsing em template inerte; o tema lê somente o widget Blog1 da resposta e reconstrói as entradas com nós de texto, links e miniaturas. Scripts, eventos e estilos recebidos não são inseridos no documento ativo. A paginação nativa permanece disponível em caso de falha.
- Miniaturas decorativas com dimensões, carregamento lento e decodificação assíncrona. Quando o Blogger oferece dois tamanhos distintos, o navegador escolhe entre 320w e 640w. A URL original continua disponível como alternativa. Artigos sem miniatura continuam legíveis.
- Título por página, canonical e metadados do Blogger, com microdados do conteúdo visível. Sem scripts especiais para rastreadores ou metadados duplicados.
- A seção lateral legada é reservada ao editor de Layout para manter o local dos gadgets durante a migração. Confira o editor e o HTML público após importar o XML.

Compare a home curta e a paginação nativa após importar o tema. Meça o carregamento em uma conexão móvel para avaliar o efeito do agendamento e da prioridade declarada.

## Medições anteriores

Em 11/10/2026, as respostas oficiais de fontes mostraram 13.667 → 3.772 bytes de CSS descomprimido ao solicitar intervalos variáveis. Apontavam para os mesmos dez URLs de arquivos de fontes: é redução da folha CSS, sem comprovação de menos fontes baixadas. Respostas variam com navegador e cache.

O HTML inicial da home rc.3 tinha 37.049 bytes descomprimidos (9.744 em gzip). Um artigo tinha 44.477 bytes (11.048 em gzip), incluindo 10.086 bytes da lateral oculta. Os recursos nativos de CSS/JavaScript de widgets do Blogger tinham 36.892/152.070 bytes descomprimidos e continuam habilitados. Essas observações não são notas Lighthouse, Core Web Vitals ou prova de melhoria de ranking. Não houve comparação de velocidade em produção com a recuperação.

## Manter sua instalação rápida

1. Escolha no Blogger quantos posts fazem sentido na home. Use `homePageLimit` com valor 0 no XML para manter apenas a paginação nativa. [Configuração da home](HOME.md).
2. Confira os gadgets opcionais herdados no editor de Layout após instalar o tema.
3. Redimensione/comprima imagens antes do envio, informe dimensões e texto alternativo. Mantenha imagens iniciais do artigo com carregamento imediato; use carregamento lento nas posteriores. [Imagens no navegador](https://web.dev/articles/browser-level-image-lazy-loading).
4. Evite larguras fixas e excesso de estilos/scripts nos posts. Use o [exemplo de postagem](POSTS.md) e uma quebra de expansão depois de introduções longas.
5. Para fontes do dispositivo, remova os três links Google Fonts do cabeçalho XML. Ao hospedar fontes, preserve seus avisos OFL. [Licenças](PROVENANCE.md).
6. Preencha descrições de pesquisa do blog e de cada post. O tema usa o cabeçalho nativo; ele não inventa resumos. [SEO](SEO.md).

## Conferir no blog publicado

Após importar, confira dois destaques e posts abaixo, paginação correta, artigo, página fixa, busca, celular, ausência de rolagem horizontal e console sem erros. Teste uma conexão lenta e JavaScript desligado. Use resultados reais de PageSpeed Insights/Search Console para avaliar velocidade e indexação; conteúdo, imagens, anúncios, gadgets e a plataforma afetam o resultado.

`make check` valida XML, idiomas, documentação e código. `make preview` gera casos visuais e de continuação, incluindo uma home que começa com apenas dois posts. A prévia não compila o XML no Blogger. O Actions executa checks e gera artefatos identificados pelo commit.

## Navegação nativa

Os gadgets Páginas e Menu entregam os links em HTML. O tema dispensa consultas ao feed de páginas. [Configuração do menu](PAGES.md).

## Contato opcional — rc.13

O widget nativo é declarado apenas para páginas estáticas, em seção própria. Um marcador no conteúdo ativa sua apresentação por CSS `:has()`, sem detecção de URL, JavaScript adicional, consulta de feed ou biblioteca nova. O markup do formulário também existe, oculto, nas demais páginas estáticas; não é renderizado na home nem nos posts. O envio depende do runtime nativo do Blogger, que o tema não copia nem substitui. [Configuração](CONTACT.md).
