# appStore.py 
# Functions to help install apps from the App Store

import sys
sys.path.append('../utility')
from utility import process

def install(filepath: str, askPrompt=False, prompt='') -> None:
    print('Installing App Store %s apps' % prompt)

    if askPrompt and input('Download Pandoks_\'s App Store %s? [y/n]' % prompt) != 'y':
        return

    process.install(filepath, 'mas install')

    print('App Store %s apps installed' % prompt)

def install_all(appPaths: list, askPrompt=False) -> None:
    for appPath in appPaths:
        appName = process.name_from_file_path(appPath)
        install(appPath, askPrompt, appName)