# Validação — v0.2.0-rc.15

[English](en/VALIDATION.md) · [Português](VALIDATION.md)

## rc.15 — Cabeçalho uniforme e curadoria — 24/10/2026

Assuntos e links do menu usam a mesma fonte, tamanho, peso, entrelinha, alvo de toque e espaço vertical. Sem cápsula, borda, fundo destacado, seta ou contagens. Os gadgets, scripts e o modo automático atual foram preservados. A configuração de cinco a sete categorias, poucos links no topo e até três destaques fica documentada no [Layout](LAYOUT.md), sem escolhas impostas ou corte silencioso.

36 testes locais passam. XML, traduções, links, pacote e prévia passam. O CSS acrescenta 634 bytes (95 em gzip isolado) contra a rc.14; os scripts permanecem idênticos. Os links da prévia conectada de documentação foram conferidos. A ausência de navegador nesta sessão mantém a avaliação visual da rc.15 pendente.

O proprietário relatou a instalação da rc.14, e a consulta pública confirmou o marcador dessa versão e o controle Assuntos. Isso não confirma a instalação da rc.15 nem todos os dados de perfil.

## rc.14 — Biblioteca web e navegação — 24/10/2026

A versão da main inclui links editoriais opcionais, assuntos nativos no cabeçalho, assinatura com foto opcional e modelos web de Biblioteca/apostila/capítulos. **36 testes locais passaram**, incluindo completude do pacote. Idiomas, XML, links da documentação e prévia passam; o Actions repete os checks antes da integração e na main/tag.

Os dois scripts permanecem idênticos à rc.13. CSS: 14.724 → 17.566 bytes; gzip isolado: 3.704 → 4.184 bytes. Sem novas fontes, serviços ou recursos de impressão. O pacote inclui os modelos Markdown referenciados pelos guias. São medidas de arquivos, não resultados de velocidade publicados.

Nova importação no Blogger, foto exposta pelo perfil e revisão visual em dispositivos permanecem pendentes. A release rc.14 é uma candidata, sem promover esses testes locais a confirmação da plataforma.

## Status anterior — rc.13

A rc.13 inclui o formulário nativo em seção própria, fora da lateral oculta. Uma classe no conteúdo da página estática ativa sua apresentação por CSS, com qualquer nome/endereço. Não há detecção por URL, novo JavaScript ou criação automática de páginas. Importação e entrega desta candidata ainda precisam de confirmação no Blogger.

A rc.6 recupera as definições dos gadgets e o script de continuação da rc.3, confirmada pelo proprietário e observada com dez posts no blog em 11/10/2026. Mantém o layout sem lateral, o rodapé compacto, as fontes variáveis abertas, o menu móvel e a leitura de 22px. O proprietário confirmou a importação da rc.6 e a remoção da lateral em 12/10/2026. Ela é a base validada da rc.7.

Actions está ativo para PRs, main, tags e execução manual. Os registros históricos abaixo preservam as condições em que foram feitos.

## Contato por conteúdo — rc.13, 17/10/2026

A cópia exportada pelo proprietário continha ContactForm1 na lateral oculta e com condição de URL antiga. A rc.13 declara o gadget completo na seção contactpage, fora de sidebar, com escopo de páginas estáticas. O modelo HTML acrescenta a classe balaio-contact-page; não é mais necessário editar linhas do XML ou fixar um endereço. Os gadgets anteriores e os dois scripts foram preservados. As prévias desativam envio e não carregam o transporte Google. 31 testes locais passaram, além de links da documentação, geração de idiomas, XML e whitespace. Os seis gadgets anteriores e os scripts home-continuation/page-navigation foram comparados à main anterior, sem diferenças.

As prévias dos dois idiomas foram conferidas em 320, 360, 768 e 1440px: um H1, campos de 16px, controles acima de 44px, alinhamento com a coluna de leitura, intervalo de 24px após o texto e nenhuma rolagem horizontal. Três URLs diferentes (duas com sufixo numérico) exibiram o formulário; Sobre, Privacidade e a página sem classe o mantiveram oculto. O aviso sem JavaScript apareceu no quadro isolado. E-mail inválido foi reconhecido; dados fictícios com nome vazio foram aceitos pela validação HTML. Retornos de erro/sucesso são apenas estados ilustrativos, sem mensagem enviada.

