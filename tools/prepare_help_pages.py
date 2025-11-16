"""Script for help page preparation.

Requires Python 3.9+

Copyright (c) 2025 Peter Triesberger
For further information see https://github.com/peter88213/nv_xx
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
from string import Template

DIVIDER = ']('
BULLET = '- ['

HOME_DIR = '../docs'
HOME_PAGE = f'{HOME_DIR}/index.md'

page = '''$Breadcrumbs > $Heading

---

# $Heading

'''

with open(HOME_PAGE, 'r', encoding='utf-8') as f:
    text = f.read()

header = True
for line in text.split('\n'):
    if header:
        if line.startswith('---'):
            header = False
        elif line.startswith('['):
            breadcrumb = f'{line}{DIVIDER}index.md)'.replace('> ', '> [')
        continue

    if not line.startswith(BULLET):
        continue

    line = line.removeprefix(BULLET).removesuffix(')')
    heading, link = line.split(DIVIDER)

    mapping = dict(
        Breadcrumbs=breadcrumb,
        Heading=heading,
    )
    text = Template(page).safe_substitute(mapping)

    with open(f'{HOME_DIR}/{link}', 'w', encoding='utf-8') as f:
        f.write(text)

