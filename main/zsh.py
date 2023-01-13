# zsh.py
# Functions to help install .zshrc

import os
from utility import prompt
from utility import process

if __name__ == '__main__':
    initialLocation = './preferences/appSettings/zsh/.zshrc'
    finalLocation = '~/.zshrc'
    
    askPrompt = process.check_prompt()
    if askPrompt:
        if input('Do you want to install Pandoks_\'s zsh settings [y/n]? ') == 'y':
            print('Installing zsh settings')
            prompt.github_api_token_process(initialLocation)
            prompt.sshpas_alias_process(initialLocation)
            os.system('cp %s %s' % (initialLocation, finalLocation))
            print('All zsh settings installed')
        else:
            print('Skipping')
    else:
        print('Installing zsh settings')
        prompt.github_api_token_process(initialLocation)
        prompt.sshpas_alias_process(initialLocation)
        os.system('cp %s %s' % (initialLocation, finalLocation))
        print('All zsh settings installed')