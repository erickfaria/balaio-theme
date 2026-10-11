# SEO e descoberta em buscas com IA

[Português](SEO.md) · [English](en/SEO.md)

O tema fornece uma base técnica. Posição, indexação e citações também dependem do conteúdo publicado, das configurações do Blogger e dos buscadores. Não existe posição garantida nem um botão universal de “SEO para LLM”.

## O que o tema faz

- Preserva um título de documento e o `all-head-content` nativo do Blogger para canonical, feeds, compartilhamento e regras de indexação configuradas. Evite inserir blocos duplicados de metadados.
- Usa título principal em artigos, páginas e listagens fora da home. A apresentação editável fornece o H1 da home; preserve um H1 significativo ao personalizá-la.
- Identifica o conteúdo visível dos artigos com microdados schema.org `BlogPosting`: título, autor, corpo e permalink. Páginas estáticas usam `WebPage`. Essa abordagem dispensa montar JSON com texto não escapado de posts. Não inventa datas, avaliações, organização ou credenciais editoriais.
- Oferece links HTML, leitura responsiva e imagens decorativas dos cards com alt vazio, dimensões e decodificação assíncrona. Imagens informativas dentro dos posts ainda precisam de texto alternativo escrito por você.

O Google aceita microdados de artigos e recomenda propriedades corretas e aplicáveis. A marcação atual é parcial: datas de publicação/alteração e imagens representativas em alta resolução dependem de campos do Blogger verificados antes de serem adicionadas. Valide a página **publicada** no [Rich Results Test](https://search.google.com/test/rich-results) e inspecione no Search Console. XML válido não comprova que o Blogger renderiza a marcação corretamente. [Documentação de artigos](https://developers.google.com/search/docs/appearance/structured-data/article).

## Configure o Blogger antes de publicar

1. Em **Configurações → Privacidade**, habilite a visibilidade para mecanismos de pesquisa do blog público.
2. Em **Configurações → Metatags**, habilite a descrição de pesquisa e escreva uma descrição curta e fiel do blog. No editor de cada post, preencha **Descrição da pesquisa** com um resumo específico. Confira no HTML uma `meta name="description"` preenchida; o tema depende da saída nativa do Blogger.
3. Configure idioma e redirecionamentos HTTPS. Confira se os endereços alternativos redirecionam para a URL HTTPS preferida e se o canonical de cada artigo aponta para ele mesmo.
4. Revise robots.txt e tags de cabeçalho de robôs personalizados. Preserve exclusões intencionais de páginas privadas/busca; evite `noindex` ou bloqueios acidentais em artigos públicos. Não copie uma receita genérica de liberar tudo.
5. Verifique o domínio no [Google Search Console](https://search.google.com/search-console) e no [Bing Webmaster Tools](https://www.bing.com/webmasters/). Envie o `/sitemap.xml` do Blogger, inspecione artigos representativos e acompanhe erros de indexação.
6. Escreva títulos específicos, subtítulos úteis, links internos descritivos, referências e autoria visível. Mostre datas reais de publicação/atualização quando pertinentes. Evite excesso de palavras-chave e afirmações sem apoio. Comprima imagens e escreva texto alternativo no editor.
7. Após importar, teste home, artigo, página estática, busca, marcador e paginação. Meça desempenho móvel no blog real; fixtures de prévia não comprovam Core Web Vitals.

[Guia de busca do Blogger](https://support.google.com/blogger/answer/41373?hl=pt-BR).

## Busca com IA e escolhas de rastreamento

As buscas com IA do Google usam a base tradicional de SEO, sem exigir arquivo ou schema especial para IA. As páginas precisam ser indexáveis e elegíveis para snippets. [Documentação do Google](https://developers.google.com/search/docs/appearance/ai-features).

Na busca do ChatGPT, `OAI-SearchBot` faz descoberta; `GPTBot` atende ao treinamento de modelos de forma independente. `ChatGPT-User` atende a visitas iniciadas por usuários. Decida permissões de busca e treinamento separadamente; o tema não altera essas políticas. Confira robots.txt e eventuais regras de firewall do domínio. [Documentação oficial da OpenAI](https://developers.openai.com/api/docs/bots).

O repositório não gera `llms.txt`, instruções ocultas para IA ou sitemap substituto. O Blogger serve robots.txt e sitemaps fora do template.

## Inspecione o HTML renderizado

Sem dependências adicionais:

```sh
python3 scripts/audit_seo.py --url https://www.example.com/
python3 scripts/audit_seo.py --url https://www.example.com/2026/10/example.html
python3 scripts/audit_seo.py --file /tmp/pagina-salva.html
```

O relatório JSON verifica título, canonical, descrição, H1, idioma, ausência de alt, sintaxe JSON-LD e restrições de pesquisa. Código de saída 1 indica erro estrutural; avisos precisam de contexto e não alteram o código. O escopo de cada robô permanece no relatório. A auditoria **não** comprova indexação, completude de schema, acesso via robots.txt ou desempenho. Não execute sobre XML de template não compilado. Falhas HTTP são erros; redirecionamentos são seguidos e o HTML final é inspecionado.

## Diagnóstico público — 11/10/2026

Observações somente de leitura em `https://www.balaiocientifico.com/`, **antes de instalar o tema desta branch**:

- Home e `/2025/04/analise-de-dados-do-cnes-no-jamovi.html` retornam HTTP 200, com canonical HTTPS apontando para a própria página.
- O H1 do artigo inspecionado contém o nome do blog, não o título do artigo. O novo tema atribui o H1 ao título do artigo.
- As duas páginas inspecionadas não têm meta description padrão; a descrição de compartilhamento da home está vazia. Configure descrições de pesquisa e confira novamente o HTML.
- `/robots.txt` permite rastreamento geral de artigos públicos e exclui `/search` e `/share-widget`; anuncia `/sitemap.xml`.
- O sitemap responde com um conjunto de URLs XML preenchido. Seu `X-Robots-Tag: noindex` aplica-se à resposta do sitemap e não comprova exclusão dos artigos.

Isso não comprova indexação real, citações por IA ou desempenho. Nenhuma configuração ou conteúdo publicado foi alterado nesta auditoria.
