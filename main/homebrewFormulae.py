# homebrewFormulae.py
# Functions to help install homebrew formulae

from utility import process
from utility import installer

if __name__ == '__main__':
    installPath = './preferences/homebrewFormulae'
    installerCommand = 'brew install'
    askPrompt = process.check_prompt()
    if askPrompt:
        if input('Do you want to install Pandoks_\'s Homebrew formulae [y/n]? ') == 'y':
            installer.make_install(installPath, installerCommand, askPrompt)
        else:
            print('Skipping')
    else:
        installer.make_install(installPath, installerCommand, askPrompt)