# Recommended Repository Settings

在 GitHub 的 **Settings → Rules → Rulesets** 中为默认分支创建规则：

- Ruleset name: `Protect main`
- Enforcement status: `Active`
- Target branches: Default branch
- Restrict deletions: Enabled
- Block force pushes: Enabled
- Require a pull request before merging: Enabled
- Required approvals: 1
- Dismiss stale pull request approvals when new commits are pushed: Enabled
- Require review from Code Owners: Enabled
- Require status checks to pass: 在首次工作流成功后选择 `structure`
- Require branches to be up to date before merging: Enabled

建议保留 squash merge；是否关闭 merge commit 和 rebase merge 由组内习惯决定。若 Organization 套餐不支持所选规则，请至少使用经典 Branch protection rule 实现 PR、review、status check 和禁止 force push。
