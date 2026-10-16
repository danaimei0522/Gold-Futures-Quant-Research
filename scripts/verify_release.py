"""Check the public methods package without executing research code."""
import ast
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAYLOAD = {
    ".gitignore", "README.md", "METHODS.md", "STRATEGY_PSEUDOCODE.md",
    "DATA_REQUIREMENTS.md", "REPRODUCING.md", "CODE_PROVENANCE.md",
    "THIRD_PARTY_NOTICES.md", "CODE_ONLY_RELEASE_AUDIT.md",
    "scripts/verify_release.py",
}
# Audit record is separately allowlisted and hashed with the documents.
PAYLOAD.add("STATIC_CHECKS.md")


def verify():
    manifest = json.loads((ROOT / "release_manifest.json").read_text())
    assert set(manifest["files"]) == PAYLOAD, "Manifest inventory differs"
    found = set()
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if rel.parts[0] == ".git":
            continue
        assert not path.is_symlink(), f"Symlink: {rel}"
        if path.is_file():
            found.add(rel.as_posix())
    assert found == PAYLOAD | {"release_manifest.json"}, "Unexpected or missing file"
    patterns = [
        r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
        r"(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}",
        r"AKIA[A-Z0-9]{16}",
        r"/(?:Users|home)/[A-Za-z0-9_.-]+/",
        r"[A-Za-z0-9_.+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
    ]
    for name in sorted(PAYLOAD):
        path = ROOT / name
        content = path.read_bytes()
        assert hashlib.sha256(content).hexdigest() == manifest["files"][name], f"Hash mismatch: {name}"
        text = content.decode("utf-8")
        if path.suffix == ".py":
            ast.parse(text, filename=name)
        if name != "scripts/verify_release.py":
            for pattern in patterns:
                assert not re.search(pattern, text), f"Review sensitive content: {name}"
            assert not re.search(r"from\s+panda_|import\s+(?:panda_|numpy|pandas)", text), f"Platform source fragment: {name}"
        if path.suffix == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", text):
                if "://" in target or target.startswith("#"):
                    continue
                assert (path.parent / target.split("#")[0]).is_file(), f"Broken link: {name}"
    print("PASS: exact 12-file inventory, payload hashes, verifier syntax, relative links, limited sensitive-content and platform-import scans.")
    print("No strategy, platform connection, market data, backtest or order execution.")


if __name__ == "__main__":
    verify()
