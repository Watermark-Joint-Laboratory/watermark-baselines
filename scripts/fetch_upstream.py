from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch one pinned official baseline repository.")
    parser.add_argument("baseline", help="Directory name below baselines/")
    args = parser.parse_args()

    baseline = (ROOT / "baselines" / args.baseline).resolve()
    baseline_root = (ROOT / "baselines").resolve()
    if baseline.parent != baseline_root or not baseline.is_dir():
        raise SystemExit(f"Unknown baseline: {args.baseline}")

    manifest_path = baseline / "upstream.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    repository = manifest.get("repository")
    commit = manifest.get("commit")

    if not repository or not commit:
        raise SystemExit(f"{args.baseline} has no public official implementation to fetch.")
    if not repository.startswith("https://github.com/") or not repository.endswith(".git"):
        raise SystemExit("Only explicit HTTPS GitHub repository URLs are accepted.")
    if not COMMIT_RE.fullmatch(commit):
        raise SystemExit("Pinned commit must be a full 40-character lowercase SHA.")

    destination = baseline / "src" / "upstream"
    if destination.exists():
        raise SystemExit(f"Refusing to overwrite existing checkout: {destination}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    run(["git", "clone", "--filter=blob:none", repository, str(destination)])
    run(["git", "-C", str(destination), "checkout", "--detach", commit])
    actual = subprocess.check_output(
        ["git", "-C", str(destination), "rev-parse", "HEAD"], text=True
    ).strip()
    if actual != commit:
        raise SystemExit(f"Commit verification failed: expected {commit}, got {actual}")

    print(f"Fetched {args.baseline} at {actual}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
