# Maintenance and pull request policy / Política de manutenção

## English

Balaio welcomes public contributions through forks and pull requests. **@erickfaria** is the sole code owner for all files, including `.github/CODEOWNERS` and workflow/ruleset definitions. Other users may leave feedback; their reviews do not replace the maintainer's required approval.

For contributors other than the owner, the protected `main` branch requires a pull request, successful `validate` checks from GitHub Actions, an up-to-date branch, resolved review conversations and squash merges. Direct pushes are blocked for contributors. Force-pushes and branch deletion are blocked for everyone, including the owner. New reviewable commits invalidate previous approvals. Only the owner can integrate changes.

**Owner exception:** only `@erickfaria` has an `always` bypass in the workflow and ownership rulesets. The owner can push directly and merge without approving reviews or successful CI. The separate history ruleset has no bypass: force-push, deletion of `main` and non-linear history remain blocked. This is the owner's explicitly chosen balance. Repository-wide squash merge settings are unchanged. GitHub Actions is enabled for PRs, main pushes, version tags and manual runs. PRs and local checks remain recommended.

During the pause, the configured `validate` status requirement remains in the ruleset but cannot run. Only the owner can integrate reviewed changes using the existing owner bypass after local validation. Resuming Actions requires an explicit owner decision; merely pushing a commit will not start it.

Repository administrator access is unchanged: the owner can edit repository settings and rulesets. Retaining history safeguards does not transfer ownership or remove administration rights.

Ruleset payloads in [.github/rulesets/main-safety.json](.github/rulesets/main-safety.json) , [.github/rulesets/main-workflow.json](.github/rulesets/main-workflow.json) and [.github/rulesets/main-owner.json](.github/rulesets/main-owner.json) record the configured policy. They are snapshots; editing them alone does not update GitHub. Administrators must apply changes through repository Settings or the REST API and verify the active rules.

When enabled, Actions use read-only workflow tokens and cannot approve PRs. Workflow runs from all external contributors require approval. Issues remain enabled; unused Wiki/Projects tabs are disabled. Only squash merges are enabled, auto-merge is disabled, and merged working branches are deleted automatically.

The released theme and its licenses are unchanged by repository governance. Follow [CONTRIBUTING.md](CONTRIBUTING.md) for development checks.

## Português

Contribuições públicas são bem-vindas por forks e pull requests. **@erickfaria** é o único CODEOWNER de todos os arquivos, inclusive `.github/CODEOWNERS`, workflows e definições de regras. Outras pessoas podem comentar e revisar, mas sua aprovação não substitui a aprovação obrigatória do mantenedor.

Para contribuidores que não sejam o proprietário, a `main` protegida exige PR, check `validate` aprovado pelo GitHub Actions, branch atualizada, conversas resolvidas e squash merge. Push direto é bloqueado para contribuidores. Force-push e exclusão da branch são bloqueados para todos, inclusive o proprietário. Novos commits revisáveis invalidam aprovações anteriores. Somente o proprietário pode integrar mudanças.

**Exceção do proprietário:** somente `@erickfaria` tem bypass `always` nas camadas de fluxo e autoria. O proprietário pode fazer push direto e merge sem revisão ou CI aprovado. A camada separada de histórico não tem exceção: force-push, exclusão da `main` e histórico não linear continuam bloqueados. Esse é o equilíbrio escolhido explicitamente pelo proprietário. As configurações globais de squash merge permanecem iguais. O GitHub Actions está ativo para PRs, pushes na main, tags e execuções manuais. PRs e checks locais continuam recomendados.

Durante a pausa, a exigência configurada do check `validate` continua na regra, mas não pode executar. Somente o proprietário pode integrar mudanças revisadas com o bypass existente após validação local. Retomar o Actions exige decisão explícita do proprietário; um push por si só não inicia execução.

O acesso de administrador permanece igual: o proprietário pode editar configurações e regras. Manter proteções de histórico não transfere a propriedade nem retira direitos de administração.

Os arquivos [.github/rulesets/main-safety.json](.github/rulesets/main-safety.json) , [.github/rulesets/main-workflow.json](.github/rulesets/main-workflow.json) e [.github/rulesets/main-owner.json](.github/rulesets/main-owner.json) registram a configuração. São snapshots: editar o JSON sozinho não altera o GitHub. Aplique alterações pelas configurações ou API e confira as regras ativas.

Quando habilitado, o Actions usa tokens somente de leitura e não pode aprovar PRs. Workflows de todos os contribuidores externos precisam de aprovação. Issues continuam habilitadas; abas Wiki/Projects sem uso ficam desabilitadas. Só squash merge está habilitado, auto-merge está desligado e branches de trabalho mescladas são excluídas automaticamente.

A governança não altera o tema publicado nem suas licenças. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para os checks de desenvolvimento.
