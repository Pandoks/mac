# homebrewCask.py
# Functions to help install homebrew casks

import sys
sys.path.append('../utility')
from utility import process

def install(filepath: str, askPrompt=False, prompt='') -> None:
    print('Installing Homebrew casks %s' % prompt)
    
    if askPrompt and input('Download Pandoks_\'s Homebrew cask %s? [y/n]' % prompt) != 'y':
        return

    process.install(filepath, 'brew install --cask')

    print('All Homebrew casks %s installed' % prompt)

def install_all(caskPaths: list, askPrompt=False) -> None:
    for caskPath in caskPaths:
        caskName = process.name_from_file_path(caskPath)
        install(caskPath, askPrompt, caskName)