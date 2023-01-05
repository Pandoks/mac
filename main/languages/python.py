# python.py
# Functions to install python modules (pip)

import sys
sys.path.append('../utility')
from utility import process

def install(filepath: str, askPrompt=False, prompt='') -> None:
    print('Installing Python %s modules' % prompt)

    if askPrompt and input('Download Pandoks_\'s Python module %s? [y/n]' % prompt) != 'y':
        return
    
    process.install(filepath, 'pip3 install')

    print('All python %s modules installed' % prompt)

def install_all(modulePaths: list, askPrompt=False) -> None:
    for modulePath in modulePaths:
        moduleName = process.name_from_file_path(modulePath)
        install(modulePath, askPrompt, moduleName)