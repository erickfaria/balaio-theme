# Biblioteca e materiais para a web

[English](en/MATERIALS.md) · [Português](MATERIALS.md)

O tema apresenta materiais de referência com HTML e CSS discretos. Não acrescenta scripts, consultas, uma plataforma de Wiki ou um modo de impressão. Inter e Newsreader continuam sob OFL; código e modelos próprios são MIT. Os direitos dos textos e das imagens publicados são definidos por seus autores.

## Organização simples

- **Biblioteca:** uma página com título, resumo e link de cada material, agrupados em apostilas, guias, documentação, estudos e artigos.
- **Apostila:** apresentação e índice de capítulos. Uma apostila inteira também pode permanecer em um único post, preservando seu endereço.
- **Capítulo:** conteúdo e links de índice, anterior e próximo.
- **Documentação:** objetivo, requisitos, instruções e referências. Só acrescente versão e revisão quando forem informações reais.

Adicione a URL da Biblioteca uma vez no gadget Páginas ou em Guias e projetos. Mantenha poucos links no cabeçalho. Se os capítulos forem páginas fixas, o [menu manual](PAGES.md#escolher-somente-algumas-páginas-ou-ordenar-todo-o-menu) evita listar cada capítulo no menu principal.

## Usar no editor do Blogger

Copie o corpo de um modelo para o editor HTML, substitua o texto de exemplo e os links pelos destinos publicados:

- [Biblioteca](../examples/pages/library.pt-BR.html).
- [Apresentação de apostila](../examples/pages/book.pt-BR.html).
- [Capítulo](../examples/pages/chapter.pt-BR.html).
- [Documentação de projeto](../examples/pages/project.pt-BR.html).
- [Guia com índice interno](../examples/pages/guide.pt-BR.html).

O título do Blogger fornece o H1. Os modelos usam H2/H3 no corpo e não incluem tags de widgets, scripts, fotos ou URLs de demonstração externas. Os links internos de exemplo apontam para seções do próprio modelo; substitua-os pelos capítulos quando dividir a leitura em páginas diferentes. O tema não publica páginas nem mantém índices editoriais sozinho.

## Automatizar a partir do Markdown

Um publicador pode gerar os mesmos blocos durante o envio do Markdown ao Blogger. O tema apenas os apresenta. Um cabeçalho portátil de exemplo está em [material.pt-BR.md](../examples/material.pt-BR.md):

```toml
[params.material]
kind = "chapter"
collection = "apostila-jamovi"
order = 10
```

Os tipos sugeridos são `guide`, `documentation`, `study`, `article`, `book`, `chapter` e `library`. Uma apresentação `book` identifica a coleção; seus capítulos recebem ordens únicas. `title` e `description` fornecem os textos dos links e resumos. Versão, data de revisão e licença são opcionais e não devem ser inventadas.

O gerador deve trabalhar com IDs e endereços confirmados, excluir rascunhos e conteúdos futuros e atualizar os índices ao sincronizar. Não deve adivinhar permalinks ou baixar o acervo no navegador do leitor. O intervalo de atualização depende do publicador, não do tema. Os campos extras do TOML são portáveis, mas um tema Hugo precisará interpretá-los para gerar a mesma navegação.

## Contrato HTML pequeno

| Classe | Conteúdo |
| --- | --- |
| `material-meta` | Tipo do material e contexto opcional de versão/revisão. |
| `material-license` | Link opcional com `rel="license"` para a licença do material. |
| `material-library` | Seções H2 e listas de materiais com resumo. |
| `material-index` | Navegação com a lista de capítulos. |
| `collection-nav` | Links para índice, anterior (`rel="prev"`) e próximo (`rel="next"`). |

Sem os estilos, tudo continua legível e navegável. Sem JavaScript, texto e links permanecem no HTML inicial. A estrutura entrega o mesmo conteúdo a pessoas, buscadores e leitores automatizados; não cria texto oculto para IA, um JSON duplicado ou schema de livro sem dados verificados. [SEO e limites da plataforma](SEO.md).

Vídeos podem ser apresentados por um link descritivo comum, carregando o serviço de vídeo somente após o leitor abrir o destino. O tema não transforma automaticamente os vídeos de posts antigos. Comentários e contato continuam dependentes da configuração e dos serviços do Blogger.

## Validação

Confira Biblioteca, capítulo, apostila e documentação na prévia. A suíte verifica destinos de âncoras e ausência de scripts nos modelos. Importação real, visual em dispositivos e saída compilada do Blogger continuam sendo verificações separadas. Esta entrega não altera estilos de impressão nem adiciona recursos de exportação para PDF.
