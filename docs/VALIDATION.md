# Validação — v0.2.0-rc.6

[English](en/VALIDATION.md) · [Português](VALIDATION.md)

## Status

A rc.6 recupera as definições dos gadgets e o script de continuação da rc.3, confirmada pelo proprietário e observada com dez posts no blog em 11/10/2026. Mantém o layout sem lateral, o rodapé compacto, as fontes variáveis abertas, o menu móvel e a leitura de 22px. O proprietário confirmou a importação da rc.6 e a remoção da lateral em 12/10/2026. Ela é a versão recomendada da main.

Actions está ativo para PRs, main, tags e execução manual. Os registros históricos abaixo preservam as condições em que foram feitos.

## Checks automatizados

26 testes locais passaram: estrutura XML/gadgets, idiomas, metadados/auditoria HTML, Designer, contraste, navegação/busca móvel, sintaxe nas duas serializações CDATA e início da continuação numa home com dois posts. O limite zero não faz requisições; o limite padrão consulta o link nativo com a quantidade restante e timeout de oito segundos. Sem Node, os quatro checks JavaScript são pulados localmente; o CI inclui Node. Links Markdown, geração inglesa, XMLs, whitespace e prévia passam.

## Conferência pública — rc.6, 12/10/2026

O proprietário confirmou que a restauração funcionou e que a lateral saiu como desejado. Uma consulta anônima confirmou `balaio-version=0.2.0-rc.6`, Header1/Blog1 renderizados e nenhuma seção `no-items`. O navegador no endereço público exibiu **dois destaques e oito entradas antigas**, dez permalinks distintos, lateral com `display:none` e console sem erros/avisos. A paginação avançou para um trecho de novembro de 2024 depois das entradas mostradas.

Esta evidência confirma a instalação em português e a continuação da home no blog observado. Designer, importação inglesa, todas as configurações de gadgets e métricas de velocidade continuam com seu próprio escopo de validação pendente; não são presumidos a partir desta confirmação.

## Recuperação verificada localmente — rc.6

- Todos os corpos dos gadgets foram recuperados da rc.3. O script fica novamente no include `homeContinuation` de Blog1; não há alterações em conteúdo ou datas dos posts.
- A prévia começa com somente dois posts. Em 320, 360, 768 e 1440px, o navegador exibiu dois destaques e oito entradas distintas abaixo. A paginação avançou para `older-5.html`, após os trechos já mostrados.
- Uma busca por quadro, nenhuma lateral visível e nenhuma rolagem horizontal do documento: larguras cliente/rolagem 305, 345, 753 e 1425px. Console sem erros ou avisos.
- Estes são checks locais do script e CSS. Não executam o compilador ou a restauração dos gadgets do Blogger. A recomendação da rc.6 baseia-se também na conferência pública registrada acima; a numeração rc.6 foi preservada.

## Evidências anteriores da prévia responsiva — v0.2.0-rc.1

- Home com nove posts: três cards e seis entradas distintas em 320, 360, 768, 801, 1050 e 1440px, sem transbordamento horizontal da página.
- Artigo, privacidade e conteúdo longo em 320, 360, 768 e 1440px: leitura de 22px e entrelinha de 38,5px, com conteúdo largo contido.
- Assuntos no celular: os 24 links continuam visíveis, com ao menos 44px de altura e uma única divisória externa. A comparação anterior de espaçamento em 360px reduziu o cabeçalho de 290px para 258px e a lista de 885px para 642px.
- Navegação de Privacidade: um H1, microdados WebPage e indicação de página atual.
- Fixture de Perfil/Atribuição herdados: ocultos em 320, 768 e 1440px; lateral de artigo oculta e nenhum rodapé gerado.

São checks de CSS/DOM em exemplos, não compilação do Blogger nem revisão visual completa por captura de tela. As capturas estavam indisponíveis na revisão anterior; o carregamento remoto das fontes nas fixtures locais não foi confirmado.

## Auditoria do blog publicado

