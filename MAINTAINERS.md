# Maintenance and pull request policy / Política de manutenção

## English

Balaio welcomes public contributions through forks and pull requests. **@erickfaria** is the sole code owner for all files, including `.github/CODEOWNERS` and workflow/ruleset definitions. Other users may leave feedback; their reviews do not replace the maintainer's required approval.

The protected `main` branch requires a pull request, successful `validate` checks from GitHub Actions, an up-to-date branch, resolved review conversations and squash merges. Direct pushes, force-pushes and branch deletion are blocked. New reviewable commits invalidate previous approvals. Only the owner can integrate changes.

GitHub does not allow approving your own PR. The owner therefore has a **pull-request-only bypass of the ownership/review ruleset**. It does not bypass the separate safety ruleset: CI, PRs, conversation resolution and history protections still apply. The owner can use the merge override in GitHub after reviewing their own changes and confirming checks. As repository owner, they can also edit settings; avoid broad or permanent bypasses.

Ruleset payloads in [.github/rulesets/main-safety.json](.github/rulesets/main-safety.json) and [.github/rulesets/main-owner.json](.github/rulesets/main-owner.json) record the configured policy. They are snapshots; editing them alone does not update GitHub. Administrators must apply changes through repository Settings or the REST API and verify the active rules.

Actions use read-only workflow tokens and cannot approve PRs. Workflow runs from all external contributors require approval. Issues remain enabled; unused Wiki/Projects tabs are disabled. Only squash merges are enabled, auto-merge is disabled, and merged working branches are deleted automatically.

The released theme and its licenses are unchanged by repository governance. Follow [CONTRIBUTING.md](CONTRIBUTING.md) for development checks.

## Português

Contribuições públicas são bem-vindas por forks e pull requests. **@erickfaria** é o único CODEOWNER de todos os arquivos, inclusive `.github/CODEOWNERS`, workflows e definições de regras. Outras pessoas podem comentar e revisar, mas sua aprovação não substitui a aprovação obrigatória do mantenedor.

A `main` protegida exige PR, check `validate` aprovado pelo GitHub Actions, branch atualizada, conversas resolvidas e squash merge. Push direto, force-push e exclusão da branch são bloqueados. Novos commits revisáveis invalidam aprovações anteriores. Somente o proprietário pode integrar mudanças.

O GitHub não permite aprovar o próprio PR. Por isso, o proprietário tem uma **exceção às regras de autoria/revisão somente no fluxo de PR**. Ela não ignora a camada separada de segurança: CI, PRs, conversas resolvidas e proteção do histórico continuam obrigatórios. O proprietário pode usar a opção de integração com exceção após revisar suas mudanças e conferir os checks. Como dono do repositório, também pode editar configurações; evite exceções amplas ou permanentes.

Os arquivos [.github/rulesets/main-safety.json](.github/rulesets/main-safety.json) e [.github/rulesets/main-owner.json](.github/rulesets/main-owner.json) registram a configuração. São snapshots: editar o JSON sozinho não altera o GitHub. Aplique alterações pelas configurações ou API e confira as regras ativas.

O Actions usa tokens somente de leitura e não pode aprovar PRs. Workflows de todos os contribuidores externos precisam de aprovação. Issues continuam habilitadas; abas Wiki/Projects sem uso ficam desabilitadas. Só squash merge está habilitado, auto-merge está desligado e branches de trabalho mescladas são excluídas automaticamente.

A governança não altera o tema publicado nem suas licenças. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para os checks de desenvolvimento.