Nenhum conteúdo, configuração ou mensagem foi enviado ao Blogger. Os checks locais não executam o compilador/migração da plataforma nem confirmam entrega de e-mail. A nova importação e o recebimento real continuam pendentes.

## Contato manual e remoção da integração — rc.12, 17/10/2026

O proprietário informou que o Blogger criou uma página com sufixo numérico. A condição da rc.11 aceitava apenas dois caminhos fixos, portanto não cobria esse endereço. A pedido do proprietário, removemos a integração, em vez de acrescentar outras regras de detecção.

Os dois XMLs foram comparados ao commit rc.10: após normalizar somente a versão, são idênticos. Todos os gadgets, CSS, marcação e scripts da base são preservados. Os geradores de idioma e prévia também retomaram a rc.10; o teste de contrato e as prévias de formulário da integração removida foram excluídos.

28 testes locais passaram, com documentação bilíngue, XML, idiomas e scripts validados. A prévia de Contato agora contém apenas o texto de referência, sem controles de envio. Os guias orientam a usar a URL real gerada, inclusive com sufixo, configurar um formulário separadamente e remover o gadget da rc.11 no Layout caso o Blogger o preserve. O XML não modifica textos de páginas já publicadas. [Referência e migração](CONTACT.md).

Não houve alteração de conteúdo/configurações no Blogger nem envio de mensagens. A rc.12 retoma o código já importado da rc.10; não é uma nova conferência de importação pelo compilador do Blogger.

## Contato nativo — rc.11, 17/10/2026

30 testes locais passaram, incluindo regressões para os seis IDs que o runtime nativo usa, rótulos associados aos campos, nome opcional, e-mail/mensagem obrigatórios, retornos acessíveis e escopo da página. O contrato foi conferido lendo o recurso público de widgets do Blogger; a biblioteca não foi copiada ao repositório.

As páginas públicas da rc.10 confirmaram os campos `canonicalUrl` e `canonicalHomepageUrl`. No modo móvel, `homepageUrl` inclui `?m=1`, enquanto as duas URLs canônicas ficam limpas. O novo widget compara as URLs canônicas, preservando a seleção da página no celular e sem fixar o domínio.

A prévia usa o formulário real de cada XML, com Enviar desativado e sem transporte Google. Em 320, 360, 768 e 1440px, nos dois idiomas, os campos ficaram contidos, com um H1, três rótulos associados, fontes Inter de 16px e botões acima de 44px. Larguras cliente/rolagem coincidiram (305, 345, 753 e 1425px). O intervalo entre introdução e formulário foi 24px, com um único link de retorno visível. Capturas locais foram inspecionadas.

A validade HTML rejeitou e-mail malformado e campos obrigatórios vazios; aceitou os dados fictícios com nome vazio. Os exemplos de erro/sucesso foram conferidos como **estados ilustrativos**, sem afirmar entrega. Nenhuma mensagem ou dado do usuário foi enviado. Layout, recepção de e-mail, modo móvel, idioma das mensagens nativas e ausência do formulário em outras páginas devem ser conferidos após importar. [Ativação](CONTACT.md).

## Busca à esquerda — rc.10, 17/10/2026

A prévia usa o formulário e CSS reais do tema. Em 320, 360, 768 e 1440px, o campo aberto ficou à esquerda da lupa com a mesma coordenada vertical, separado por 6px. Há um único elemento de lupa. A altura do cabeçalho não mudou entre abrir e fechar, sem rolagem horizontal; a home manteve dois destaques e oito entradas abaixo.

No modo móvel, o nome fica oculto enquanto a busca ocupa a linha e reaparece ao fechar, mantendo as dimensões do cabeçalho. Enter abriu e Espaço fechou o controle nativo. Tab alcançou o campo; a seta enviou `ciência dados` por GET, por clique no desktop e teclado num quadro sem JavaScript. Foram inspecionadas capturas locais. A transição CSS tem duração de 160ms e é desativada pela preferência por movimento reduzido.

28 testes locais passaram. Os corpos de todos os gadgets e os dois scripts foram comparados à rc.9 sem diferenças. Esses checks de prévia não confirmam uma importação da rc.10 no Blogger.

## Busca recolhível e atualização do menu — rc.9, 17/10/2026

A página pública foi observada com a rc.8 instalada e gadgets preenchidos. Seu menu nativo tinha apenas Início. O feed público passou a conter somente Privacidade e Sobre; Membros retornou HTTP 404 após voltar a rascunho. Uma nova abertura mostrou os três links corretos. A lista anterior podia persistir por um minuto no cache de sessão da rc.8.

