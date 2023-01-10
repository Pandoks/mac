# p10k.py
# Functions to install powerlevel10k to Oh-My-Zsh

import os
from utility import process

def p10k_shell() -> None:
    os.system('brew install romkatv/powerlevel10k/powerlevel10k')
    os.system('echo "source $(brew --prefix)/opt/powerlevel10k/powerlevel10k.zsh-theme" >> ~/.zshrc')
    
def install() -> None:
    print('Installing powerlevel10k\n')
    p10k_shell()
    print('powerlevel10k installed\n')

if __name__ == '__main__':
    askPrompt = process.check_prompt()
    if askPrompt:
        if input('Do you want to install powerlevel10k [y/n]? ') == 'y':
            install()
        else:
            print('Skipping')
            exit()
    else:
        install()