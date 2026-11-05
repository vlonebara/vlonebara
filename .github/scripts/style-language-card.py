from pathlib import Path

card = Path("profile/top-langs.svg")
svg = card.read_text(encoding="utf-8")
replacements = {
    'fill="#ffffff00"': 'fill="#0D1117"',
    'stroke="#e4e2e2"': 'stroke="#30363D"',
    'stroke-opacity="0"': 'stroke-opacity="1"',
    'fill: #417E87;': 'fill: #C9D1D9;',
    'fill: #006AFF;': 'fill: #58A6FF;',
    'fill: #ddd;': 'fill: #30363D;',
}
for old, new in replacements.items():
    if old not in svg:
        raise SystemExit(f"Expected SVG styling was not found: {old}")
    svg = svg.replace(old, new)
card.write_text(svg, encoding="utf-8")
