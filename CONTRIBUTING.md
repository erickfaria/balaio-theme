# Contribuir com o Balaio

Correções, melhorias de acessibilidade e sugestões são bem-vindas. O código do projeto está sob MIT; fontes e eventuais recursos de terceiros preservam suas próprias licenças.

## Trabalhar no tema

1. Crie uma branch para a mudança.
2. Edite `theme/balaio.xml`, a fonte principal do tema. O CSS está em `b:skin`, organizado por regras, com cores e famílias de fonte em `:root`.
3. Rode as verificações locais:

```sh
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
