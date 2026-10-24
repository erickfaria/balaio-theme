# Changelog / Histórico

## Unreleased

- Share menu typography and vertical spacing with Topics on desktop/mobile; remove the separate pill treatment. / Unificar tipografia e espaço vertical do menu e de Assuntos no computador/celular; remover o tratamento de cápsula separada.

- Replace the default topic triangle with a restrained text disclosure and refine chapter-link hierarchy without extra scripts. / Substituir o triângulo padrão de assuntos por um controle discreto e melhorar os links de capítulos sem scripts extras.
- Add a connected three-page project-documentation preview and document documentation collection indexes. / Adicionar prévia conectada de documentação com três páginas e explicar os índices de projetos.

## 0.2.0-rc.14 — web library and reference navigation / biblioteca web e navegação — 2026-10-24

- Add optional web-only material metadata, library lists and chapter navigation styles, with bilingual HTML/Markdown examples and a publisher integration contract. No new scripts, requests, fonts or print features. — reference navigation / navegação de referência

- Optional native curated home links, header topics and long-guide HTML samples, with no additional JavaScript. / Links nativos opcionais de guias na home, assuntos no cabeçalho e modelos HTML de leitura longa, sem JavaScript adicional.
- Native post bylines with optional profile photo and text-only fallback. / Assinatura nativa do post com foto de perfil opcional e alternativa somente com nome.
- Existing scripts and core widget IDs retained; Blogger import and visual browser review remain pending. / Scripts existentes e IDs centrais preservados; importação no Blogger e revisão visual no navegador pendentes.

- Include portable Markdown examples in the install ZIP alongside the bilingual HTML models and license notices. / Incluir exemplos Markdown portáteis no ZIP de instalação junto dos modelos HTML bilíngues e avisos de licença.

## 0.2.0-rc.13 — portable contact page / contato portátil — 2026-10-17

- Include the complete native ContactForm1 in a dedicated section outside the hidden sidebar; limit rendering to static pages.
- Incluir o ContactForm1 completo em seção própria fora da lateral oculta, com renderização restrita a páginas estáticas.
- Enable the form with a simple page-content class, regardless of language, title, domain or numeric URL suffix. No per-blog XML edits, extra JavaScript or new library.
- Ativar por uma classe simples no conteúdo da página, sem depender de idioma, título, domínio ou sufixo numérico. Sem editar o XML por blog, JavaScript extra ou biblioteca nova.
- Ship bilingual ready-to-paste page samples and setup/migration instructions; preserve existing widgets, home continuation and search.
- Distribuir modelos prontos nos dois idiomas e instruções de ativação/atualização; preservar gadgets existentes, continuação da home e busca.
- Add native-contract regressions and non-sending responsive/URL opt-in previews. Fresh Blogger import and inbox delivery remain pending.
- Adicionar regressões do contrato nativo e prévias responsivas/de URL sem envio. Nova importação e entrega no Blogger ainda pendentes.

## 0.2.0-rc.12 — manual contact reference / referência de contato manual — 2026-10-17

- Remove rc.11’s fixed-path ContactForm1 integration and form styles. Blogger may generate a suffixed page URL, so a title is not a reliable way to select the contact page.
- Remover a integração ContactForm1 da rc.11 vinculada a caminhos fixos e seus estilos. O Blogger pode gerar URL com sufixo; o título não determina um endereço fixo de contato.
- Keep only editable Contact text references and English/Portuguese manual setup guides. Document actual page URLs, independently configured forms and removal of the rc.11 gadget if retained on import.
- Manter apenas referências textuais editáveis e guias de configuração manual em português/inglês. Documentar URLs reais, formulários configurados separadamente e remoção do gadget da rc.11 se preservado na importação.
- Restore rc.10 theme XML apart from version metadata; preserve search, page navigation and older-post continuation. Remove obsolete contact runtime tests and form-preview generation.
- Retomar o XML da rc.10, exceto os metadados de versão; preservar busca, navegação e continuação dos posts. Remover testes da integração e geração de prévias de formulário obsoletos.

## 0.2.0-rc.11 — native contact / contato nativo — 2026-10-17

