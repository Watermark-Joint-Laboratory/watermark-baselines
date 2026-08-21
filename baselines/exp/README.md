# EXP / EXP-Edit

## Method information

- Paper: [Robust Distortion-free Watermarks for Language Models](https://arxiv.org/abs/2307.15593)
- Venue: TMLR 2024
- Scope: 指数最小采样、生成与编辑鲁棒检测
- Official repository: https://github.com/jthickstun/watermark
- Fixed commit: `80d4ec8f4280da2a2cada03adfc8940593d1964c`
- License: Not declared; source is not redistributed

## Current status

- [x] Paper and official source searched
- [x] Upstream commit pinned
- [x] License checked
- [ ] Clean environment reproduced
- [ ] Generation reproduced
- [ ] Detection reproduced
- [ ] Benchmark results reviewed independently

## Obtain the implementation

```bash
python scripts/fetch_upstream.py exp
```

### Upstream commands to verify

```bash
cd baselines/exp/src/upstream
conda create --name exp-watermark --file requirements.txt
python demo/generate.py --model facebook/opt-1.3b --m 80 --key 42 > doc.txt
python demo/detect.py --tokenizer facebook/opt-1.3b --key 42 < doc.txt
```

The fetch command checks out an immutable commit under `src/upstream/`. That directory is ignored by Git so unlicensed upstream code is not accidentally redistributed.

## Results

No result is marked reproduced yet. Record model revision, dataset revision, config, seed, hardware and output location before updating the status table.

## Citation

```bibtex
@article{kuditipudi2024robust,\n  title={Robust Distortion-free Watermarks for Language Models},\n  author={Kuditipudi, Rohith and Thickstun, John and Hashimoto, Tatsunori and Liang, Percy},\n  journal={Transactions on Machine Learning Research},\n  year={2024}\n}
```
