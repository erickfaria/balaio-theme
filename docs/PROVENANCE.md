# Autoria e política de recursos

[English](en/PROVENANCE.md) · [Português](PROVENANCE.md)

## Implementação Balaio

O Balaio é um tema independente para Blogger, com código original sob licença MIT. A direção visual está documentada em [DESIGN.md](DESIGN.md).

`theme/balaio.xml` foi escrito para este projeto. A base não incorpora bibliotecas JavaScript, imagens ou ícones de terceiros. As fontes abertas são carregadas via Google Fonts; seus arquivos binários não estão incluídos no repositório.

Imagens e textos de posts são fornecidos pelo blog que instalar o tema; seus direitos não são transferidos nem cobertos pela licença MIT do código.

## Inclusão de recursos

Para qualquer recurso futuro de terceiros, registrar antes da inclusão: origem, autor, versão, licença, atribuição exigida e arquivo incorporado. Recursos sem permissão verificável de redistribuição devem ser substituídos por alternativas próprias. A licença MIT deste repositório não substitui licenças de terceiros.

Backups, credenciais e conteúdos privados não fazem parte da distribuição e devem permanecer fora dos commits.

## Documentação técnica consultada

- [Elementos de página e seções](https://support.google.com/blogger/answer/46888?hl=en)
- [Dados de layouts](https://support.google.com/blogger/answer/47270?hl=en)
- [Tags de widgets](https://support.google.com/blogger/answer/46995?hl=en)

Estas páginas documentam a estrutura do Blogger; não são fontes do código ou de recursos visuais do tema.

## Fontes abertas

| Família | Autoria e origem | Uso | Licença local |
| --- | --- | --- | --- |
| Inter | [The Inter Project Authors](https://github.com/rsms/inter) | Interface e identidade textual | [SIL OFL 1.1](../licenses/inter-OFL.txt) |
| Newsreader | [The Newsreader Project Authors / Production Type](https://github.com/productiontype/Newsreader) | Títulos e leitura | [SIL OFL 1.1](../licenses/newsreader-OFL.txt) |

Avisos copiados do [repositório oficial Google Fonts](https://github.com/google/fonts/tree/main/ofl) em 11/10/2026, preservados integralmente. As famílias são utilizadas sem modificação. O template usa a API CSS do Google Fonts com `display=swap` e fallback do sistema. A licença MIT do código não altera a licença das fontes.

## Inventário de licenças dos recursos

| Recurso distribuído ou solicitado | Origem | Licença |
| --- | --- | --- |
| XML, CSS, Python, documentação e exemplos HTML | Implementação própria Balaio | [MIT](../LICENSE) |
| Paleta pastel e regras de layout | Valores próprios do CSS, editáveis em `:root` | MIT como parte do código |
| SVG geométrico da prévia | Gerado pelo nosso script | MIT |
| Inter e Newsreader | Projetos de fontes listados acima | Seus avisos SIL OFL 1.1 |
| Placeholders Lorem ipsum das páginas | Exemplos editáveis incluídos | MIT como parte dos exemplos |

Não distribuímos fontes compradas, fotos de banco proprietário, ícones proprietários ou código de temas terceiros. As requisições padrão carregam fontes OFL via Google Fonts; a hospedagem é opcional e pode ser substituída por hospedagem própria ou fontes genéricas do dispositivo. A disponibilidade e licença das fontes do dispositivo pertencem a ele, não ao repositório. O Blogger é uma plataforma externa, não distribuída ou licenciada pelo projeto.

Todos os recursos incluídos permitem reutilização e modificação sob suas respectivas licenças. Preserve avisos MIT e OFL ao redistribuir os códigos ou fontes correspondentes. O [guia de personalização](CUSTOMIZATION.md) explica como remover requisições externas de fontes.

## Contato — rc.12

A rc.12 distribui apenas o modelo textual de Contato e guias de configuração manual, sob MIT. A integração nativa experimental da rc.11 e seus estilos foram removidos. Nenhuma biblioteca de envio é copiada ou distribuída. Serviços usados por quem configurar um formulário ficam sob seus próprios termos. [Referência](CONTACT.md).
