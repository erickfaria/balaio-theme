# Balaio Theme

Tema open source para Blogger, voltado a blogs pessoais, divulgação científica e compartilhamento de conhecimento. Código próprio sob licença MIT, com uma direção editorial minimalista: tipografia confortável, espaço em branco, destaque para conteúdo e navegação simples.

**Estado: primeira base experimental.** O XML pode ser verificado localmente, mas ainda não foi importado nem validado no Blogger. Não use diretamente no blog de produção.

## Instalação para teste

1. Crie um blog de teste no Blogger e adicione algumas postagens e uma página.
2. Faça backup do tema atual em **Tema → menu → Fazer backup**.
3. Em **Tema → Editar HTML**, substitua o conteúdo por `theme/balaio.xml` e salve.
4. Em **Layout**, configure o gadget **Menu** com links de páginas ou marcadores; o link Início já vem no tema.
5. Configure título e descrição nas configurações do blog. Acrescente gadgets na lateral e no rodapé.
6. Confira a lista de verificação em [docs/ROADMAP.md](docs/ROADMAP.md) antes de usar em produção.

## Primeira implementação

- Home com três cards de abertura e lista editorial, sem duplicar publicações.
- Artigos e páginas com coluna de leitura, imagens fluidas, tabelas e blocos de código com rolagem.
- Busca nativa, marcadores, paginação e link para comentar.
- Lista básica de comentários; formulário incorporado e respostas encadeadas ainda pendentes.
- Cabeçalho textual, menu de links, lateral e rodapé editáveis pelo Layout.
- Layout responsivo, navegação por teclado, link para pular ao conteúdo e estilo para impressão.
- Inter e Newsreader via Google Fonts, com fallback local; nenhuma biblioteca JavaScript.

Os textos de interface desta versão estão em português. Para mudar cores e largura, edite as propriedades CSS em `:root` no XML. O texto de abertura pode ser editado no gadget **Apresentação**, em **Layout**. Preserve uma única tag `<h1>` na abertura. A configuração visual pelo Designer de temas e a imagem de logo ainda não estão implementadas.

## Desenvolvimento

```sh
python3 scripts/validate_theme.py
python3 -m unittest discover -s tests -v
python3 scripts/build_preview.py
python3 -m http.server 8765 --bind 127.0.0.1 --directory preview
```

Abra `http://127.0.0.1:8765` para ver home, artigo e busca sem resultados. As páginas usam o CSS extraído do XML e conteúdo fictício; não compilam tags do Blogger. Os HTML gerados ficam fora do Git.

O validador usa somente a biblioteca padrão do Python. Verifica XML, estrutura de seções e referências aos blocos locais; não substitui o compilador do Blogger nem um teste visual. Veja [a direção visual](docs/DESIGN.md), [o plano de desenvolvimento](docs/ROADMAP.md) e [a origem e política de recursos](docs/PROVENANCE.md).

## Licença e referências

O código original deste projeto usa a [licença MIT](LICENSE). Backups e conteúdos privados não integram a distribuição. Recursos de terceiros exigem licença e origem documentadas antes de entrar nos commits. Veja [docs/PROVENANCE.md](docs/PROVENANCE.md).

## Estrutura do repositório

| Caminho | Conteúdo |
| --- | --- |
| `theme/balaio.xml` | Tema para instalar no Blogger e CSS principal |
| `scripts/` | Validador e gerador de prévia, sem dependências Python externas |
| `tests/` | Verificações estruturais do validador |
| `docs/` | Direção visual, personalização, origem e validação |
| `licenses/` | Avisos das fontes de terceiros |
| `.github/` | CI e modelos de issues e pull requests |
| `preview/` | Arquivos gerados localmente, ignorados pelo Git |

Se tiver `make` instalado, `make check` roda as verificações e `make serve` gera e abre o servidor local.

Para contribuir, veja [CONTRIBUTING.md](CONTRIBUTING.md). Mudanças são registradas em [CHANGELOG.md](CHANGELOG.md). A automação executa os checks em pushes e pull requests; seu sucesso não confirma compatibilidade com o Blogger.

## Fontes e personalização

Inter atende menu, busca e interface; Newsreader atende títulos e texto longo. As duas famílias usam SIL OFL 1.1, com avisos em `licenses/`. O código Balaio continua MIT. Veja [docs/CUSTOMIZATION.md](docs/CUSTOMIZATION.md) para cores, fontes, cards e gadgets.
