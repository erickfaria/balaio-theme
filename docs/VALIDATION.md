# Validação — v0.2.0-rc.4

[English](en/VALIDATION.md) · [Português](VALIDATION.md)

## Status

Candidata preparada em 11/10/2026. O proprietário confirmou a importação da v0.1.0 e a continuação da home da rc.3. Nova inspeção da rc.3 mostrou dez posts distintos e console sem erros. A rc.4 otimizada precisa de nova importação no Blogger. Ambos os idiomas, Designer e todos os gadgets nativos ainda não foram conferidos independentemente na plataforma.

**Pausa do Actions:** as execuções de CI registradas abaixo passaram antes da pausa. O Actions do repositório agora está desativado; as validações podem ser executadas localmente e o workflow salvo é apenas manual para retomada futura autorizada.

## Checks automatizados

Vinte e quatro testes locais passam: estrutura XML/gadgets, equivalência de idiomas, metadados nativos/auditoria HTML, resolução/contraste do Designer e navegação/busca móvel. Quatro checks Node verificam sintaxe com CDATA preservado/removido, falha da rc.2 e agendamento adiado (antes de load, execução tardia e sem API ociosa) nos dois idiomas. Sem Node, os quatro são pulados localmente. XMLs, geração inglesa, links Markdown, whitespace e geração da prévia passam. O workflow manual pode repetir checks/pacote somente após retomada autorizada; não houve CI para rc.4. Links externos e âncoras de títulos não são conferidos automaticamente.

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

Importe a candidata num blog de teste; salve cores/fontes no Designer; confira posição de Páginas/Menu, ambos os idiomas, busca, marcadores, listas vazias, miniaturas, paginação e comentários. Confira teclado, zoom a 200% e impressão. Registre o idioma e os resultados antes de promover esta candidata a estável. Core Web Vitals, indexação e posição em buscas/IA não são comprovados por estes checks.

[Checklist de plataforma](ROADMAP.md) · [Auditoria de SEO](SEO.md) · [Atualização e arquivos da versão](RELEASE.md)
