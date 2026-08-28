# Watermark Baselines

[![Validate repository](https://github.com/Watermark-Joint-Laboratory/watermark-baselines/actions/workflows/validate.yml/badge.svg)](https://github.com/Watermark-Joint-Laboratory/watermark-baselines/actions/workflows/validate.yml)

组内文本水印经典方法复现库。本仓库统一记录论文、官方实现、固定上游版本、环境、运行命令和复现结果，使每项实验都可追溯、可复查、可继续扩展。

当前已登记 5 种方法：KGW、EXP / EXP-Edit、SWEET、DBW 和 REMARK-LLM。其中 4 种方法已固定官方仓库 commit，可按需获取；DBW 暂无公开官方实现。所有方法目前均未标记为已复现。

## 方法概览

| Method | Scope | Venue | Upstream | License | Status |
|---|---|---|---|---|---|
| [KGW](baselines/kgw/README.md) | 自然语言生成与检测 | ICML 2023 | [Pinned](baselines/kgw/upstream.md) | Apache-2.0 | Ready-to-fetch |
| [EXP / EXP-Edit](baselines/exp/README.md) | 无失真生成与编辑鲁棒检测 | TMLR 2024 | [Pinned](baselines/exp/upstream.md) | 未声明，不再分发源码 | Ready-to-fetch |
| [SWEET](baselines/sweet/README.md) | 低熵代码生成水印 | ACL 2024 | [Pinned](baselines/sweet/upstream.md) | 未声明，不再分发源码 | Ready-to-fetch |
| [DBW](baselines/dbw/README.md) | 熵感知动态偏置 | Pattern Recognition 2026 | [Unavailable](baselines/dbw/upstream.md) | N/A | Metadata-only |
| [REMARK-LLM](baselines/remark_llm/README.md) | 学习式多比特编码与解码 | USENIX Security 2024 | [Pinned](baselines/remark_llm/upstream.md) | 未声明，不再分发源码 | Ready-to-fetch |

状态含义：

- `Metadata-only`：只登记论文信息，尚无可获取的公开官方实现。
- `Ready-to-fetch`：已登记官方仓库并固定完整 commit，但尚未完成干净环境复现。
- `Reproduced`：生成、检测或评估流程已按记录成功运行。
- `Stable`：复现结果已由另一位组员独立复核。

详细进度见 [Baseline Status](docs/baseline_status.md)。

## 快速开始

克隆仓库并先运行结构检查：

```bash
git clone https://github.com/Watermark-Joint-Laboratory/watermark-baselines.git
cd watermark-baselines
python scripts/validate_structure.py
```

按方法获取固定的官方实现，例如 KGW：

```bash
python scripts/fetch_upstream.py kgw
```

可用参数为 `kgw`、`exp`、`sweet` 和 `remark_llm`。脚本会将官方仓库检出到 `baselines/<method>/src/upstream/`，切换到登记的不可变 commit，并校验实际 SHA。该目录已被 Git 忽略，不会被本仓库重新分发。

获取后请进入对应方法目录，按照其 README 创建独立环境并运行上游验证命令：

- [KGW 使用说明](baselines/kgw/README.md)
- [EXP / EXP-Edit 使用说明](baselines/exp/README.md)
- [SWEET 使用说明](baselines/sweet/README.md)
- [REMARK-LLM 使用说明](baselines/remark_llm/README.md)

DBW 当前仅保存论文元数据；在找到作者发布的官方代码和许可证前，不导入非官方实现。

## 仓库结构

```text
baselines/      各方法的元数据、独立环境、配置、脚本与复现档案
common/         至少被三种方法稳定复用后再抽取的公共组件
configs/        跨方法共享的模型与数据集配置
experiments/    按数据集或研究问题组织的实验入口与记录
scripts/        上游获取脚本与仓库结构校验
docs/           状态、环境、仓库设置和复现规范
.github/        CI、Issue、PR 与代码所有者配置
```

## 复现流程

1. 阅读方法目录中的 `README.md`、`upstream.md` 和 `upstream.json`。
2. 使用 `scripts/fetch_upstream.py` 获取固定版本，不直接复制许可证不明确的源码。
3. 按 [环境规范](docs/environment.md) 为该方法创建独立环境。
4. 先执行方法 README 中记录的最小上游验证命令，再接入统一实验。
5. 为正式实验记录 Git commit、配置、随机种子、模型版本、数据版本、硬件和输出位置。
6. 将小型汇总结果提交为 JSON、CSV 或 Markdown；大型输出存放在组内对象存储。
7. 更新 [复现记录](docs/reproduction_notes.md) 和 [状态表](docs/baseline_status.md)，并请另一位组员复核。

## 添加新方法

1. 从 `main` 创建 `baseline/<method>` 分支。
2. 将 `baselines/_template/` 复制为 `baselines/<method>/`，不要直接修改模板。
3. 填写方法 README、`upstream.md` 和 `upstream.json`，并完成许可证检查。
4. 不提交密钥、个人路径、模型权重、完整数据集、缓存或大型实验输出。
5. 运行 `python scripts/validate_structure.py`。
6. 提交 Pull Request，确保 `structure` 检查通过并由至少一位非作者组员审核。

完整准入要求和审查清单见 [贡献指南](CONTRIBUTING.md)。安全问题请按 [安全策略](SECURITY.md) 报告。

## 许可证与上游代码

本仓库暂未声明统一许可证。每个 Baseline 都必须单独记录其上游许可证和固定来源。只有 KGW 的已登记上游明确采用 Apache-2.0；EXP、SWEET 和 REMARK-LLM 的已登记官方仓库未声明许可证，因此本仓库只保存来源、commit 和获取脚本，不复制或重新分发其源码。