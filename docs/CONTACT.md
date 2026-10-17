# Contato com ativação simples — rc.13

[English](en/CONTACT.md) · [Português](CONTACT.md)

O formulário nativo já está incluído nos dois XMLs do tema, em uma área própria fora da lateral oculta. **Você só cria ou edita a página Contato e cola o conteúdo abaixo no modo HTML.** Não precisa editar linhas do XML, adicionar gadgets ou escolher uma URL especial.

## Ativar em três passos

1. Importe o XML atual do tema no idioma desejado. Ao atualizar, mantenha uma cópia do tema anterior.
2. Em **Blogger → Páginas**, abra a página Contato existente ou crie uma. No editor, selecione **modo HTML** e cole:

```html
<p>Tem uma dúvida, sugestão ou proposta?</p>
<p class="balaio-contact-page">Preencha o formulário abaixo para entrar em contato.</p>
```

3. Publique ou atualize a página e abra seu endereço público. Faça um envio de teste e confira o recebimento, inclusive a pasta de spam.

O mesmo conteúdo está em [contact.pt-BR.html](../examples/pages/contact.pt-BR.html); a tradução está em [contact.en.html](../examples/pages/contact.en.html). O tema fornece o título H1 e os campos. Você pode editar o texto: **mantenha `class="balaio-contact-page"` em um elemento do corpo da página**.

Qualquer nome e endereço de página funciona, inclusive URLs com sufixo numérico. Não é preciso apagar, recriar ou renomear a página para obter `/p/contato.html`. O tema não cria registros de páginas nem modifica seu conteúdo ao importar. [Instruções do Blogger para páginas](https://support.google.com/blogger/answer/165955?hl=pt-BR).

## O que aparece

- Nome opcional, e-mail obrigatório para receber resposta e mensagem obrigatória.
- Rótulos ligados aos campos, foco visível, mensagem de erro/sucesso acessível e botão arredondado.
- Coluna responsiva com a paleta e a fonte de interface do tema. A página marcada não exibe o link de retorno antes do formulário.
- Nenhuma tela de login criada pelo tema. Confira o comportamento e a entrega também em uma janela anônima; o processamento e as proteções contra abuso pertencem ao Blogger.

A ativação usa CSS `:has()`, já empregado na busca do tema, nos navegadores atuais. O formulário precisa do JavaScript e dos dados de sessão nativos que o Blogger injeta para o gadget `ContactForm1`. O tema não copia essa biblioteca, não implementa um serviço de e-mail e não exige API key ou senha. Não remova o JavaScript padrão da plataforma. [Estrutura dos widgets](https://support.google.com/blogger/answer/46888?hl=pt-BR) · [Orientação sobre gadgets](https://support.google.com/blogger/answer/176245?hl=pt-BR).

## Desativar ou usar outro canal

Remova a classe `balaio-contact-page` do conteúdo: o formulário volta a ficar oculto. Você pode manter a página com seus próprios canais ou outro formulário configurado separadamente. Não adicione um segundo `ContactForm1` e não mova o gadget para a lateral legada.

A classe só deve ser usada em **Páginas**, não em posts. O widget é renderizado apenas em páginas estáticas; não é incluído na home nem em posts individuais. Páginas sem a classe mantêm o formulário oculto.

## Atualizar da rc.11/rc.12 ou de uma edição manual

Baixe o XML completo da main e atualize o tema. Na página Contato já existente, substitua a referência antiga pelo trecho acima. Não cole `<b:section>` ou `<b:widget>` no editor da página; esses elementos agora vêm no XML do repositório.

A rc.13 declara o `ContactForm1` completo na seção `contactpage`, fora de `sidebar`, sem condição por domínio/endereço. Se **Restaurar** preservar uma posição, condição ou corpo antigo do gadget, use **Tema → Editar HTML**, substitua o editor pelo XML completo atual e salve. Depois confira `balaio-version` como `0.2.0-rc.13`, a página pública e um envio real. Não reimporte posts para corrigir a apresentação.

## Dados e validação

O Blogger processa o e-mail e a mensagem para encaminhar o contato aos responsáveis pelo blog. Ajuste sua política de privacidade à configuração real; o exemplo de privacidade do repositório não substitui essa informação.

Os exemplos locais desativam o envio e não carregam o transporte Google. Eles conferem visual e ativação, não a entrega de e-mail. A importação e a entrega desta candidata ainda precisam de confirmação no Blogger. [Evidências e limites](VALIDATION.md).

Código próprio e exemplos são MIT; Inter/Newsreader mantêm SIL OFL. O Blogger é um serviço externo com seus próprios termos.
