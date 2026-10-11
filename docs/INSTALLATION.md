# Instalar e usar

[English](en/INSTALLATION.md) · [Português](INSTALLATION.md)

## Antes de instalar

Use um blog de teste com alguns posts e uma página. Guarde o backup do tema atual. A versão é experimental e ainda precisa de validação por importação no Blogger.

## Passo a passo

1. Baixe `theme/balaio.xml` para português ou `theme/balaio.en.xml` para inglês. Baixe o arquivo raw, sem copiar a página HTML do GitHub.
2. No Blogger, selecione o blog correto e vá a **Tema → menu → Fazer backup**.
3. Em **Tema → menu → Editar HTML**, substitua o conteúdo pelo XML completo, desde a declaração inicial até o fechamento de `html`, e salve.
4. Configure título, descrição e idioma em **Configurações**. Em **Layout**, ajuste Menu, Apresentação, marcadores, lateral e rodapé. Os gadgets têm nomes ingleses no XML inglês.
5. Publique posts fictícios com e sem imagem para testar os cards. A home usa os três posts mais recentes da página; configure mais de três posts por página se quiser também a lista abaixo.
6. Abra artigos, páginas, busca, marcadores e outras páginas de posts. Confira comentários e celular. Veja [ROADMAP.md](ROADMAP.md).

## Dúvidas comuns

| Problema | Como conferir |
| --- | --- |
| O editor rejeita o arquivo | Confira se copiou o XML completo, sem cercas de Markdown ou HTML do GitHub. Registre a mensagem exata para uma issue. |
| Não há imagem no card | Use um post com imagem. A miniatura depende dos dados fornecidos pelo Blogger; sem imagem, a entrada continua legível. |
| As fontes parecem diferentes | Confira acesso ao Google Fonts. O fallback usa fontes do dispositivo quando as fontes remotas não carregam. |
| O menu não tem minhas páginas | Cadastre os links no gadget Menu. O tema não cria as páginas do blog. |
| A abertura continua igual | Edite Apresentação/Introduction no Layout e salve. Preserve um único `h1`. |
| Comentários não aparecem | Confira as configurações e permissões do post. O formulário incorporado e as respostas encadeadas ainda não estão prontos. |
| Quero voltar ao tema anterior | Restaure o XML que você salvou antes da instalação pelo menu do tema. |

Posts, imagens e URLs não são migrados por este tema. Guarde uma cópia do XML que personalizou. A instalação altera a apresentação do blog; mantenha seus backups separados do repositório.

[Personalizar](CUSTOMIZATION.md) · [Voltar ao README](../README.pt-BR.md) · [Ajuda oficial do Blogger](https://support.google.com/blogger/answer/176245?hl=pt-BR)

Antes de publicar, siga a [configuração de SEO](SEO.md).
