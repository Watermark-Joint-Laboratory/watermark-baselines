# SWEET

## Method information

- Paper: [Who Wrote this Code? Watermarking for Code Generation](https://arxiv.org/abs/2305.15060)
- Venue: ACL 2024
- Scope: 低熵代码生成的选择性水印
- Official repository: https://github.com/hongcheki/sweet-watermark
- Fixed commit: `853b47eb064c180beebd383302d09491fc98a565`
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
python scripts/fetch_upstream.py sweet
```

### Upstream commands to verify

```bash
cd baselines/sweet/src/upstream
# Select a model-specific script documented in the upstream README
bash scripts/main/run_{MODEL}_generation.sh
bash scripts/main/run_{MODEL}_detection.sh
```

The fetch command checks out an immutable commit under `src/upstream/`. That directory is ignored by Git so unlicensed upstream code is not accidentally redistributed.

## Results

No result is marked reproduced yet. Record model revision, dataset revision, config, seed, hardware and output location before updating the status table.

## Citation

```bibtex
@inproceedings{lee2024sweet,\n  title={Who Wrote this Code? Watermarking for Code Generation},\n  author={Lee, Taehyun and Hong, Seokhee and Ahn, Jaewoo and others},\n  booktitle={ACL},\n  year={2024}\n}
```
