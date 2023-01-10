# appStore.py 
# Functions to help install apps from the App Store

from utility import process
from utility import installer

if __name__ == '__main__':
    installPath = './preferences/appStore'
    installerCommand = 'mas install'
    askPrompt = process.check_prompt()
    if askPrompt:
        if input('Do you want to install Pandoks_\'s App Store Apps [y/n]? ') == 'y':
            installer.make_install(installPath, installerCommand, askPrompt)
        else:
            print('Skipping')
    else:
        installer.make_install(installPath,installerCommand, askPrompt)