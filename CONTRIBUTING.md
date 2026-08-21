# 贡献指南

## 分支与提交

- 新方法：`baseline/<method>`
- 修复：`fix/<short-description>`
- 实验：`experiment/<dataset-or-topic>`
- 文档：`docs/<short-description>`

建议使用 Conventional Commits，例如 `feat: add KGW reproduction`。禁止直接向 `main` 推送，所有变更通过 Pull Request 合并。

## Baseline 准入要求

每个 `baselines/<method>/` 至少包含：

- `README.md`：方法、环境、数据、命令、参数、结果和已知问题。
- `upstream.md`：论文、官方仓库、固定 commit、获取日期、许可证与本地修改。
- `requirements.txt` 或其他可复现环境文件。
- `configs/`：论文默认配置和组内正式实验配置。
- `scripts/`：可直接执行的生成、检测或评估入口。
- `src/`：方法实现或经过允许的本地修改。

## Pull Request 检查

- [ ] 上游许可证允许当前使用方式。
- [ ] 未提交密钥、访问令牌、个人路径、模型权重或完整数据集。
- [ ] README 中的安装和运行命令已在干净环境验证。
- [ ] 参数与论文或固定上游版本一致。
- [ ] 结果记录包含 Git commit、配置、随机种子和环境。
- [ ] `python scripts/validate_structure.py` 通过。
- [ ] 至少一位非作者组员完成复核。

## 公共代码原则

第一阶段优先保留各方法的可运行版本。只有同一能力被三个或以上方法稳定复用时，才移动到 `common/`；抽取时必须保留原行为测试。
