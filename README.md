# Watermark Baselines

组内文本水印经典方法复现库。仓库保存可运行代码、固定配置、运行命令、上游版本与复现结果，使每项实验都可追溯、可复查、可继续扩展。

> 当前为仓库初始化版本。请先复制 `baselines/_template/`，再导入具体方法；不要直接修改模板。

## Baseline 总表

| Method | Paper | Venue | Generation | Detection | HumanEval | MBPP | C4 | Status |
|---|---|---|:---:|:---:|:---:|:---:|:---:|---|
| KGW | 待补充 | ICML 2023 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | Planned |
| EXP | 待补充 | 待补充 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | Planned |
| SWEET | 待补充 | 待补充 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | Planned |
| DBW | 待补充 | 待补充 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | Planned |
| REMARK-LLM | 待补充 | 待补充 | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ | Planned |

状态定义：`Planned` → `Importing` → `Reproduced` → `Stable`。只有在干净环境中按 README 成功运行并由另一位组员复核后，才能标记为 `Stable`。

## 仓库结构

```text
baselines/      各方法的独立代码、环境、配置和复现档案
common/         至少三个方法重复使用后再抽取的公共组件
configs/        跨方法共享的模型与数据集配置
experiments/    按数据集或研究问题组织的实验入口与记录
scripts/        仓库级辅助脚本与结构校验
docs/           状态、环境和复现记录
.github/        CI、Issue、PR 与代码所有者配置
```

## 添加一个方法

1. 从 `main` 创建 `baseline/<method>` 分支。
2. 将 `baselines/_template/` 复制为 `baselines/<method>/`。
3. 填写该目录的 `README.md` 和 `upstream.md`，再导入经过许可证检查的代码。
4. 不提交模型权重、完整数据集、密钥、缓存和大型实验输出。
5. 运行 `python scripts/validate_structure.py`。
6. 提交 Pull Request，并请另一位组员按复现清单验证。

详细要求见 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [docs/reproduction_notes.md](docs/reproduction_notes.md)。

## 数据与结果约定

- 原始数据集、模型权重和缓存保存在仓库外，通过配置记录路径或下载方式。
- 小型汇总结果可提交为 JSON/CSV/Markdown；大型输出放在组内对象存储，并在实验记录中保存不可变链接或版本号。
- 每次正式实验记录 Git commit、配置文件、随机种子、模型版本、数据版本和运行环境。

## 许可证

本仓库暂未声明统一许可证。每个 Baseline 必须在 `upstream.md` 中记录上游许可证；没有明确许可证的代码不得直接复制进本仓库。