Uma inspeção anterior em 11/10, antes da importação da v0.2.0-rc.1, encontrou CSS anterior, menu superior vazio, dois posts na home e outros pela paginação. A busca móvel acrescentava `search` depois de `?m=1`; a candidata usa `/search`. Foram observadas requisições de fontes Inter/Newsreader e famílias calculadas correspondentes. Um artigo público medido em 360px ainda usava o texto anterior de 18px.

A auditoria corresponde ao tema anterior instalado, não à publicação desta candidata. Nenhum conteúdo ou configuração do blog foi alterado.

## Evidência anterior da continuação — v0.2.0-rc.2

Antes de preparar a rc.2, o blog público em português foi observado usando a v0.2.0-rc.1 em 11/10/2026. As respostas nativas continham apenas dois posts na página inicial apesar do link com `max-results=20`. Uma cópia local dos HTMLs públicos reais, com o novo script, exibiu dois destaques e oito posts adicionais únicos; o link de paginação avançou até o primeiro trecho não exibido. É um check de DOM/execução no navegador, não uma importação do novo XML no Blogger.

Os cenários reproduzíveis de `build_preview.py` conferiram: dez posts únicos a partir de dois; filtragem de duplicações; falha inicial e parcial de rede com preservação do último link de paginação; interrupção de ciclos; links seguintes externos sem requisição; fim do arquivo ocultando a navegação; scripts/eventos recebidos inertes; modo sem script e carregamento desligado; orçamento de uma página respeitado; meta atingida sem cortar a última página. O código não insere o HTML recebido no documento ativo.

A prévia `responsive-home.html` foi conferida em quadros locais de 320, 360, 768 e 1440px: dois destaques e oito entradas, sem transbordamento horizontal do documento interno. O cliente medido desconta 15px da barra vertical (305, 345, 753 e 1425px). Os ajustes de viewport da ferramenta não funcionaram; os quadros aplicaram dimensões reais. Capturas estavam indisponíveis, portanto é uma revisão de CSS/DOM, sem nova inspeção por imagem. Os checks anteriores acima correspondem à v0.2.0-rc.1; confira também o celular real após importar. Metadados e paginação nativos permanecem; não há garantia de indexação das entradas extras por JavaScript na home.

## Correção do HTML publicado — v0.2.0-rc.3

A nova inspeção do blog em 11/10/2026 confirmou a rc.2 publicada, dois posts iniciais, lista vazia e link nativo com `max-results=50`. O console acusou `SyntaxError: Unexpected token '<'`: o Blogger publicou os delimitadores CDATA literalmente dentro do script. A próxima página consultada respondeu HTTP 200 sem redirecionar. Datas antigas não impediram o acesso aos posts seguintes.

Uma reprodução local manteve o HTML público completo, inclusive seus delimitadores, mudando apenas o domínio para atender as requisições na cópia local. A forma original repetiu os dois posts e o mesmo erro. Ao adicionar somente `//` aos dois delimitadores, o navegador mostrou dez permalinks distintos: dois destaques e oito entradas abaixo, começando por “Como usar R no Jamovi?”. A paginação avançou além do último post exibido e o console dessa cópia corrigida ficou sem erros/avisos. As páginas seguintes foram consultadas no blog real; redirecionamentos não foram seguidos silenciosamente pelo servidor de teste.

`build_preview.py` agora preserva o bloco de script bruto em vez de extrair seu texto via parser XML. A prévia atual, com `//<![CDATA[` presente no HTML, também exibiu 2 + 8 posts em quadros de 320, 360, 768 e 1440px, com larguras de cliente/rolagem iguais (305, 345, 753 e 1425px). Isto verifica DOM, execução e largura; não equivale à importação da rc.3 nem a uma nova revisão por captura de tela. As observações anteriores da rc.2 não comprovavam compatibilidade com a serialização do Blogger.

## Candidata de performance — v0.2.0-rc.4

