# Verificação local — 11/10/2026

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
- Quatro testes estruturais do validador passaram localmente. O workflow está preparado para repetir a validação no GitHub; ainda não foi executado lá.
