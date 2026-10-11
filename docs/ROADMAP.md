# Plano de desenvolvimento

[English](en/ROADMAP.md) · [Português](ROADMAP.md)

## Base entregue

XMLs estáveis v0.1.0, home com lista editorial, artigos, páginas, busca, marcadores, paginação, comentários básicos, gadgets e CSS responsivo. Na home, os três primeiros posts são cards de abertura; os demais ficam na lista, sem duplicação. Busca e arquivos preservam a listagem comum. O proprietário confirmou a importação. A saída de miniaturas/resumos, idioma e comportamento com lista vazia ainda precisam de checks específicos em execução.

## Próxima etapa: validar no Blogger

- [x] Importação bem-sucedida confirmada pelo proprietário.
- [ ] Registrar o idioma importado e testar explicitamente as duas variantes.
- [ ] Conferir home com zero, um e vários posts; títulos ausentes e posts sem imagem.
- [ ] Conferir busca com e sem resultados, marcadores e arquivos por data.
- [ ] Conferir links de paginação em um blog com mais posts que o limite da home.
- [ ] Conferir artigos longos, páginas estáticas, imagens, legendas, listas, tabelas, código e vídeos.
- [ ] Conferir comentários abertos/fechados, removidos e link para publicação de comentário.
- [ ] Conferir menu, título, descrição e gadgets após salvar no editor de Layout.
- [ ] Conferir larguras de 360, 768 e 1440 px, teclado, zoom a 200% e impressão.
- [ ] Conferir título de página, canonical, descrição e dados gerados pelo cabeçalho nativo.
- [ ] Implementar e conferir página 404.

## Expansão visual e funcional

1. Validar os controles de cores/fontes desta branch no Designer de temas. Logo opcional fica para uma etapa futura.
2. Imagens em resolução adequada e navegação complementar por assuntos. Avaliar destaques apenas se ajudarem a leitura.
3. Comentários incorporados e respostas encadeadas com comportamento nativo.
4. Tempo de leitura, compartilhamento e artigos relacionados, com melhoria progressiva.
5. Versão demonstrativa pública e revisão visual com as fontes carregadas. Guias bilíngues de instalação e personalização já estão disponíveis.
