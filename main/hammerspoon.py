# hammerspoon.py
# Functions to help install hammerspoon keybinds

import os
from utility import prompt
from utility import process

if __name__ == '__main__':
    initialLocation = './preferences/appSettings/hammerspoon/init.lua'
    finalLocation = '~/.hammerspoon/init.lua'

    # Install
    askPrompt = process.check_prompt()
    if askPrompt:
        if input('Do you want to install Pandoks_\'s hammerspoon key bindings [y/n]? ') == 'y':
            print('Installing Hammerspoon bindings')
            prompt.hammerspoon_key_binding_process(initialLocation)
            os.system('cp %s %s' % (initialLocation, finalLocation))
            print('All hammerspoon key bindings installed')
        else:
            print('Skipping')
            exit()
    else:
        print('Installing Hammerspoon bindings')
        prompt.hammerspoon_key_binding_process(initialLocation)
        os.system('cp %s %s' % (initialLocation, finalLocation))
        print('All hammerspoon key bindings installed')

    # Initialize key bindings
    print('Initializing Hammerspoon key bindings.')
    print('Change Hammerspoon settings to your own preferences and reload config.')
    os.system('open -a Hammerspoon')
    
    
    