- CSS oficial das fontes: 13.667 → 3.772 bytes descomprimidos; as duas respostas apontaram para os mesmos dez URLs de arquivos de fontes. Os intervalos cobrem os pesos intermediários da interface.
- O artigo rc.3 inspecionado continha lateral oculta de 10.086 bytes (192 tags de abertura). O XML candidato condiciona a seção para item/static_page; a redução compilada precisa de nova importação.
- Reprodução local do HTML rc.3 com script candidato: dois destaques e oito entradas distintas, links adicionais sem `m`, próxima página correta e console sem erros/avisos.
- Fixtures regeneradas preservam sucesso, duplicações, ciclos, falha inicial/parcial, rejeição de URL externo, fim do arquivo, conteúdo inerte, sem script/desligado, limite de uma página e última página completa. Novos casos preservam outros parâmetros/fragmentos, ignoram cards/paginação fora de `Blog1` e mantêm navegação se `Blog1` estiver ausente.
- Quadros de home em 320, 360, 768 e 1440px mostraram dez entradas distintas; larguras de cliente/rolagem coincidiram em 305, 345, 753 e 1425px. Artigo/privacidade/stress mantêm texto de 22px e entrelinha de 38,5px sem transbordamento da página.
- Auditorias da home rc.3 e de um artigo publicado encontraram um título/canonical/H1, idioma português e nenhum erro estrutural. Ambos estavam sem descrição de pesquisa; configure-a nas Configurações/editor do Blogger. Conteúdo/configurações não foram alterados.

São checks locais de execução/DOM e bytes; não houve Lighthouse, Core Web Vitals, rede limitada ou comparação de velocidade em produção. [Evidências e ajustes de performance](PERFORMANCE.md).

## Checks de plataforma pendentes

A importação portuguesa e a home da rc.6 foram confirmadas. Num blog de teste, salve cores/fontes no Designer; confira posição de Páginas/Menu, ambos os idiomas, busca, marcadores, listas vazias, miniaturas, paginação e comentários. Confira teclado, zoom a 200% e impressão. Registre o idioma e os resultados antes de promover esta candidata a estável. Core Web Vitals, indexação e posição em buscas/IA não são comprovados por estes checks.

[Checklist de plataforma](ROADMAP.md) · [Auditoria de SEO](SEO.md) · [Atualização e arquivos da versão](RELEASE.md)

## Layout sem lateral — desenvolvimento

24 testes locais passaram. A prévia da home foi conferida a 320, 360, 768 e 1440px: 10 cards únicos, uma busca, nenhuma lateral e link de denúncia no rodapé. Sem rolagem horizontal nesses quadros. Nova importação real no Blogger continua pendente.

## Falha real após restauração — 12 de outubro de 2026

O proprietário confirmou restauração das duas candidatas do PR #14, mas a página continuou vazia.
Inspeção pública confirmou seções `header`, `navigation`, `introduction`, `main` e `sidebar`
com `no-items`, sem elementos Header1/Blog1, embora os gadgets fossem registrados pelo JavaScript.
O feed público continua com 144 posts. A falha ocorre na renderização de gadgets, não na remoção de posts.
A comparação local não confirma o conteúdo efetivamente salvo pelo Blogger: é necessário analisar
o backup XML exportado após restaurar. A causa permanece aberta e não houve merge dessas candidatas.

`audit_seo.py` agora trata como erro um Header/Blog registrado sem elemento correspondente no HTML.
Os checks de XML, traduções e prévia não compilam nem executam a migração do Blogger;
CI aprovado não implica que a importação ou renderização real esteja aprovada.

O backup enviado pelo proprietário confirmou que todos os includables próprios foram preservados; os atributos `visible` foram descartados pelo Blogger. As tentativas de preservar IDs e definir visibilidade não corrigiram a página. A tentativa rc.5 separou o JavaScript do gadget Blog1. O proprietário depois informou que a página apareceu, mas continuou só com dois posts. A consulta pública anônima ainda respondeu com seções vazias na rc.5, portanto o resultado publicado permanece sem reconciliação. A rc.6 recuperou a base rc.3 e depois teve a instalação confirmada, conforme o registro público acima.
