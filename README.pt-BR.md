# Balaio Theme

**[English](README.md) · [Português brasileiro](README.pt-BR.md)**

Tema **Blogger** gratuito, livre, open source e responsivo para blogs pessoais, divulgação científica e compartilhamento de conhecimento. Design editorial próprio, com espaço para o conteúdo, cores suaves e tipografia confortável.

**Licença MIT.** Você pode usar, modificar e redistribuir o código, inclusive em projetos comerciais. Preserve os avisos de autoria e licença nas cópias ou partes substanciais do código. A MIT não exige crédito visível no site nem autorização paga. O software é fornecido sem garantia. [Leia a licença](LICENSE) · [MIT na Open Source Initiative](https://opensource.org/license/mit).

> **Estado:** experimental. As verificações locais de XML e de layout da prévia passaram; a importação e o funcionamento dos gadgets no Blogger ainda não foram confirmados. Use primeiro em um blog de teste. Ainda não há versão estável publicada.

## Escolha o idioma

| Interface | Arquivo |
| --- | --- |
| Português brasileiro | [theme/balaio.xml](theme/balaio.xml) |
| Inglês | [theme/balaio.en.xml](theme/balaio.en.xml) |

Configure o idioma do blog no Blogger de acordo com a interface escolhida. O tema não traduz o conteúdo das suas publicações.

## Instalar no Blogger

Não precisa compilar nem instalar ferramentas para usar o tema.

1. Baixe o ZIP do repositório em **Code → Download ZIP** e extraia, ou baixe o XML desejado pela opção **Raw / Download raw file** do GitHub.
2. Escolha um **blog de teste** no Blogger. Faça backup do tema atual em **Tema → menu → Fazer backup**.
3. Abra **Tema → menu → Editar HTML**. Substitua o conteúdo do editor pelo XML completo e salve.
4. Configure título, descrição e idioma em **Configurações**.
5. Em **Layout**, edite **Menu** com links de páginas ou marcadores. Início já vem no código.
6. Edite **Apresentação** (português) ou **Introduction** (inglês) para mudar a abertura. Configure os gadgets de marcadores, lateral e rodapé.
7. Confira artigos, páginas, busca, paginação e comentários no celular e no computador antes de usar no blog principal.

[Instalação e solução de problemas](docs/INSTALLATION.md) · [Personalização](docs/CUSTOMIZATION.md)

## Recursos

- Três cards de abertura na home, seguidos da lista editorial sem repetir posts.
- Layout responsivo para celulares, tablets e computadores; miniaturas opcionais e entradas com largura completa quando não há imagem.
- Busca nativa, marcadores, paginação, artigos e páginas estáticas.
- Comentários básicos e link para comentar; formulário incorporado e respostas encadeadas ainda pendentes.
- Apresentação, menu, lateral e rodapé editáveis por gadgets.
- Foco de teclado, link para pular ao conteúdo, rolagem contida em código/tabelas e estilos para impressão.
- **Inter** para interface e **Newsreader** para títulos e leitura, via Google Fonts com fallback local e `display=swap`. Ambas usam SIL OFL 1.1; suas licenças são separadas da MIT.
- Sem JavaScript do tema ou dependências externas de pacotes Python.

Logo em imagem, controles do Designer de temas e layout específico de 404 ainda não estão implementados. A prévia usa o CSS real com conteúdo de exemplo; não compila expressões do Blogger.

## Desenvolvimento local

Requer Python 3.10+; `make` é opcional.

```sh
python3 scripts/validate_docs.py
python3 scripts/build_locales.py --check
python3 scripts/validate_theme.py
python3 -m unittest discover -s tests -v
python3 scripts/build_preview.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory preview
```

Abra `http://127.0.0.1:8765`. Encerre o servidor com Ctrl+C. Com Make instalado, use `make check` e `make serve`. Após editar o XML português, rode `make locales` ou `python3 scripts/build_locales.py` para atualizar a versão inglesa.

## Organização

| Caminho | Conteúdo |
| --- | --- |
| `theme/` | XMLs instaláveis; português é a fonte da variante inglesa |
| `scripts/` | Geração de idioma, validação e prévia |
| `tests/` | Verificações do validador |
| `docs/` / `docs/en/` | Guias e notas em português / inglês |
| `licenses/` | Avisos originais das fontes |
| `.github/` | CI e modelos de issue e PR |
| `preview/` | Arquivos locais gerados, ignorados pelo Git |

[Contribuir](CONTRIBUTING.md) · [Histórico](CHANGELOG.md) · [Design](docs/DESIGN.md) · [Plano](docs/ROADMAP.md) · [Validação](docs/VALIDATION.md) · [Autoria e licenças](docs/PROVENANCE.md)

Backups, credenciais e conteúdo privado não integram a distribuição. Fontes mantêm a licença OFL; posts e imagens têm direitos próprios. A automação do GitHub verifica os templates, as traduções e a geração da prévia; um check verde não confirma importação no Blogger.
