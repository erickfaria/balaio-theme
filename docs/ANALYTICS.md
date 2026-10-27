# Google Analytics opcional

[English](en/ANALYTICS.md) · [Português](ANALYTICS.md)

A partir da rc.16, os dois XMLs usam a integração nativa do Blogger com Google Analytics 4 (GA4). O tema lê o ID configurado pelo proprietário nas Configurações do blog. Não contém ID de demonstração ou do autor.

## Ativar

1. No Google Analytics, crie uma propriedade GA4 e um fluxo de dados da Web para seu blog. Copie o **ID de métricas**, que começa com `G-`.
2. Instale o XML atualizado do Balaio no idioma escolhido. [Instalação](INSTALLATION.md).
3. No Blogger, abra **Configurações → Básicas → ID de métricas do Google Analytics**, cole seu ID `G-…` e salve. O nome do campo pode aparecer como “ID de medição do Google Analytics”.
4. Abra a URL pública do blog e confira o relatório **Tempo real** do Analytics. O aparecimento dos dados pode levar algum tempo; bloqueadores e suas escolhas de consentimento também podem impedir o envio.

Se já houver um snippet de Analytics ou Tag Manager adicionado manualmente para a mesma propriedade, escolha um único caminho de instalação para evitar eventos duplicados. Com a integração nativa, não é preciso colar o código do Google no XML ou em um gadget HTML/JavaScript.

[Configuração oficial do Google para Blogger](https://support.google.com/analytics/answer/14854594?hl=pt-BR) · [Ajuda do Blogger sobre Analytics](https://support.google.com/blogger/answer/7039627?hl=pt-BR).

## Funcionamento e desativação

A chamada global fica antes do fechamento de `body`, fora dos gadgets e dos scripts do tema:

```xml
<b:if cond='data:blog.analyticsAccountNumber'>
  <b:include data='blog' name='google-analytics'/>
</b:if>
```

Sem ID configurado, essa chamada não é executada. Para desligar a integração, apague o ID nas Configurações do Blogger. Home, posts, páginas e busca usam a mesma chamada; não é necessário configurar cada texto. Ela não altera as estatísticas próprias do painel do Blogger.

O Blogger fornece e mantém o código de rastreamento; o repositório não o copia nem distribui outra biblioteca. O [include nativo](https://blogger-developers.googleblog.com/2011/10/today-we-have-made-change-to-layouts.html) é a conexão com a plataforma; a configuração atual de GA4 é descrita na ajuda do Google acima.

## Leveza, dados e validação

Com Analytics ativado, o serviço externo acrescenta JavaScript e requisições ao Google. A base sem ID mantém o comportamento anterior, sem Analytics acrescentado por esta integração. Nenhum CSS, fonte, gadget ou script próprio foi adicionado. Google Analytics mantém seus próprios termos e não é parte do código MIT distribuído neste repositório.

Atualize o texto de Privacidade para descrever os serviços que você decidir usar. O tema não configura consentimento nem substitui controles que a instalação venha a exigir.

Os checks locais validam XML, idiomas, pacote e a preservação dos scripts/gadgets. Eles não executam o include do Blogger nem comprovam coleta de dados. A importação e a chegada de eventos a uma propriedade real precisam ser conferidas depois da configuração. A prévia local não carrega Analytics.
