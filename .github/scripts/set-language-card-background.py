from pathlib import Path
import re

path = Path("profile/top-langs.svg")
svg = path.read_text(encoding="utf-8")
pattern = re.compile(r'(<rect\s+data-testid="card-bg".*?\s+fill=")[^"]+(".*?/>)', re.DOTALL)
svg, replacements = pattern.subn(r'\g<1>#21262D\g<2>', svg, count=1)
if replacements != 1:
    raise SystemExit("Could not find the language card background in the generated SVG")
path.write_text(svg, encoding="utf-8")
