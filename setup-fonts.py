#!/usr/bin/env python3
"""Install your own Montserrat Arabic .zip into this site's assets/fonts directory.
Usage: python3 setup-fonts.py "/path/to/Montserrat_Arabic_Font_Family.zip"
When no argument is given, search next to this script and its parent folder.
The archive is processed locally and its font binaries are never distributed with this website.
"""
from pathlib import Path
import re, sys, zipfile
ROOT = Path(__file__).resolve().parent
DEST = ROOT / 'assets' / 'fonts'
WEIGHTS = {400: 'Regular', 500: 'Medium', 600: 'SemiBold', 700: 'Bold'}

def locate():
    if len(sys.argv) >= 2:
        path = Path(sys.argv[1]).expanduser()
        if not path.is_file():
            raise SystemExit(f'Cannot find font zip: {path}')
        return path
    choices = [p for folder in [ROOT, ROOT.parent] for p in folder.glob('*.zip') if 'montserrat' in p.name.lower()]
    if len(choices) == 1: return choices[0]
    raise SystemExit('Place the Montserrat Arabic font ZIP beside setup-fonts.py and run again, or pass its path as an argument.')

def main():
    archive = locate()
    DEST.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as z:
        members = [m for m in z.infolist() if not m.is_dir() and m.filename.lower().endswith(('.otf', '.ttf'))]
        for weight, label in WEIGHTS.items():
            expected = re.compile(r'montserrat[-_ ]arabic.*(?:^|[ _-])' + re.escape(label) + r'(?:[ _-]|\.)', re.I)
            matched = [m for m in members if expected.search(Path(m.filename).name) and
                       (label != 'Bold' or not re.search('ExtraBold|SemiBold', m.filename, re.I))]
            if len(matched) != 1:
                raise SystemExit(f'Expected exactly one Montserrat Arabic {label} font; got {len(matched)}')
            raw = z.read(matched[0])
            if not raw: raise SystemExit(f'Empty file: {matched[0].filename}')
            out = DEST / f'Montserrat-Arabic-{label}.otf'
            out.write_bytes(raw)
            print(f'✓ {label} ({weight}) installed: {out.relative_to(ROOT)}')
    print('\nReady. Open index.html (or refresh the browser). Montserrat Arabic will now render locally.')

if __name__ == '__main__': main()
