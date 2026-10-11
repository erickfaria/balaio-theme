# Validação da versão — 11/10/2026

[English](en/VALIDATION.md) · [Português](VALIDATION.md)

## Checks automatizados

Treze testes verificam seções de widgets inválidas, IDs duplicados, includes ausentes, equivalência de idiomas, metadados nativos e auditoria de SEO no HTML. Os dois XMLs são válidos, a geração de idiomas está atualizada, links Markdown locais e whitespace do Git passam. O CI repete esses checks e gera a prévia. URLs externas e âncoras de títulos não são conferidas automaticamente.

## Evidências da prévia responsiva

- Home e artigo medidos por DOM em 320, 360, 480, 600, 768, 900, 1050 e 1440 px, sem transbordamento horizontal.
- Títulos sem espaços, URLs, tabelas e código conferidos em 320, 360, 768 e 1440 px, com rolagem contida.
- Exemplo de post, figura e iframe vazio 16:9 conferidos em 320, 360, 768 e 1440 px. Mídia dentro da coluna de leitura.
- Privacidade conferida em 320, 768 e 1440 px: um H1, microdados WebPage, link atual destacado e navegação para Contato funcionando.
- A fixture da home tem três cards e uma entrada distinta na lista.

## Limites e próximas verificações

São checks de CSS/DOM em fixtures, não execução do compilador do Blogger. Importação, dados nativos, gadgets, comentários, paginação e marcação publicada seguem pendentes. A captura de tela estava indisponível e o carregamento das fontes remotas não foi confirmado; as medidas refletem fontes de fallback. Não há comprovação de Core Web Vitals nem posição em buscas.

A release é alpha até concluir o [checklist de plataforma](ROADMAP.md). Consulte [SEO.md](SEO.md) para auditar HTML publicado e [RELEASE.md](RELEASE.md) para instalação e conteúdo do pacote.