- Include ContactForm1 with original minimal styling and accessible labels/status: optional name, required email/message, no visitor sign-in. Use Blogger’s native delivery without embedded secrets or another service/library.
- Incluir ContactForm1 com visual próprio minimalista, rótulos e status acessíveis: nome opcional, e-mail/mensagem obrigatórios, sem login do visitante. Usar o envio nativo do Blogger, sem segredos no XML ou outro serviço/biblioteca.
- Restrict presentation to `/p/contato.html` and `/p/contact.html`. Include editable page bodies and bilingual one-time setup instructions; XML does not create page records. Existing widget bodies and both scripts remain unchanged.
- Restringir apresentação a `/p/contato.html` e `/p/contact.html`. Incluir corpos de página editáveis e instruções bilíngues de ativação; o XML não cria registros de páginas. Gadgets existentes e ambos os scripts preservados.
- Add non-sending responsive/feedback fixtures and native-contract regression checks. Google transport remains external; fresh rc.11 import and delivery remain pending.
- Adicionar prévias responsivas/retornos sem envio e regressões do contrato nativo. O transporte Google é externo; importação e entrega da rc.11 ainda pendentes.

## 0.2.0-rc.10 — inline search / busca na mesma linha — 2026-10-17

- Open the rounded field to the left of one magnifier, on the same header row. Replace the duplicate search icon with a small submit arrow; retain native keyboard and script-free operation.
- Abrir o campo arredondado à esquerda de uma única lupa, na mesma linha do cabeçalho. Trocar o ícone duplicado por uma seta discreta para enviar; manter teclado e funcionamento nativo sem JavaScript.
- On phones, temporarily hide the title while search occupies that row; closing restores it without shifting the layout. Respect reduced motion. Preserve rc.9 spacing, typography, widgets, page navigation and older-post continuation.
- No celular, ocultar temporariamente o nome enquanto a busca ocupa a linha; fechar o restaura sem deslocar o layout. Respeitar movimento reduzido. Preservar espaços, tipografia, gadgets, navegação de páginas e continuação dos posts da rc.9.
- Update both XML locales and bilingual guides. Fresh rc.10 Blogger import remains pending.
- Atualizar os dois XMLs e guias bilíngues. Nova importação da rc.10 ainda pendente.

## 0.2.0-rc.9 — compact search / busca compacta — 2026-10-17

- Keep only a magnifier beside the title on phones and desktop. A native details/summary disclosure opens the rounded search field by touch or keyboard, including without JavaScript; no new assets or libraries.
- Manter apenas a lupa ao lado do nome no celular e desktop. O controle nativo details/summary abre a busca arredondada por toque ou teclado, inclusive sem JavaScript; sem novos recursos ou bibliotecas.
- Remove Blogger’s extra 30px introduction-widget margin; the gap before posts is 16px on phones / 20px on desktop. Preserve all widget bodies and older-post continuation from imported rc.8.
- Remover a margem extra de 30px do gadget de apresentação do Blogger; o intervalo antes dos posts fica em 16px no celular / 20px no desktop. Preservar todos os gadgets e a continuação dos posts da rc.8 importada.
- Revalidate the summary page feed once per page load instead of using a one-minute session list, reflecting publication, title changes and returns to draft after reload. Manually configured links remain unchanged; no polling.
- Revalidar o feed resumido uma vez por carregamento, em vez da lista de sessão de um minuto, refletindo publicação, mudança de nome e retorno a rascunho ao atualizar. Links manuais continuam sob controle do usuário; sem polling.
- Update bilingual documentation and runtime checks. Fresh rc.9 Blogger import remains pending.
- Atualizar documentação bilíngue e regressões. Nova importação da rc.9 ainda pendente.

## 0.2.0-rc.8 — automatic page navigation / navegação automática — 2026-10-17

- Discover published pages through the same-origin public summary feed; preserve configured link order/labels, deduplicate pages and alphabetize additional links. Cache only titles/URLs for 60 seconds; allow fully manual navigation.
- Descobrir páginas publicadas pelo feed público resumido do próprio blog; preservar ordem/nomes configurados, evitar duplicações e ordenar links adicionais alfabeticamente. Guardar somente títulos/URLs por 60 segundos; permitir navegação totalmente manual.
- Override Blogger’s 30px navbar height, align links with the brand and replace the active green pill with a subtle underline. Keep native widget definitions and working home continuation.
- Corrigir a altura nativa de 30px da navbar, alinhar links com a marca e trocar o destaque verde por sublinhado discreto. Preservar gadgets nativos e continuação da home.
- Add runtime cases for failures, cache, duplicate/unsafe URLs, manual mode and current-page state. rc.8 was subsequently observed installed on October 17; see validation records.
- Adicionar regressões de falha, cache, URLs duplicadas/inseguras, modo manual e página atual. A rc.8 foi posteriormente observada instalada em 17 de outubro; consulte os registros de validação.


