# Validação — v0.2.0-rc.1

[English](en/VALIDATION.md) · [Português](VALIDATION.md)

## Status

Versão candidata preparada em 11/10/2026. O proprietário confirmou a importação da v0.1.0 anterior, mas os XMLs alterados da v0.2.0-rc.1 ainda precisam de nova importação no Blogger. Não há afirmação de que ambos os idiomas ou todos os gadgets nativos tenham sido testados independentemente na plataforma.

## Checks automatizados

Vinte testes verificam estrutura XML/gadgets, equivalência de idiomas, metadados nativos de SEO e auditoria de HTML, resolução das variáveis do Designer/contraste padrão e regressões de navegação/busca móvel. Os dois XMLs são válidos; a geração inglesa está atualizada; links Markdown locais e whitespace passam. O CI repete os checks e gera prévia e pacote limpo. Links externos e âncoras de títulos não são conferidos automaticamente.

## Evidências da prévia responsiva

- Home com nove posts: três cards e seis entradas distintas em 320, 360, 768, 801, 1050 e 1440px, sem transbordamento horizontal da página.
- Artigo, privacidade e conteúdo longo em 320, 360, 768 e 1440px: leitura de 22px e entrelinha de 38,5px, com conteúdo largo contido.
- Assuntos no celular: os 24 links continuam visíveis, com ao menos 44px de altura e uma única divisória externa. A comparação anterior de espaçamento em 360px reduziu o cabeçalho de 290px para 258px e a lista de 885px para 642px.
- Navegação de Privacidade: um H1, microdados WebPage e indicação de página atual.
- Fixture de Perfil/Atribuição herdados: ocultos em 320, 768 e 1440px; lateral de artigo oculta e nenhum rodapé gerado.

São checks de CSS/DOM em exemplos, não compilação do Blogger nem revisão visual completa por captura de tela. As capturas estavam indisponíveis na revisão anterior; o carregamento remoto das fontes nas fixtures locais não foi confirmado.

## Auditoria do blog publicado

A inspeção por navegador de `www.balaiocientifico.com` em 11/10 encontrou CSS anterior, menu superior vazio, dois posts na home e outros pela paginação. A busca móvel acrescentava `search` depois de `?m=1`; a candidata usa `/search`. Foram observadas requisições de fontes Inter/Newsreader e famílias calculadas correspondentes. Um artigo público medido em 360px ainda usava o texto anterior de 18px.

A auditoria corresponde ao tema anterior instalado, não à publicação desta candidata. Nenhum conteúdo ou configuração do blog foi alterado.

## Checks de plataforma pendentes

Importe a candidata num blog de teste; salve cores/fontes no Designer; confira posição de Páginas/Menu, ambos os idiomas, busca, marcadores, listas vazias, miniaturas, paginação e comentários. Confira teclado, zoom a 200% e impressão. Registre o idioma e os resultados antes de promover esta candidata a estável. Core Web Vitals, indexação e posição em buscas/IA não são comprovados por estes checks.

[Checklist de plataforma](ROADMAP.md) · [Auditoria de SEO](SEO.md) · [Atualização e arquivos da versão](RELEASE.md)
