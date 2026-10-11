# Contributing to Balaio

[English](#english) · [Português](#português)

## English

Bug fixes, accessibility improvements and suggestions are welcome. Original project code is MIT; fonts and third-party resources keep their own licenses. By contributing original code, you agree to distribute it under the project's MIT license.

1. Create a branch for your change.
2. Edit `theme/balaio.xml`, the Portuguese source. CSS is in `b:skin`, with colors and fonts in `:root`.
3. Run `python3 scripts/build_locales.py` after changing the source; do not edit the English XML directly.
4. Run the checks and rebuild the preview:

```sh
make check
make preview
```

Without Make, run the Python commands listed in [README.md](README.md). Python 3.10+ is required, with no external packages.

5. Examine phone, tablet and desktop layouts. For widget or expression changes, also import into a separate test Blogger blog and record the outcome.
6. Submit a concise description of the issue, result and validation. Keep both language guides aligned.

Do not commit generated `preview/`, credentials, private content or backups. The preview uses real CSS and sample markup; it is not a Blogger compiler.

Follow [docs/en/DESIGN.md](docs/en/DESIGN.md). Document third-party resources, authorship, license and attribution in the provenance guides and preserve required notices. Do not add resources without verified redistribution permission. Explain any new dependencies or external services. Reading, navigation and search must work without theme JavaScript.

## Português


Correções, melhorias de acessibilidade e sugestões são bem-vindas. O código do projeto está sob MIT; fontes e eventuais recursos de terceiros preservam suas próprias licenças.

## Trabalhar no tema

Ao contribuir com código original, você concorda em distribuí-lo sob a licença MIT do projeto.

1. Crie uma branch para a mudança.
2. Edite `theme/balaio.xml`, a fonte principal do tema. O CSS está em `b:skin`, organizado por regras, com cores e famílias de fonte em `:root`.
3. Após editar o XML fonte português, rode `python3 scripts/build_locales.py`. Não edite a variante inglesa diretamente. Rode as verificações locais:

```sh
python3 scripts/build_locales.py --check
python3 scripts/validate_docs.py
python3 scripts/validate_theme.py
python3 -m unittest discover -s tests -v
python3 scripts/build_preview.py
git diff --check
```

4. Examine a prévia em celular e desktop. Quando alterar widgets ou expressões, teste também num Blogger separado e registre o resultado.
5. Envie uma descrição curta do problema, da mudança e do que foi verificado.

Não inclua `preview/`, backups, credenciais ou conteúdo privado. O gerador de prévia usa CSS real com marcação fictícia; mantenha a estrutura de demonstração coerente com o XML, sem tratá-la como compilador do Blogger.

## Recursos e identidade

Siga [docs/DESIGN.md](docs/DESIGN.md). Código e gráficos novos devem ter autoria ou origem documentadas. Para incluir fontes, imagens ou dependências, registre licença e atribuição em `docs/PROVENANCE.md` e preserve os avisos necessários. Não inclua recursos sem permissão de redistribuição verificável.

Não acrescente dependências ou serviços externos sem explicar sua utilidade. Leitura, navegação e busca precisam funcionar sem JavaScript do tema.