## 0.2.0-rc.7 — visual refinement / ajuste visual — 2026-10-12

- Replace the large text search button with an original CSS magnifier in a rounded field. Keep an accessible button label, keyboard focus and a 44px tap target; no icon library or new asset request.
- Substituir o botão grande de busca por uma lupa própria em CSS numa caixa arredondada, com nome acessível, foco de teclado e área de toque de 44px; sem biblioteca de ícones ou nova requisição de recurso.
- Reduce header/menu/introduction/list spacing on desktop and mobile. Preserve rc.6 widget definitions, continuation, pastel palette, open fonts and 22px post/page text.
- Reduzir espaços entre cabeçalho/menu/apresentação/listagem no computador e celular. Preservar gadgets, continuação, paleta pastel, fontes abertas e leitura de 22px da rc.6.


## 0.2.0-rc.6 — main recomendada / recommended main — 2026-10-12

- Owner confirmed successful Portuguese import and requested sidebar removal. Public browser inspection verified two highlights plus eight older posts, ten distinct permalinks and no console errors. rc.6 is the recommended main-branch template; its version number is retained.
- Proprietário confirmou a importação portuguesa e a remoção da lateral. A inspeção pública verificou dois destaques e oito posts antigos, dez permalinks distintos e console sem erros. A rc.6 passa a ser o template recomendado da main; a numeração foi preservada.

- Restore all widget bodies and the home continuation include from owner-confirmed rc.3. Keep two highlights, the older-post list, mobile navigation, 22px reading text and native pagination.
- Restaurar todos os gadgets e o include de continuação da rc.3 confirmada pelo proprietário. Preservar dois destaques, lista de posts antigos, menu móvel, leitura de 22px e paginação nativa.
- Keep the full-width layout, CSS-hidden legacy sidebar, one header search, compact report-abuse footer and open variable fonts. Restore migration keeps complete native widget definitions.
- Manter layout de largura completa, lateral legada oculta por CSS, uma busca no topo, denúncia no rodapé e fontes variáveis abertas. A migração preserva os gadgets completos.
- Enable PR/main/tag/manual CI and downloadable theme artifacts. Add published-HTML checks for registered but missing Header/Blog widgets; local preview success does not establish Blogger import compatibility.
- Ativar CI em PR/main/tag/manual com artefatos do tema. Detectar no HTML publicado gadgets Header/Blog registrados mas ausentes; sucesso da prévia não comprova compatibilidade da importação no Blogger.

## v0.2.0-rc.4 — 2026-10-11

### English

- Prioritize initial content: defer home continuation until load/idle and hint low fetch priority; keep the working rc.3 pagination fallback and ten-post target.
- Request variable-font ranges, reducing the measured Google Fonts CSS from 13,667 to 3,772 decoded bytes while keeping open Inter/Newsreader and the same font file URLs.
- Omit hidden article/static-page sidebar markup; scope fetched cards/pagination to Blog1 and normalize only mobile parameters in appended content links.
- Add lifecycle/runtime regressions, bilingual performance guidance, measured evidence and live rc.3 owner confirmation. Twenty-four local tests pass; optimized rc.4 import and production speed measurements remain pending.

- Temporarily disable repository GitHub Actions at the owner’s request; remove automatic push/PR/tag triggers. Keep a manual workflow for an explicitly approved future resumption and document local validation during the pause. Previously published assets and main protections remain unchanged.

### Português

- Priorizar conteúdo inicial: adiar continuação para load/ociosidade e indicar prioridade baixa; preservar paginação de fallback da rc.3 e meta de dez posts.
- Solicitar intervalos de fontes variáveis, reduzindo CSS Google Fonts medido de 13.667 para 3.772 bytes descomprimidos com Inter/Newsreader abertas e mesmos URLs de arquivos de fontes.
- Evitar HTML da lateral oculta em artigos/páginas; restringir cards/paginação recebidos a Blog1 e normalizar apenas parâmetros móveis em links de conteúdo adicionais.
- Adicionar regressões de ciclo/execução, guia de performance bilíngue, evidências medidas e confirmação da rc.3 pelo proprietário. Vinte e quatro testes locais passam; importação da rc.4 e medições de velocidade em produção seguem pendentes.

