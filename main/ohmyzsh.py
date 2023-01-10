# ohmyzsh.py
# Functions to help install oh-my-zsh

import os
from utility import process

def process_download(link: str, filepath: str) -> None:
    process.curl_download(link, filepath)
    os.system('chmod a+rx %s' % filepath)
    process.filter_code(filepath, 'exec ')

def install() -> None:
    print('Installing Oh-My-Zsh')
    link = 'https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh'
    filepath = './ohmyzsh.sh'
    process_download(link, filepath)
    os.system(filepath)
    print('Oh-My-Zsh Installed')

if __name__ == '__main__':
    askPrompt = process.check_prompt()
    if askPrompt:
        if input('Do you want to install Oh-My-Zsh [y/n]? ') == 'y':
            install()
        else:
            print('Skipping')
            exit()
    else:
        install()