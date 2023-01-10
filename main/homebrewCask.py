# homebrewCask.py
# Functions to help install homebrew casks

from utility import process
from utility import installer

if __name__ == '__main__':
    installPath = './preferences/homebrewCasks'
    installerCommand = 'brew install --cask'
    askPrompt = process.check_prompt()
    if askPrompt:
        if input('Do you want to install Pandoks_\'s Homebrew casks [y/n]? ') == 'y':
            installer.make_install(installPath, installerCommand, askPrompt)
        else:
            print('Skipping')
    else:
        installer.make_install(installPath, installerCommand, askPrompt)