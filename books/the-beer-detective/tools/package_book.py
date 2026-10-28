#!/usr/bin/env python3
"""Package the complete book project, excluding caches and nested archives."""
from pathlib import Path
import argparse
import hashlib
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist/the-beer-detective-project.zip')
    args = parser.parse_args()
    files = [path for path in sorted(ROOT.rglob('*')) if path.is_file()
             and not any(part.startswith('.') or part == '__pycache__' for part in path.relative_to(ROOT).parts)
             and path.suffix not in {'.zip', '.pyc'} and path.name != 'SHA256SUMS']
    sums = '\n'.join(f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT).as_posix()}' for path in files) + '\n'
    checksum_file = ROOT / 'SHA256SUMS'
    checksum_file.write_text(sums)
    files.append(checksum_file)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(args.output, 'w', zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            name = 'the-beer-detective/' + path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(name, (2026, 10, 28, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, path.read_bytes())
    print(f'{args.output}: {len(files)} files, {args.output.stat().st_size:,} bytes')


if __name__ == '__main__':
    main()
