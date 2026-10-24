"""Install archives must include referenced examples and exclude development data."""
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


class ReleaseTests(unittest.TestCase):
    def test_install_package_is_complete_and_scoped(self):
        with tempfile.TemporaryDirectory() as folder:
            subprocess.run(['python3', 'scripts/build_release.py', '--output', folder],
                           cwd=ROOT, check=True, capture_output=True)
            archive = next(Path(folder).glob('*.zip'))
            with zipfile.ZipFile(archive) as bundle:
                names = {name.split('/', 1)[1] for name in bundle.namelist()}
                for required in ('theme/balaio.xml', 'theme/balaio.en.xml',
                                 'examples/material.pt-BR.md', 'examples/material.en.md',
                                 'docs/MATERIALS.md', 'docs/en/MATERIALS.md',
                                 'licenses/inter-OFL.txt', 'licenses/newsreader-OFL.txt'):
                    self.assertIn(required, names)
                self.assertNotIn('public_html.zip', names)
                self.assertFalse(any(name.startswith(('tests/', 'scripts/', 'preview/', '.git/', '.github/')) for name in names))
                self.assertEqual(bundle.read(archive.stem + '/theme/balaio.xml'),
                                 (Path(folder) / 'balaio.xml').read_bytes())


if __name__ == '__main__':
    unittest.main()
