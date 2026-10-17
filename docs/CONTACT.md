# Contato: referência e configuração manual — rc.12

[English](en/CONTACT.md) · [Português](CONTACT.md)

O Balaio inclui apenas um [modelo de conteúdo de Contato](../examples/pages/contact.pt-BR.html), editável. **O tema não cria a página, não instala formulário de contato e não ativa um formulário pelo endereço.** A criação da página, o canal de contato e qualquer formulário ficam a cargo de quem administra o blog.

## Criar sua página

1. Em **Blogger → Páginas → Nova página**, crie Contato. Se já existe uma página, reutilize-a.
2. No modo HTML do editor, copie o corpo de [contact.pt-BR.html](../examples/pages/contact.pt-BR.html) ou [contact.en.html](../examples/pages/contact.en.html) e substitua o texto de orientação pelos seus canais reais de contato. O tema já fornece o H1.
3. Publique e **copie a URL que o próprio Blogger gerar**. Não deduza o endereço a partir do título: ele pode conter um sufixo, como `/p/contato_1234567890.html`. Esse endereço é válido; não é necessário recriar a página para tentar obter `/p/contato.html`.
4. Use a URL real no gadget **Páginas/Menu** se configurar os links manualmente. A navegação automática existente também usa a URL retornada no feed das páginas publicadas, incluindo sufixos. [Modos do menu](PAGES.md).
5. Abra a URL pública e confira o texto e os links no celular. O XML não publica nem altera o conteúdo dessa página.

[Instruções do Blogger para páginas](https://support.google.com/blogger/answer/165955?hl=pt-BR).

## Se quiser um formulário

Configure o formulário separadamente, com o serviço ou recurso escolhido. Defina destinatário, campos, apresentação e o local de exibição; depois confira uma entrega real. O modelo de conteúdo deste repositório não contém formulário nem botão de envio.

O Blogger oferece o gadget **Formulário de contato**. Ele usa o JavaScript e a sessão nativos da plataforma; copiar apenas o HTML de um formulário para uma página não configura o envio. Este tema não reserva uma área visível para esse gadget: a instalação e o posicionamento devem ser configurados manualmente no Layout/XML. A lateral legada está oculta; adicionar o gadget nela não o torna visível. [Orientação do Blogger sobre gadgets](https://support.google.com/blogger/answer/176245?hl=pt-BR) · [Requisitos do widget de contato](https://support.google.com/blogger/thread/252064400/how-to-edit-contact-form-gadget-texts?hl=en).

Se desejar envio sem login, confira esse comportamento no formulário que você configurar. Informe aos leitores quais dados são enviados, quem os recebe e qual serviço os processa. A página de privacidade deve refletir a configuração real do blog; o exemplo incluído continua sendo apenas um placeholder.

## Atualizar a partir da rc.11

A rc.11 tentou vincular ContactForm1 a dois caminhos fixos. Essa integração foi removida na rc.12. Importe o XML atualizado. Se o Blogger preservar o **Formulário de contato / ContactForm1** criado pela rc.11, remova esse gadget no Layout; mantenha a página e qualquer formulário que você tenha configurado por conta própria.

Edite também o conteúdo da página no painel: retire frases como “formulário abaixo” se não houver um formulário configurado. Importar o XML não substitui textos já publicados.

O código próprio e o modelo textual são MIT; as fontes Inter/Newsreader mantêm SIL OFL. Qualquer serviço de formulário escolhido tem seus próprios termos. A rc.12 não acrescenta transporte, armazenamento, credenciais ou biblioteca de contato ao tema. [Validação](VALIDATION.md).
