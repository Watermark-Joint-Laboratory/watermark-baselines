# METHOD_NAME

## 1. 方法信息

- Paper：TODO
- Venue：TODO
- Paper URL：TODO
- Official Code：TODO
- Original Commit：TODO
- Maintainer：TODO

## 2. 当前复现状态

- [ ] Environment
- [ ] Generation
- [ ] Detection
- [ ] HumanEval
- [ ] MBPP
- [ ] C4
- [ ] Robustness Attack
- [ ] Independent Review

## 3. 环境

- Python：TODO
- PyTorch：TODO
- Transformers：TODO
- CUDA：TODO
- GPU：TODO

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r baselines/METHOD_NAME/requirements.txt
```

## 4. 数据集与模型

记录下载方式、版本、校验值或数据快照 ID。不要提交完整数据集或模型权重。

## 5. 运行

### Generation

```bash
python baselines/METHOD_NAME/scripts/generate.py --config baselines/METHOD_NAME/configs/default.yaml
```

### Detection

```bash
python baselines/METHOD_NAME/scripts/detect.py --config baselines/METHOD_NAME/configs/default.yaml
```

### Evaluation

```bash
python baselines/METHOD_NAME/scripts/evaluate.py --config baselines/METHOD_NAME/configs/default.yaml
```

## 6. 关键参数

| Parameter | Paper default | Reproduction | Description |
|---|---:|---:|---|
| TODO | TODO | TODO | TODO |

## 7. 复现结果

| Dataset | Metric | Paper | Reproduction | Seed | Config |
|---|---|---:|---:|---:|---|
| TODO | TODO | TODO | TODO | TODO | TODO |

## 8. 与官方代码的修改

- TODO

## 9. 已知问题

- TODO

## 10. Citation

```bibtex
TODO
```
