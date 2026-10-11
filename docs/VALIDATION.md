# Validação da versão — 11/10/2026

[English](en/VALIDATION.md) · [Português](VALIDATION.md)

## Importação no Blogger confirmada

Em 11/10/2026, o proprietário informou importação bem-sucedida e autorizou expressamente a promoção para `v0.1.0` estável. Esta é uma evidência de plataforma relatada pelo mantenedor. O idioma importado e os resultados completos dos widgets não foram registrados; não significa que ambos os XMLs ou todos os comportamentos foram testados independentemente. Os templates XML são os mesmos da alpha importada.

## Checks automatizados

Treze testes verificam seções de widgets inválidas, IDs duplicados, includes ausentes, equivalência de idiomas, metadados nativos e auditoria de SEO no HTML. Os dois XMLs são válidos, a geração de idiomas está atualizada, links Markdown locais e whitespace do Git passam. O CI repete esses checks e gera a prévia. URLs externas e âncoras de títulos não são conferidas automaticamente.

## Evidências da prévia responsiva

- Home e artigo medidos por DOM em 320, 360, 480, 600, 768, 900, 1050 e 1440 px, sem transbordamento horizontal.
- Títulos sem espaços, URLs, tabelas e código conferidos em 320, 360, 768 e 1440 px, com rolagem contida.
- Exemplo de post, figura e iframe vazio 16:9 conferidos em 320, 360, 768 e 1440 px. Mídia dentro da coluna de leitura.
- Privacidade conferida em 320, 768 e 1440 px: um H1, microdados WebPage, link atual destacado e navegação para Contato funcionando.
- A fixture da home tem três cards e uma entrada distinta na lista.

## Limites e próximas verificações

São checks de CSS/DOM em fixtures, não execução do compilador do Blogger. A importação foi confirmada pelo proprietário. Testes completos de dados nativos, gadgets, comentários, paginação e marcação publicada seguem pendentes. A captura de tela estava indisponível e o carregamento das fontes remotas não foi confirmado; as medidas refletem fontes de fallback. Não há comprovação de Core Web Vitals nem posição em buscas.

O proprietário autorizou a versão estável após confirmar a importação; o [checklist de plataforma](ROADMAP.md) registra verificações complementares. Consulte [SEO.md](SEO.md) para auditar HTML publicado e [RELEASE.md](RELEASE.md) para instalação e conteúdo do pacote.

## Branch de desenvolvimento: personalização nativa

Os controles de cores/fontes são alterações novas e não estão cobertos pelo relato de importação da versão estável acima. Dezoito testes locais passam, incluindo resolução de variáveis, equivalência de idiomas e contraste mínimo de 4,5:1 do texto padrão. A prévia usa os valores salvos resolvidos; não verifica se o Blogger apresenta ou salva os controles do Designer. Importe e salve o tema personalizado num blog de teste antes de lançar estas mudanças.

A prévia atualizada foi medida em 320, 360, 768 e 1440px para home, artigo, privacidade, conteúdo longo e mídia, sem transbordamento horizontal da página. O corpo de artigos e páginas resolve para 20px nas quatro larguras.

Uma fixture temporária com texto serif de 24px e fundo areia pastel também respeitou a largura da tela em 320, 768 e 1440px para artigos e privacidade. Estas prévias geradas não integram o Git.
