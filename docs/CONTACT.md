# Contato nativo do Blogger — rc.11

[English](en/CONTACT.md) · [Português](CONTACT.md)

O tema inclui **ContactForm1**, um widget nativo do Blogger com visual próprio, minimalista e responsivo. O visitante não precisa entrar numa conta: nome é opcional, e-mail e mensagem são obrigatórios. Não é anonimato completo: os responsáveis recebem o e-mail informado, e o Blogger processa o envio.

## Ativar uma vez em cada blog

1. Faça backup e importe o XML atualizado no idioma desejado. Guarde a rc.10 enquanto confirma a nova instalação.
2. Em **Configurações**, selecione o idioma do blog. Os rótulos do tema seguem o XML escolhido; as mensagens de envio/erro do widget seguem o idioma do Blogger.
3. Em **Páginas → Nova página**, crie **Contato** (português) ou **Contact** (inglês). Se a página já existe, reutilize-a.
4. No modo HTML do editor, copie apenas o corpo de [contact.pt-BR.html](../examples/pages/contact.pt-BR.html) ou [contact.en.html](../examples/pages/contact.en.html). Os textos são genéricos e editáveis. Não cole outro formulário, um documento completo nem o XML do tema.
5. Publique e confira o endereço: **`/p/contato.html` ou `/p/contact.html`**. O tema mostra o formulário nessas páginas estáticas; não na home, em artigos, busca ou outras páginas. O menu automático encontra a página publicada ao atualizar.
6. Abra a página pública e confira uma entrega para a sua própria caixa de entrada, incluindo spam. Os testes locais não enviam e-mails e não comprovam entrega pelo Blogger.

A condição compara a URL canônica da página com a URL canônica do blog, mantendo o contato acessível também com parâmetros móveis como `?m=1`.

O XML instala o widget e seu layout; **não cria registros de páginas**. Publicar a página no painel é a única etapa de conteúdo necessária. O tema não substitui uma página existente nem altera seus textos. [Criar páginas no Blogger](https://support.google.com/blogger/answer/165955?hl=pt-BR).

## Destino e funcionamento

Não há destinatário, chave de API, senha ou token fixo no tema. O Blogger gera os dados da sessão e determina o destino a partir do blog e de suas configurações. Confira a conta e os administradores do blog ao validar o recebimento. O endereço do responsável não é incluído no HTML pelo Balaio.

O envio depende do **JavaScript nativo do Blogger**, inclusive seus dados de sessão. Não copie apenas o HTML do formulário para um post/página e não remova o widget ContactForm1 ou os scripts nativos do tema. Nome e e-mail usam preenchimento automático, os rótulos são associados aos campos, e os retornos de erro/status têm regiões acessíveis. Sem JavaScript, o tema informa que o formulário precisa dele.

Não há iframe, formulário de serviço pago nem biblioteca de envio adicionada pelo Balaio. O tema não envia mensagens por conta própria nem registra formulários em serviços externos. [Orientação da comunidade do Blogger sobre widget e sessão](https://support.google.com/blogger/thread/252064400/how-to-edit-contact-form-gadget-texts?hl=en).

## Outro endereço ou desativação

Para um endereço como `/p/fale-comigo.html`, edite somente os caminhos na condição `cond` do widget **ContactForm1**, preservando `data:blog.pageType == "static_page"`. Não altere a condição ou os includes de **Blog1**. Nenhum domínio específico é necessário. Se quiser controlar o menu manualmente, use [PAGES.md](PAGES.md).

Para desativar, remova **Formulário de contato** no Layout. Se houver um ContactForm antigo no blog, mantenha somente um widget e confira seus IDs após importar, para evitar registros duplicados. Guarde as personalizações antes de reimportar o XML.

## Código, privacidade e validação

O markup, CSS e exemplos próprios são MIT. O envio, a proteção contra abuso, o JavaScript e a infraestrutura do **Blogger/Google são serviços externos**, não código aberto distribuído ou coberto pela licença deste repositório. Nenhuma cópia dessa biblioteca é incluída no pacote. Inter e Newsreader mantêm SIL OFL.

O texto junto ao formulário informa o tratamento pelo Blogger. Adapte a página de privacidade do blog ao uso efetivo do contato; o exemplo de privacidade continua sendo apenas um placeholder. O tema não adiciona um armazenamento próprio de mensagens, analytics ou rastreadores ao formulário.

As prévias locais desativam Enviar e não fazem requisições de contato. Elas verificam layout, idiomas, rótulos, campos e estados ilustrativos. **Importação e entrega da rc.11 ainda precisam de confirmação no Blogger.** [Evidências e limites](VALIDATION.md).
