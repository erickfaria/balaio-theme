# Verificação local — 11/10/2026

[English](en/VALIDATION.md) · [Português](VALIDATION.md)

## Resultado

- XML e estrutura local passaram em `scripts/validate_theme.py`.
- Prévia de home e artigo examinada pelo DOM do navegador em viewports de 360, 768 e 1440 px. Em todas, a largura rolável do documento ficou igual à largura disponível, sem transbordamento horizontal da página.
- Blocos de código e tabelas mantêm rolagem dentro da área de leitura quando necessário.
- Posts sem imagem ocupam a largura da entrada, sem reservar uma coluna vazia.
- Navegação da home para a leitura foi exercitada na prévia.

O teste encontrou um transbordamento causado pela largura mínima dos itens do grid no artigo. A base agora define `min-width: 0` para os filhos do grid e limita a coluna de leitura à largura disponível.

## Limitações

A prévia usa o CSS real e marcação de exemplo; não interpreta os widgets ou expressões do Blogger. O gadget de apresentação, os dados reais, os comentários e a paginação ainda precisam ser validados na plataforma. A captura de tela não estava disponível no navegador desta sessão; esta verificação foi feita por estrutura e medidas do DOM, sem revisão por screenshot.

Não há confirmação de importação bem-sucedida no Blogger. O checklist completo está em [ROADMAP.md](ROADMAP.md).

## Refinamento de cards e tipografia

- Prévia da home conferida por DOM em 360, 768 e 1440 px, sem transbordamento da página.
- A fixture exibe três cards de abertura e uma entrada na lista, com quatro publicações ao todo, sem repetição.
- O CSS computado utiliza a família Inter na interface. A confirmação de download das fontes não foi concluída: a espera do navegador excedeu o tempo disponível. O fallback permanece configurado. A tipografia final precisa de revisão visual em ambiente com acesso ao Google Fonts.
- Quatro testes estruturais do validador passaram localmente. O PR inicial passou no CI do GitHub antes do merge. A implementação de SEO em `15ad07e` também passou no [CI do GitHub](https://github.com/erickfaria/balaio-theme/actions/runs/38142451054).

## Revisão responsiva e bilíngue

- Home e artigo medidos por DOM em viewports de 320, 360, 480, 600, 768, 900, 1050 e 1440 px: sem transbordamento horizontal do documento.
- Fixture com título sem espaços, URLs extensas, tabela larga e código sem quebras conferida em 320, 360, 768 e 1440 px, também sem transbordamento da página.
- Quebra de títulos longos e largura mínima do cabeçalho reforçadas no CSS.
- Variantes XML em português e inglês validadas. Dois testes adicionais garantem CSS equivalente e as mesmas identidades de widgets; seis testes passaram ao todo.
- Links locais da documentação bilíngue conferidos automaticamente. Âncoras e URLs externas não fazem parte desse check.
- As fontes remotas não apareceram como carregadas na inspeção atual; os testes de largura refletem o fallback. A revisão visual com as fontes finais continua pendente.

## Validação da branch de SEO

Doze testes locais cobrem XML, idiomas, metadados nativos e auditoria de HTML. Esta branch adiciona microdados parciais de artigos/páginas e títulos de listagens; importação no Blogger e validação de resultados enriquecidos seguem pendentes. O [guia de SEO](SEO.md) registra o diagnóstico público, separado da verificação do template.

## Diagnóstico público — 11/10/2026

Observações somente de leitura em `https://www.balaiocientifico.com/`, **antes de instalar o tema desta branch**:

- Home e `/2025/04/analise-de-dados-do-cnes-no-jamovi.html` retornam HTTP 200, com canonical HTTPS apontando para a própria página.
- O H1 do artigo inspecionado contém o nome do blog, não o título do artigo. O novo tema atribui o H1 ao título do artigo.
- As duas páginas inspecionadas não têm meta description padrão; a descrição de compartilhamento da home está vazia. Configure descrições de pesquisa e confira novamente o HTML.
- `/robots.txt` permite rastreamento geral de artigos públicos e exclui `/search` e `/share-widget`; anuncia `/sitemap.xml`.
- O sitemap responde com um conjunto de URLs XML preenchido. Seu `X-Robots-Tag: noindex` aplica-se à resposta do sitemap e não comprova exclusão dos artigos.

Isso não comprova indexação real, citações por IA ou desempenho. Nenhuma configuração ou conteúdo publicado foi alterado nesta auditoria.

## Revisão de buscadores e layout das postagens

Treze testes locais passam, incluindo restrição com escopo de DuckDuckBot. A fixture `media.html` usa o exemplo editável de post em português, figura e iframe vazio de vídeo 16:9. Medições por DOM em 320, 360, 768 e 1440 px não mostraram transbordamento horizontal; figura e iframe ficaram na coluna de leitura. Isso verifica contêineres, não reprodução de vídeo nem importação no Blogger.

## Revisão de páginas básicas

A prévia de Privacidade tem um H1, microdados WebPage e destaque do link atual no menu. Medições por DOM em 320, 768 e 1440 px não mostraram transbordamento horizontal. A navegação de Privacidade para Contato funcionou. Os corpos das páginas usam Lorem ipsum; não são conteúdo publicado do site. Os treze testes estruturais e de SEO passam. Importação e funcionamento dos gadgets no Blogger seguem pendentes.
