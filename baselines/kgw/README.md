# KGW

## Method information

- Paper: [A Watermark for Large Language Models](https://arxiv.org/abs/2301.10226)
- Venue: ICML 2023
- Scope: 自然语言生成与检测
- Official repository: https://github.com/jwkirchenbauer/lm-watermarking
- Fixed commit: `82922516930c02f8aa322765defdb5863d07a00e`
- License: Apache-2.0

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
python scripts/fetch_upstream.py kgw
```

### Upstream commands to verify

```bash
cd baselines/kgw/src/upstream
python demo_watermark.py
```

The fetch command checks out an immutable commit under `src/upstream/`. That directory is ignored by Git so unlicensed upstream code is not accidentally redistributed.

## Results

No result is marked reproduced yet. Record model revision, dataset revision, config, seed, hardware and output location before updating the status table.

## Citation

```bibtex
@inproceedings{kirchenbauer2023watermark,
  title={A Watermark for Large Language Models},
  author={Kirchenbauer, John and Geiping, Jonas and Wen, Yuxin and Katz, Jonathan and Miers, Ian and Goldstein, Tom},
  booktitle={ICML},
  year={2023}
}
```
