# homebrew.py
# Functions to help install homebrew formulae

import sys
sys.path.append('../utility')
from utility import process

def install(filepath: str, askPrompt=False, prompt='') -> None:
    print('Installing Homebrew formulae %s' % prompt)

    if askPrompt and input('Download Pandoks_\'s Homebrew %s? [y/n]' % prompt) != 'y':
        return
    
    process.install(filepath, 'brew install')

    print('All Homebrew formulae %s installed' % prompt)

def install_all(formulaePaths: list, askPrompt=False) -> None:
    for formulaPath in formulaePaths:
        formulaName = process.name_from_file_path(formulaPath)
        install(formulaPath, askPrompt, formulaName)