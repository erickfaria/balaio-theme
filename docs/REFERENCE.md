# Guias, projetos e conteúdo de referência

[English](en/REFERENCE.md) · [Português](REFERENCE.md)

A rc.15 é a versão atual da main. Assuntos usa a mesma tipografia e o mesmo alinhamento do menu, sem contagens ou marcador visual. Os checks locais não substituem uma importação e conferência visual no Blogger.

## Uma pequena biblioteca dentro do blog

Um conteúdo pilar pode continuar sendo um post: destaque sua URL em vez de mudar o endereço ou duplicar o texto. A apostila, a documentação e os tutoriais continuam com os títulos, links e metadados nativos. Páginas estáticas também usam a mesma coluna de leitura. O tema não cria nem publica páginas ou muda conteúdo.

A composição proposta tem três entradas:

- **Páginas:** links institucionais no menu existente; Sobre, Contato e Privacidade são exemplos.
- **Assuntos:** o gadget nativo de marcadores abre uma lista recolhível no cabeçalho, por toque ou teclado. Não há biblioteca ou consulta extra para listar categorias.
- **Guias e projetos:** uma faixa pequena na home, depois da apresentação, com uma seleção editorial de conteúdos duradouros.

## Destacar uma apostila ou um projeto

Em **Layout → Guias e projetos → Editar**, adicione o título e a URL real de até três conteúdos importantes. É uma Lista de links nativa (`LinkList2`), aceitando posts, páginas e destinos externos. Sem links, a faixa não aparece nem reserva espaço visual. Não há links de demonstração no XML distribuído.

A seleção é manual: não transforma toda postagem com uma categoria em destaque e não depende de data recente. Use títulos curtos e específicos, como o nome da apostila ou do projeto. Não é preciso editar código para trocar os itens.

Se houver muitos conteúdos, crie uma página **Biblioteca** com seções e links reais para os capítulos e adicione essa página à faixa. A home apresenta poucos caminhos; o índice reúne os detalhes. Conteúdo público e documentação continuam no seu blog, sem um motor de Wiki adicional.

## Páginas e categorias no cabeçalho

**Layout → Páginas** mantém os links principais. **Menu** continua disponível para links extras. A descoberta automática de páginas permanece como antes; se você publicar muitos capítulos estáticos, considere o [modo manual do menu](PAGES.md#escolher-somente-algumas-páginas-ou-ordenar-todo-o-menu) para selecionar somente as entradas principais. Não há novo limite silencioso de páginas.

**Layout → Assuntos** configura o mesmo `Label1` que existia na área lateral antiga, preservando o ID do gadget. Escolha cinco a sete marcadores principais e um título curto. As contagens não são exibidas. Siga a [configuração curta do Layout](LAYOUT.md). O marcador do Blogger funciona como categoria; o tema não cria nem reorganiza seus rótulos. A seção lateral antiga continua reservada para compatibilidade, oculta.

## Estruturar uma leitura longa

Copie o [modelo de guia](../examples/pages/guide.pt-BR.html) para o corpo de um post ou página no editor HTML. O título do Blogger fornece o H1; use H2/H3 no corpo. O índice usa `details/summary`, links e IDs escritos no conteúdo. Funciona sem JavaScript e fica recolhido inicialmente. Atualize os links quando adicionar seções.

O tema também aplica esse tratamento discreto a índices existentes com `class="post-toc"`. Não percorre o artigo para inventar um índice automaticamente. Texto, títulos, código e tabelas mantêm a largura de leitura existente; não há painel lateral permanente nem navegação fixa cobrindo o texto.

A importância de um conteúdo vem da seleção editorial e dos links descritivos. A faixa não cria schema de artigo adicional, não duplica H1 e não implica ganho garantido de posição nas buscas. Links configurados nos gadgets são entregues no HTML inicial; a descoberta automática de páginas mantém sua dependência anterior de JavaScript.

## Autoria discreta

Nos posts, a assinatura passa a mostrar **Escrito por**, nome e, quando fornecidos pelo Blogger, link do perfil e foto pública de 32 × 32 px com recorte circular por CSS. A imagem mantém largura/altura reservadas, carregamento lento e decodificação assíncrona. A miniatura é decorativa para leitores de tela porque o nome está ao lado.

O nome e os microdados `Person` permanecem sem foto ou URL de perfil. A assinatura usa os dados de cada postagem, respeitando blogs com vários autores; não aplica uma foto global em todos os textos. Não adiciona JavaScript, chamadas à API ou pesquisa de perfil. A exibição de `post.authorPhoto.url` e `post.authorProfileUrl` depende dos dados expostos pelo Blog1 na instalação; confira num post após importar. Páginas estáticas e listas de cards mantêm o tratamento anterior de autoria.

Confira a foto pública no perfil do autor caso ela não apareça. Sem uma foto exposta pelo Blogger, o resultado previsto é somente o nome, sem avatar genérico imposto pelo tema.

## Peso e validação da rc.15

Comparação com a rc.14: CSS de **17.566 → 18.200 bytes**; gzip isolado de **4.184 → 4.279 bytes** (95 bytes a mais). São medidas dos arquivos locais. não uma medição de velocidade ou de HTML publicado. Os dois scripts permanecem idênticos: **9.295 bytes**. sem JavaScript adicional. Nenhuma biblioteca. fonte ou serviço foi incluído.

**36 testes locais passaram**, incluindo continuidade da home, menu automático, estrutura dos gadgets, traduções, autoria opcional e destinos do índice. O gerador inclui home com e sem destaques, ausência de assuntos/foto, nome longo, guia em português/inglês e quadros de 320, 360, 768 e 1440 px. O avatar de demonstração é um SVG original gerado só na prévia, não uma foto de pessoa.

O navegador de revisão não estava disponível nesta sessão; responsividade visual e importação real permanecem pendentes. A prévia é uma fixture, não um compilador de expressões do Blogger. Não trate esses checks como confirmação de restauração ou exibição dos dados de perfil em produção.

## Biblioteca e publicação por Markdown

Veja os [modelos web e o contrato de automação](MATERIALS.md) para Biblioteca, apostilas, capítulos e documentação. O publicador pode montar os índices durante o envio; o tema não acrescenta consultas no navegador.