A rc.9 elimina essa lista: uma consulta de baixa prioridade ao feed resumido, timeout de seis segundos e revalidação HTTP por carregamento. As regressões executam o script real nos dois idiomas e confirmam publicação, alteração de título, retorno a rascunho, lista vazia, falha de rede e ausência de acesso a sessionStorage. Links manuais e os gadgets permanecem preservados.

28 testes locais passaram. A prévia usa o controle details/summary e o formulário reais do XML, além de reproduzir margens nativas do Blogger. A busca abriu por toque/clique e Enter, enviou termos com acentos por GET e continuou sem JavaScript em quadro isolado. Foram conferidas larguras de 320, 360, 768 e 1440px: lupa de 44px ao lado do nome, campo aberto contido, dois destaques e oito entradas, sem transbordamento horizontal. O intervalo entre a descrição da apresentação e Últimas publicações é 16px no celular e 20px no desktop, sem a margem extra de 30px do gadget. Capturas locais foram inspecionadas.

Estes checks não compilam o XML no Blogger nem confirmam uma nova importação da rc.9. Todos os corpos de gadgets e a continuação foram comparados à main rc.8, sem diferenças.

## Checks automatizados

28 testes locais passaram: estrutura XML/gadgets, idiomas, metadados/auditoria HTML, Designer, contraste, navegação/busca móvel, sintaxe nas duas serializações CDATA e início da continuação numa home com dois posts. O limite zero não faz requisições; o limite padrão consulta o link nativo com a quantidade restante e timeout de oito segundos. Sem Node, os seis checks JavaScript são pulados localmente; o CI inclui Node. Links Markdown, geração inglesa, XMLs, whitespace e prévia passam.

## Páginas automáticas e alinhamento — rc.8, 17/10/2026

A inspeção pública encontrou rc.7 com quatro páginas publicadas no sitemap, mas só Início na lista nativa de PageList1. Os quatro URLs responderam HTTP 200 com título e layout WebPage. A altura calculada da seção navbar era 30px, enquanto o link tinha 44px e passava da borda do cabeçalho.

O feed público resumido retornou as quatro páginas e 6.659 bytes na resposta observada, contra 17.308 bytes do feed completo; tamanhos variam conforme o conteúdo. O menu usa o resumido, uma consulta por carregamento sem cache, timeout de seis segundos e cache de títulos/URLs na sessão por um minuto. Não depende de API key nem de domínios fixos.

28 testes locais passaram, incluindo as duas serializações CDATA nos dois idiomas e cenários de cache válido/expirado, falta de armazenamento, modo manual, feed inválido/indisponível, duplicações, URLs externas/inseguras e item atual.

A prévia reproduz o CSS nativo `.navbar{height:30px}`. Em 320/360/768/1440px, uma reprodução local dos títulos/caminhos públicos mostrou os cinco links (Início e quatro páginas), alinhados com a marca e dentro do cabeçalho, sem fundo verde nem rolagem horizontal. A seção cresceu para 94px nas duas larguras menores e 44px nas maiores. Os dez posts continuaram carregando. A revisão visual por captura confirmou o alinhamento no computador.

Falhas de feed, JSON inválido e lista vazia preservaram Início; modo manual preservou apenas a lista configurada; um link Sobre existente manteve o nome personalizado sem duplicação; o caso de conteúdo malicioso criou texto literal, não imagens/eventos. A página Privacidade recebeu `aria-current='page'`. São verificações locais de código/DOM e uma leitura pública do feed, não uma importação da rc.8 no Blogger.

## Ajuste visual local — rc.7

26 checks passaram. Em quadros de 320, 360, 768 e 1440px, a prévia continua com dois destaques e oito entradas distintas, paginação correta e nenhuma rolagem horizontal. O botão tem nome acessível, foco de teclado, alvo de 44×44px e lupa própria em CSS, sem requisição de ícone. A busca de “ciência dados” enviou o parâmetro `q` corretamente.

No exemplo de 360px com seis links no menu, o título das publicações subiu de 583 para 488px; em 1440px, de 521 para 405px. São medidas da prévia com as mesmas fontes e conteúdo, não da nova versão publicada. Console sem erros/avisos. A importação portuguesa comprovada abaixo corresponde à rc.6.

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
