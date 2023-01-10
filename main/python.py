# python.py
# Functions to install python modules (pip)

from utility import process
from utility import installer

if __name__ == '__main__':
    installPath = './preferences/python'
    installerCommand = 'pip3 install'
    askPrompt = process.check_prompt()
    if askPrompt:
        if input('Do you want to install Pandoks_\'s Python modules [y/n]? ') == 'y':
            installer.make_install(installPath, installerCommand, askPrompt)
        else:
            print('Skipping')
    else:
        installer.make_install(installPath,installerCommand, askPrompt)