- Desativar temporariamente o GitHub Actions do repositório a pedido do proprietário; retirar disparos automáticos por push/PR/tag. Manter o workflow manual para retomada futura explicitamente autorizada e documentar checks locais durante a pausa. Arquivos das versões anteriores e proteções da main permanecem iguais.

## v0.2.0-rc.3 — 2026-10-11

### English

- Fix home continuation failing in the published rc.2: Blogger retained bare CDATA delimiters, causing `Unexpected token '<'` before any extra post request. Comment both delimiters for compatibility with preserved and XML-stripped output.
- Make previews retain the raw script block; add three JavaScript syntax regressions in both locales and Node.js to CI. The previous preview stripped CDATA and missed this production error.
- Reproduce the exact published HTML before/after: two posts and a syntax error become two highlights plus eight unique entries; update bilingual diagnosis, validation scope and install assets. Fresh rc.3 import remains pending.

### Português

- Corrigir a continuação da home na rc.2 publicada: o Blogger preservou delimitadores CDATA sem comentários, causando `Unexpected token '<'` antes de consultar posts extras. Comentar os dois delimitadores para funcionar com a serialização preservada e a extração XML.
- Preservar o bloco de script bruto na prévia; adicionar três regressões de sintaxe JavaScript nos dois idiomas e Node.js ao CI. A prévia anterior removia CDATA e não detectou este erro publicado.
- Reproduzir o HTML publicado antes/depois: dois posts e erro de sintaxe passam a dois destaques e oito entradas únicas; atualizar diagnóstico, escopo da validação e arquivos de instalação bilíngues. Nova importação da rc.3 ainda pendente.

## v0.2.0-rc.2 — 2026-10-11

### English

- Fix a short home page when Blogger returns only two posts despite a larger configured maximum. Keep two highlights and follow native older-page links toward ten posts, with up to four extra requests.
- Append complete pages without duplicate permalinks; advance the older-posts link only after displaying that page. Keep native navigation if JavaScript/network support is unavailable.
- Use original inline MIT JavaScript with no libraries or feed dependency. Rebuild text/link/thumbnail nodes from same-origin page responses without inserting fetched scripts, styles or event handlers.
- Add reproducible preview scenarios for short pages, failures, duplicates, cycles, end of archive and inert content. Document settings and SEO scope in both languages.
- Verify two highlights plus eight list entries using a local copy of the actual public blog responses. Updated XML import still needs validation in Blogger; stable v0.1.0 remains available.

### Português

- Corrigir a home curta quando o Blogger entrega apenas dois posts apesar de um máximo maior. Preservar dois destaques e seguir os links nativos para tentar completar dez posts, com até quatro requisições adicionais.
- Adicionar páginas completas sem repetir permalinks; avançar o link de posts anteriores após exibir a página. Preservar navegação nativa se JavaScript/rede estiverem indisponíveis.
- Usar JavaScript próprio MIT inline, sem bibliotecas nem dependência de feeds. Reconstruir texto, links e miniaturas das respostas do mesmo domínio sem inserir scripts, estilos ou eventos recebidos.
- Adicionar cenários reproduzíveis para páginas curtas, falhas, duplicações, ciclos, fim do arquivo e conteúdo inerte. Documentar ajustes e limites de SEO nos dois idiomas.
- Conferir dois destaques e oito entradas na lista numa cópia local das respostas reais do blog público. A nova importação do XML segue pendente; v0.1.0 estável preservada.

## v0.2.0-rc.1 — 2026-10-11

### English

Release candidate for the next minimal Balaio theme. Twenty local tests and CI pass; a fresh Blogger import and new Designer/widget checks remain pending. Stable v0.1.0 remains available.

- Add translated native color/font controls with the original pastel defaults.
- Set post/page reading text to 22px with a 1.75 line height and explicit H2/H3 sizes; preserve open Inter and Newsreader fonts under SIL OFL.
- Compact mobile header/intro spacing and topics into two columns with 44px minimum link heights; remove the duplicate sidebar divider.
- Add native Pages navigation at the top, retain optional Menu links, enable custom widgets on mobile and fix search URLs containing mobile parameters.
- Remove the visible footer and credits; hide inherited Profile/Attribution widgets and article/page sidebars at all widths.
- Preview three opening cards plus six unique list entries. Document Blogger's post-count setting and jump breaks; the theme cannot force extra posts into Blogger's response.
- Update bilingual installation, migration, customization, validation and release guides. Include clean install assets and SHA-256 checksums.

### Português

