# AWS AI Practitioner Academy — Montserrat Arabic Fix

## Important

The previous ZIP did not contain font files, so your browser fell back to another font. This version fixes the CSS and contains a tested, one-command installer. **Fonts are not redistributed in the ZIP.**

## Install the exact font you provided

1. Extract this website ZIP.
2. Put your original `Montserrat_Arabic_Font_Family_(Fontmirror)(1).zip` next to `setup-fonts.py` in the `AIF-C01-Tailwind-Academy/` folder.
3. Open Terminal inside that folder and run:

```bash
python3 setup-fonts.py
```

Alternatively, supply the full ZIP path:

```bash
python3 setup-fonts.py "/path/to/Montserrat_Arabic_Font_Family_(Fontmirror)(1).zip"
```

4. Refresh `index.html` and any `volume-N.html` page. Four `.otf` files will be installed in `assets/fonts/` locally. The `@font-face` URLs match these names exactly.

## Browser verification

Open DevTools → Inspect an Arabic paragraph → Computed → Rendered Fonts. You should see **Montserrat-Arabic** (or Montserrat Arabic Academy as the CSS family name). If you see Tahoma/Arial, check that `assets/fonts/Montserrat-Arabic-Regular.otf` exists and reload the page (disable cache if necessary).

## Design

Body text 16px desktop / 15.5px mobile. Headings 20–39px depending on hierarchy and screen size. Tables 14px desktop / 13.5px mobile. All six HTML pages reference the same `assets/typography.css`, which takes precedence over `assets/styles.css`.

The content is unchanged. This package contains the website source and installer, **not the font binaries**. Check font licensing before hosting.
