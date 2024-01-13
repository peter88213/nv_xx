"""Helper script for copying noveltree plugin translation files to the language pack directory.

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/noveltree
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import glob
import os
from shutil import copyfile
from settings import *

ROOT_DIR = '../..'

os.chdir(ROOT_DIR)
for program in glob.iglob('noveltree*', recursive=False):
    potFile = f'{program}/i18n/messages.pot'
    if os.path.isfile(potFile):
        targetPath = f'noveltree_{languageCode}/programs/{program}'
        os.makedirs(targetPath, exist_ok=True)
        copyfile(potFile, f'{targetPath}/messages.pot')
        print(program)
print('Done.')
