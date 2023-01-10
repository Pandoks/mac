# installer.py 
# Functions to help install files

import os
from utility import process

def install(filepath: str, installer: str, askPrompt=False, prompt='') -> None:
    print('Installing %s' % prompt)

    if askPrompt and input('Download Pandoks_\'s %s? [y/n]' % prompt) != 'y':
        print('Skipping')
        return

    # installation process
    installations = process.txt_to_list(filepath)
    for installation in installations:
        installationCommand = '%s %s' % (installer, installation)
        os.system(installationCommand)
    
    print('All %s installed' % prompt)

def install_all(installPaths: list, installer: str, askPrompt=False, prompt='') -> None:
    for installPath in installPaths:
        installName = prompt + ' ' + process.name_from_file_path(installPath)
        install(installPath, installer, askPrompt, installName)

def make_install(installPath: str, installer: str, askPrompt: bool) -> None:
    installPaths = process.preference_file_location_list(installPath)
    installName =  process.name_from_file_path(installPath)
    install_all(installPaths, installer, askPrompt, installName)