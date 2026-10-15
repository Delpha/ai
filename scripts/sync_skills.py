#!/usr/bin/env python3
"""Copy the canonical skills/ into each provider plugin, or check that the copies are current."""
from pathlib import Path
import argparse
import shutil

ROOT = Path(__file__).resolve().parents[1]
PROVIDERS = ("claude", "codex", "cursor")


def tree(directory):
    if not directory.exists():
        return {}
    files = {}
    for path in sorted(directory.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlinks are not allowed: {path}")
        if path.is_file():
            files[path.relative_to(directory)] = path.read_bytes()
    return files


def sync(root=ROOT, check=False):
    expected = {path: data for path, data in tree(root / "skills").items() if len(path.parts) > 1}
    stale = []
    for provider in PROVIDERS:
        target = root / "providers" / provider / "plugin" / "skills"
        if tree(target) == expected:
            continue
        stale.append(str(target.relative_to(root)))
        if not check:
            shutil.rmtree(target, ignore_errors=True)
            for relative, data in expected.items():
                (target / relative).parent.mkdir(parents=True, exist_ok=True)
                (target / relative).write_bytes(data)
    if check and stale:
        raise ValueError(f"{', '.join(stale)} differ from skills/; run python3 scripts/sync_skills.py")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail instead of rewriting the copy")
    args = parser.parse_args()
    try:
        sync(check=args.check)
    except ValueError as error:
        parser.exit(1, f"{error}\n")
    print("Provider skills are in sync.")
