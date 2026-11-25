# Responsive review — 25 Nov 2026

Reviewed the homepage and all five volumes structurally and via CSS/JS static inspection.

## Confirmed fixes
- Consistent 76px header/sidebar offset to prevent overlay conflicts at mobile widths.
- Responsive navigation at <=780px; open state now has a dismissible backdrop, Escape support and aria-expanded state.
- Header adapts at <=480px and <=350px; print button hidden on narrow mobile screens.
- Tables and formulas have contained horizontal overflow; long English terms wrap.
- Images and SVG diagrams are width constrained.
- Main content and cards cannot force page-level horizontal overflow through standard blocks.
- Reduced padding and heading scales on small phones while retaining readable body text.
- Desktop sidebar and 1010px reading area are retained.

## Tested
- All six HTML pages parsed successfully; correct RTL and viewport metadata.
- All six include responsive.css.
- CSS parsed without syntax errors, and app.js passed node --check.
- Local font installation was tested using the user-provided archive, but font binaries are not distributed.

## Limitations
Automated Chromium was available but navigation to both file:// and localhost pages was blocked by the runtime administrator. Thus no verified browser screenshots or true 320/375/390/768/1024/1440px visual pass was possible. Run real-device/browser testing after extraction, including menu opening, horizontal overflow, dark mode, diagrams and table scrolling.

## Fonts
This distribution excludes Montserrat-Arabic font binaries. Run setup-fonts.py with your own licensed archive.
