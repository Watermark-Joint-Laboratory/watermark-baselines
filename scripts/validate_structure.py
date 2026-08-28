from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT = {
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "baselines",
    "common",
    "configs",
    "experiments",
    "docs",
}
REQUIRED_BASELINE_FILES = {"README.md", "upstream.md", "upstream.json", "requirements.txt"}
REQUIRED_BASELINE_DIRS = {"configs", "scripts", "src"}


def main() -> int:
    errors: list[str] = []

    for name in sorted(REQUIRED_ROOT):
        if not (ROOT / name).exists():
            errors.append(f"missing root entry: {name}")

    baseline_root = ROOT / "baselines"
    if baseline_root.exists():
        for method in sorted(baseline_root.iterdir()):
            if not method.is_dir() or method.name.startswith("."):
                continue
            for name in sorted(REQUIRED_BASELINE_FILES):
                if not (method / name).is_file():
                    errors.append(f"{method.relative_to(ROOT)}: missing file {name}")
            for name in sorted(REQUIRED_BASELINE_DIRS):
                if not (method / name).is_dir():
                    errors.append(f"{method.relative_to(ROOT)}: missing directory {name}/")

    if errors:
        print("Repository validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Repository structure is valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
