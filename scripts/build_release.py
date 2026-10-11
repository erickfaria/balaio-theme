#!/usr/bin/env python3
"""Build install assets from a clean, committed checkout using an allowlist."""
import argparse
import hashlib
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ROOT_FILES = {'LICENSE', 'VERSION', 'README.md', 'README.pt-BR.md', 'CHANGELOG.md', 'CONTRIBUTING.md'}
DIRECTORIES = {'theme': '.xml', 'docs': '.md', 'examples': '.html', 'licenses': '.txt'}


def build(output):
    subprocess.run(['git', 'diff', '--quiet', 'HEAD'], cwd=ROOT, check=True)
    version = (ROOT / 'VERSION').read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[a-z0-9.]+)?', version):
        raise ValueError('VERSION must be a supported semantic version.')
    paths = subprocess.check_output(['git', 'ls-files', '-z'], cwd=ROOT).decode().split('\0')
    included = []
    for name in paths:
        if not name:
            continue
        path = Path(name)
        if name in ROOT_FILES or (path.parts[0] in DIRECTORIES and path.suffix == DIRECTORIES[path.parts[0]]):
            if (ROOT / path).is_symlink():
                raise ValueError(f'Release source must not be a symlink: {name}')
            included.append(name)
    required = ROOT_FILES | {'theme/balaio.xml', 'theme/balaio.en.xml',
                             'licenses/inter-OFL.txt', 'licenses/newsreader-OFL.txt',
                             'docs/RELEASE.md', 'docs/en/RELEASE.md'}
    if required - set(included):
        raise ValueError(f'Missing tracked package files: {sorted(required - set(included))}')
    output.mkdir(parents=True, exist_ok=True)
    prefix = f'balaio-{version}'
    archive = output / f'{prefix}.zip'
    with zipfile.ZipFile(archive, 'w', compression=zipfile.ZIP_DEFLATED) as bundle:
        for name in sorted(included):
            entry = zipfile.ZipInfo(f'{prefix}/{name}', date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, (ROOT / name).read_bytes())
    assets = [archive]
    for name in ('balaio.xml', 'balaio.en.xml'):
        target = output / name
        target.write_bytes((ROOT / 'theme' / name).read_bytes())
        assets.append(target)
    checksums = '\n'.join(f'{hashlib.sha256(asset.read_bytes()).hexdigest()}  {asset.name}' for asset in assets)
    (output / 'SHA256SUMS.txt').write_text(checksums + '\n', encoding='utf-8')
    print(f'Built {len(included)} package files and checksums in {output}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist')
    args = parser.parse_args()
    build(args.output.resolve())