Versão candidata do próximo tema minimalista Balaio. Vinte testes locais e CI passam; nova importação e checks dos controles/gadgets no Blogger seguem pendentes. A v0.1.0 estável continua disponível.

- Adicionar controles nativos de cores/fontes traduzidos, com os padrões pastel originais.
- Definir leitura de posts/páginas em 22px e entrelinha de 1,75, com tamanhos explícitos para H2/H3; preservar Inter e Newsreader abertas sob SIL OFL.
- Compactar cabeçalho/apresentação e assuntos em duas colunas no celular, com links de altura mínima de 44px; remover a divisória duplicada.
- Adicionar Páginas no topo, preservar o Menu de links extras, habilitar gadgets no celular e corrigir a busca com parâmetros móveis.
- Remover rodapé/créditos visíveis; ocultar gadgets herdados de Perfil/Atribuição e a lateral de artigos/páginas em todas as larguras.
- Demonstrar três cards e seis entradas únicas na lista. Documentar a quantidade de posts e quebras de expansão do Blogger; o tema não força posts adicionais na resposta da plataforma.
- Atualizar instalação, migração, personalização, validação e release nos dois idiomas. Incluir arquivos limpos de instalação e checksums SHA-256.

## v0.1.0 — 2026-10-11

### English

- Promote Balaio to its first stable release after the project owner confirmed successful Blogger import.
- Keep both theme XML files identical to v0.1.0-alpha.1; this promotion changes version metadata, documentation and validation status.
- Preserve the alpha release and publish a new stable install package, standalone XML assets and SHA-256 checksums.
- Record the confirmed import separately from remaining full widget/runtime checks.

### Português

- Promover o Balaio à primeira versão estável após o proprietário confirmar importação bem-sucedida no Blogger.
- Manter ambos os XMLs idênticos a v0.1.0-alpha.1; a promoção altera versão, documentação e status da validação.
- Preservar a alpha e publicar novo pacote estável, XMLs separados e checksums SHA-256.
- Registrar a importação confirmada separadamente dos checks completos de widgets/execução ainda pendentes.

## v0.1.0-alpha.1 — 2026-10-11

### English

First experimental release of Balaio, an original MIT-licensed minimal Blogger theme.

- Portuguese and English XML templates; three opening cards and a list without repeated posts.
- Editable pastel colors, typography and reading width; responsive articles, pages, figures, tables, code and video containers.
- Header search, configurable menu with current-page indication and optional footer links.
- Blogger-native metadata, article/WebPage microdata and semantic listing headings.
- Lorem ipsum About, Contact and Privacy samples, plus editable post examples.
- Bilingual installation, customization, licensing and SEO guides for Google, Bing, DuckDuckGo, SearXNG and AI discovery.
- Open Inter and Newsreader fonts under SIL OFL 1.1. Original code and examples under MIT.
- Dependency-free validation, thirteen regression tests, HTML SEO audit and CI.
- Install package, standalone XML files and SHA-256 checksums.

**Known limits:** Blogger import and live gadgets remain unverified. Embedded/threaded comments, image logos, Theme Designer controls and a dedicated 404 layout are not implemented. Structured data is partial; dates and high-resolution images need verified native bindings. No indexing, ranking or AI citation guarantees.

### Português

Primeira versão experimental do Balaio, tema Blogger minimalista próprio sob MIT.

- XMLs em português e inglês; três cards de abertura e lista sem posts repetidos.
- Cores pastel, fontes e largura de leitura editáveis; artigos, páginas, figuras, tabelas, código e contêineres de vídeo responsivos.
- Busca no cabeçalho, menu com indicação de página atual e links opcionais no rodapé.
- Metadados nativos, microdados de artigos/WebPage e títulos semânticos nas listagens.
- Modelos de Sobre, Contato e Privacidade com Lorem ipsum e exemplos editáveis de posts.
- Guias bilíngues de instalação, personalização, licenças e SEO para Google, Bing, DuckDuckGo, SearXNG e busca com IA.
- Inter e Newsreader abertas sob SIL OFL 1.1; código e exemplos próprios sob MIT.
- Validadores sem dependências, treze testes, auditor de HTML e CI.
- Pacote de instalação, XMLs separados e checksums SHA-256.

**Limites conhecidos:** importação e gadgets reais no Blogger seguem pendentes. Comentários incorporados/encadeados, logo em imagem, controles no Designer e layout 404 dedicado não estão implementados. O schema é parcial; datas e imagens em alta resolução precisam de campos nativos verificados. Sem garantia de indexação, posição ou citações por IA.
