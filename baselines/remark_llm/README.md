# REMARK-LLM

## Method information

- Paper: [REMARK-LLM: A Robust and Efficient Watermarking Framework for Generative Large Language Models](https://arxiv.org/abs/2310.12362)
- Venue: USENIX Security 2024
- Scope: 学习式多比特编码与解码
- Official repository: https://github.com/ruisizhang123/REMARK-LLM
- Fixed commit: `777ccb3b67fb937c276431fa3bd980813b641a21`
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
python scripts/fetch_upstream.py remark_llm
```

### Upstream commands to verify

```bash
cd baselines/remark_llm/src/upstream
pip install -r ../../requirements.txt
bash bash/run.sh train
bash bash/run.sh val
```

The fetch command checks out an immutable commit under `src/upstream/`. That directory is ignored by Git so unlicensed upstream code is not accidentally redistributed.

## Results

No result is marked reproduced yet. Record model revision, dataset revision, config, seed, hardware and output location before updating the status table.

## Citation

```bibtex
@inproceedings{zhang2024remark,\n  title={REMARK-LLM: A Robust and Efficient Watermarking Framework for Generative Large Language Models},\n  author={Zhang, Ruisi and Hussain, Shehzeen Samarah and Neekhara, Paarth and Koushanfar, Farinaz},\n  booktitle={USENIX Security},\n  year={2024}\n}
```
