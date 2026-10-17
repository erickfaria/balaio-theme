# Instalar e usar

[English](en/INSTALLATION.md) · [Português](INSTALLATION.md)

## Antes de instalar

Use o XML da rc.9 na main: lupa recolhível ao lado do título, espaços menores e menu que revalida páginas publicadas, sobre os gadgets da rc.8 já importada. A nova importação da rc.9 ainda precisa de conferência. Antes de instalar em outro blog, guarde seu backup e confira num blog de teste. Os pacotes de releases antigos não contêm esta versão.

## Passo a passo

1. Baixe `theme/balaio.xml` para português ou `theme/balaio.en.xml` para inglês. Baixe o arquivo raw, sem copiar a página HTML do GitHub.
2. No Blogger, selecione o blog correto e vá a **Tema → menu → Fazer backup**.
3. Em **Tema → menu → Editar HTML**, substitua o conteúdo pelo XML completo, desde a declaração inicial até o fechamento de `html`, e salve.
4. Configure título, descrição e idioma em **Configurações**. Páginas publicadas completam o menu automaticamente. Em **Layout**, ajuste links iniciais de Páginas, Menu e Apresentação; veja os modos automático/manual em [PAGES.md](PAGES.md). Não há lateral neste layout; gadgets antigos de busca, arquivo e destaque ficam ocultos. Os gadgets têm nomes ingleses no XML inglês.
5. Publique posts fictícios com e sem imagem para testar os cards. A home destaca os dois posts mais recentes e mostra os seguintes em lista. A continuação automática complementa páginas curtas; veja [HOME.md](HOME.md).
6. Abra artigos, páginas, busca, marcadores e outras páginas de posts. Confira comentários e celular. Veja [ROADMAP.md](ROADMAP.md).

## Usar o tema responsivo no celular

O Blogger pode servir um template móvel antigo separado. Se o celular mostra barras de data cinza, links azuis e outro cabeçalho em `?m=1`, enquanto `?m=0` mostra os cards pastel do Balaio, as duas requisições estão usando apresentações diferentes.

Em **Tema**, abra o menu ao lado de **Personalizar**. Se houver **Configurações para dispositivos móveis**, selecione **Computador/Desktop** (ou a opção de mostrar o tema de computador no celular) e salve. O Balaio adapta seu próprio layout à largura da tela; essa configuração escolhe qual template o Blogger entrega. Os nomes dos menus podem variar conforme a interface do Blogger.

Abra novamente a URL normal do blog no celular, sem acrescentar `?m=0` manualmente. Confira a home, um artigo completo e uma página estática. Compare também `?m=1` e `?m=0` para identificar diferenças restantes. Não use redirecionamento por JavaScript como substituto dessa configuração.

As capturas do proprietário mostraram a apresentação móvel antiga em `?m=1` e os cards do Balaio em `?m=0`. Elas não confirmam a versão instalada nem os novos controles do Designer. [Explicação oficial sobre templates móveis separados](https://blogger-developers.googleblog.com/2011/11/introducing-custom-mobile-templates.html).

## Dúvidas comuns

| Problema | Como conferir |
| --- | --- |
| O editor rejeita o arquivo | Confira se copiou o XML completo, sem cercas de Markdown ou HTML do GitHub. Registre a mensagem exata para uma issue. |
| Não há imagem no card | Use um post com imagem. A miniatura depende dos dados fornecidos pelo Blogger; sem imagem, a entrada continua legível. |
| As fontes parecem diferentes | Confira acesso ao Google Fonts. O fallback usa fontes do dispositivo quando as fontes remotas não carregam. |
| O menu não tem minhas páginas | Confirme a rc.9, páginas publicadas, JavaScript e o feed público habilitado. Abra ou atualize o blog após publicar; rascunhos ficam fora do feed. Links manuais precisam ser removidos no gadget. No modo manual, adicione links em **Layout → Páginas**. [Modos do menu](PAGES.md). |
| A abertura continua igual | Edite Apresentação/Introduction no Layout e salve. Preserve um único `h1`. |
| Comentários não aparecem | Confira as configurações e permissões do post. O formulário incorporado e as respostas encadeadas ainda não estão prontos. |
| Quero voltar ao tema anterior | Restaure o XML que você salvou antes da instalação pelo menu do tema. |

Posts, imagens e URLs não são migrados por este tema. Guarde uma cópia do XML que personalizou. A instalação altera a apresentação do blog; mantenha seus backups separados do repositório.

[Personalizar](CUSTOMIZATION.md) · [Voltar ao README](../README.pt-BR.md) · [Ajuda oficial do Blogger](https://support.google.com/blogger/answer/176245?hl=pt-BR)

Antes de publicar, siga a [configuração de SEO](SEO.md).

## Páginas básicas

[Modelos de Sobre, Contato e Privacidade](PAGES.md) usam Lorem ipsum. Crie e publique as páginas no Blogger e selecione-as em **Layout → Páginas**. O tema não fixa endereços de páginas nem dados de contato. Código e recursos visuais incluídos são MIT; Inter e Newsreader são fontes abertas sob SIL OFL.

## Mostrar mais posts e páginas fixas

O tema exibe todos os posts fornecidos pelo Blogger: os dois primeiros em cards, seguidos de uma lista sem duplicações. Na home, a continuação automática consulta até quatro páginas adicionais para tentar atingir dez posts; fora da home, a paginação continua nativa. Configure **Configurações → Postagens → Máximo de postagens exibidas na página principal** como **10** para começar. É um máximo, não uma garantia: o Blogger pode paginar antes em posts grandes. Se a continuação não carregar, confira a rede e o link de posts anteriores em [HOME.md](HOME.md). Adicione uma **quebra de expansão** nativa após a introdução dos posts longos e confira novamente. Não mude datas de publicação nem duplique posts. [Configurações do Blogger](https://support.google.com/blogger/answer/9691230?hl=pt-BR) · [Editor de posts](https://support.google.com/blogger/answer/154172?hl=pt-BR).

A navegação superior agora inclui **Páginas** (`PageList1`), habilitado no celular. Publique Sobre mim, Contato e Privacidade em **Páginas** e selecione-as em **Layout → Páginas**. O gadget separado **Menu** aceita links extras. As configurações de um `PageList1` existente podem ser preservadas na importação; confira sua posição no Layout. O XML não altera conteúdo de páginas nem configurações do blog.

## Falha ao restaurar

A validação local não executa o compilador nem a migração de gadgets do Blogger. A rc.6 recupera os gadgets completos da rc.3; a lateral legada permanece oculta por CSS. Faça backup antes de instalar. Se Restaurar falhar ou a página ficar vazia, tente **Tema → Editar HTML** com o XML completo e registre a mensagem exata do editor. Confirme que o arquivo começa com `<?xml` e que a versão é `0.2.0-rc.9` no meta `balaio-version`. Confira a URL pública fora da prévia do editor. Não altere nem reimporte o conteúdo do blog para resolver uma falha de apresentação.
