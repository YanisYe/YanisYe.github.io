#!/usr/bin/env python3
"""Static checks for the Jekyll academic homepage."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    '_config.yml', 'Gemfile', '_data/navigation.yml', '_pages/about.md',
    '_layouts/default.html', '_includes/author-profile.html', '_includes/masthead.html',
    'assets/css/main.scss', 'assets/js/main.min.js', 'images/yiqiang-avatar.svg',
    'files/Yiqiang-Ye-CV-EN.pdf', 'README.md',
]
REQUIRED_TEXT = [
    'Yiqiang Ye', 'yaniszz085@gmail.com', 'Shenzhen University',
    'Physics-Informed Environment Modeling', 'Knowledge-Integrated Spatial Decision-Making',
    'Spherical Physics-informed Neural Operator', 'Deep reinforcement learning unlocks sustainable livestock reallocation',
    'Interpretable Pulmonary Disease Diagnosis', 'Yiqiang-Ye-CV-EN.pdf',
]
FORBIDDEN = ['Guanting Dong', 'dongguanting', 'HuxBlog', 'huxpro', 'Your Blog', 'Boilerplate of Hux Blog']


def main() -> int:
    for rel in REQUIRED_FILES:
        assert (ROOT / rel).exists(), f'missing required file: {rel}'

    config = (ROOT / '_config.yml').read_text(encoding='utf-8')
    nav = (ROOT / '_data/navigation.yml').read_text(encoding='utf-8')
    about = (ROOT / '_pages/about.md').read_text(encoding='utf-8')
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    combined = '\n'.join([config, nav, about, readme])

    for text in REQUIRED_TEXT:
        assert text in combined, f'missing required text: {text}'
    for text in FORBIDDEN:
        assert text not in combined, f'forbidden placeholder/reference text remains: {text}'

    for anchor in ['about-me', 'news', 'education', 'research', 'publications', 'honors-awards', 'contact']:
        assert f"id='{anchor}'" in about or f'id="{anchor}"' in about, f'missing anchor: {anchor}'
        assert f'"/#{anchor}"' in nav, f'missing nav target: {anchor}'

    local_paths = set()
    for match in re.finditer(r"\{\{\s*'(/[^']+)'\s*\|\s*relative_url\s*\}\}", '\n'.join([config, about])):
        local_paths.add(match.group(1).lstrip('/'))
    for match in re.finditer(r'avatar\s*:\s*"?(/[^"\n]+)"?', config):
        local_paths.add(match.group(1).lstrip('/'))
    for path in sorted(local_paths):
        if path.startswith(('http:', 'https:')):
            continue
        assert (ROOT / path).exists(), f'local relative_url path missing: {path}'

    assert 'github           : "YanisYe"' in config, 'GitHub username should be set from repo owner'
    print('Site validation passed.')
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f'Site validation failed: {exc}', file=sys.stderr)
        raise SystemExit(1)
