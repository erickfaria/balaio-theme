# Escrever posts Blogger responsivos e preparados para SEO

[English](en/POSTS.md) · [Português](POSTS.md)

O tema exibe o título do post como H1 e usa título, autor, corpo e permalink visíveis nos microdados de artigo. Escreva o corpo com seções H2 e subseções H3; não insira outro H1 nem um segundo schema de artigo. Layout e marcação descrevem o mesmo conteúdo em celular e desktop. As propriedades do schema não mudam nos breakpoints de tela.

## Comece com um exemplo editável

Copie [post.pt-BR.html](../examples/post.pt-BR.html) para o modo HTML do editor de posts do Blogger. Substitua todo o conteúdo de exemplo e defina um título significativo e uma descrição de pesquisa. O exemplo inclui resumo, método, resultados, tabela acessível, limitações e referências. Use apenas as seções úteis para seu artigo.

## Imagens e mídia

Em imagens informativas, escreva alt fiel e informe as dimensões reais do arquivo. A legenda pode trazer contexto e créditos:

```html
<figure>
  <img src="URL_HTTPS_DA_IMAGEM" alt="Descreva o que a imagem explica"
       width="1200" height="800" loading="lazy" decoding="async">
  <figcaption>Contexto, fonte e créditos.</figcaption>
</figure>
```

Substitua URL e dimensões pelos valores da imagem. Use carregamento eager numa imagem importante visível de imediato; mantenha imagens secundárias em lazy. O CSS limita imagens e vídeos nativos à coluna de leitura. Imagens complementam o texto do artigo.

Para um iframe de vídeo 16:9, use o contêiner opcional abaixo. Ele ocupa a coluna de leitura sem largura fixa de desktop:

```html
<div class="video">
  <iframe src="URL_HTTPS_DE_INCORPORACAO" title="Título descritivo do vídeo"
          loading="lazy" allowfullscreen></iframe>
</div>
```

Use a URL de incorporação do provedor. Outras proporções precisam de `aspect-ratio` correspondente. Inclua transcrição ou resumo textual quando útil. O contêiner não implica dados estruturados de vídeo.

## Tabelas, código e links

Tabelas largas e código rolam dentro de seus contêineres. Use legendas e cabeçalhos com `scope` nas tabelas. Evite estilos inline de largura fixa no corpo. Escreva links descritivos para posts relacionados e fontes originais. Mantenha a autoria correta nas configurações do Blogger; registre alterações relevantes no texto quando atualizar um artigo.

Confira títulos longos, mídia, tabelas e código em uma largura de celular após publicar. A prévia demonstra layout; as [verificações de SEO](SEO.md) inspecionam metadados renderizados. A importação de teste no Blogger continua necessária.

## Leitura e prévias nas listas

A v0.2.0-rc.1 usa Newsreader em 22px com entrelinha de 1,75 no corpo de posts/páginas. H2/H3 seguem o tamanho de leitura selecionado. Evite tamanhos fixos copiados de outros editores, que podem substituir a tipografia do tema. Em posts longos, insira a quebra de expansão nativa do Blogger após a introdução; ela mantém o artigo completo no permalink e pode ajudar a paginação da home. A quantidade máxima na home é uma configuração do Blogger, não um limite do tema. [Editor de posts](https://support.google.com/blogger/answer/154172?hl=pt-BR) · [Instalação](INSTALLATION.md).
