# Plano de desenvolvimento

[English](en/ROADMAP.md) · [Português](ROADMAP.md)

## Base entregue

XMLs alpha, home com lista editorial, artigos, páginas, busca, marcadores, paginação, comentários básicos, gadgets e CSS responsivo. Na home, os três primeiros posts são cards de abertura; os demais ficam na lista, sem duplicação. Busca e arquivos preservam a listagem comum. Os campos `thumbnailUrl`, `snippet`, `locale` e o estado de lista vazia precisam ser confirmados durante a importação.

## Próxima etapa: validar no Blogger

- [ ] Importar as duas variantes de idioma em blog de teste e registrar qualquer erro de compilação.
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

1. Logo opcional e cores/fontes configuráveis pelo Designer de temas.
2. Imagens em resolução adequada e navegação complementar por assuntos. Avaliar destaques apenas se ajudarem a leitura.
3. Comentários incorporados e respostas encadeadas com comportamento nativo.
4. Tempo de leitura, compartilhamento e artigos relacionados, com melhoria progressiva.
5. Versão demonstrativa pública e revisão visual antes do primeiro release estável. Guias bilíngues de instalação e personalização já estão disponíveis.
