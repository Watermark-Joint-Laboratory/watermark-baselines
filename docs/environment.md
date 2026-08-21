# Environment Policy

每个 Baseline 优先维护独立环境，避免不同官方实现的依赖冲突。

至少记录：

- 操作系统与架构
- Python、PyTorch、Transformers 和 CUDA 版本
- GPU 型号与数量
- 完整依赖锁定方式
- 必需环境变量的名称（不得提交值）
- 安装和最小 smoke test 命令

环境确认可复现后再固定精确版本。若使用 Conda、uv、Poetry 或容器，保留其原生锁文件，不要同时维护多套互相矛盾的依赖定义。
