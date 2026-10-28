#!/usr/bin/env python3
"""Create a deterministic complete publishing bundle without research caches."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "100-things-beer-teaches-us-publishing-bundle.zip"
EXCLUDED = {".build", "__pycache__", ".venv", ".git"}
files = sorted(p for p in ROOT.rglob("*") if p.is_file()
               and p != DEST and not any(part in EXCLUDED for part in p.relative_to(ROOT).parts)
               and p.suffix != ".pyc")
with zipfile.ZipFile(DEST, "w") as archive:
    for file in files:
        name = "100-things-beer/" + file.relative_to(ROOT).as_posix()
        info = zipfile.ZipInfo(name, (2026, 10, 28, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, file.read_bytes())
print(f"{DEST.name}: {len(files)} files; {DEST.stat().st_size:,} bytes")
