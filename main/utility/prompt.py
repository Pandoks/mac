# prompt.py
# Functions to help get information from the user

def github_api_token_process(fileLocation: str,) -> None:
    if input('Do you have any Github API tokens you want to export [y/n]? ') != 'y':
        print('Skipping...')
        exit()

    zshrcFile = open(fileLocation, 'r')
    zshrcLines = zshrcFile.readlines()
    zshrcFile.close()
    
    zshrcFile = open(fileLocation, 'w')
    locationLine = '# TODO: Enter Github API tokens here.'
    for zshrcLine in zshrcLines:
        if locationLine not in zshrcLine:
            zshrcFile.write(zshrcLine)
            continue

        while input('Add a github token [y/n]? ') == 'y':
            print('What is the name of the Github API token?')
            tokenName = input('EXAMPLE (Homebrew\'s name: HOMEBREW_HITHUB_API_TOKEN): ')
            tokenCode = input('What is the token? ')
            tokenComment = input('What comment do you want for the token? ')

            commentLine = '# %s\n' % tokenComment
            exportLine = 'export %s=%s\n' % (tokenName, tokenCode)

            zshrcFile.write(commentLine)
            zshrcFile.write(exportLine)
        zshrcFile.write('\n')

    zshrcFile.close()

def sshpas_alias_process(fileLocation: str) -> None:
    if input('Do you want to create sshpass aliases [y/n]? ') != 'y':
        print('Skipping...')
        exit()
    
    zshrcFile = open(fileLocation, 'r')
    zshrcLines = zshrcFile.readlines()
    zshrcFile.close()

    zshrcFile = open(fileLocation, 'w')
    locationLine = '# TODO: Enter sshpass aliases here.'
    for zshrcLine in zshrcLines:
        if locationLine not in zshrcLine:
            zshrcFile.write(zshrcLine)
            continue

        while input('Add a sshpass alias [y/n]? ') == 'y':
            aliasName = input('What is the alias (shortcut for ssh)? ')
            sshServer = input('What is the server? ')
            sshPassword = input('What is the server password? ')

            aliasLine = 'alias %s="sshpass -p %s ssh %s"\n' % (aliasName, sshPassword, sshServer)

            zshrcFile.write(aliasLine)
        zshrcFile.write('\n')

    zshrcFile.close()

def hammerspoon_key_binding_process(fileLocation: str) -> None:
    if input('Do you want Hammerspoon hot keys [y/n]? ') != 'y':
        print('Skipping...')
        exit()
    
    hammerFile = open(fileLocation, 'r')
    hammerLines = hammerFile.readlines()
    hammerFile.close()

    hammerFile = open(fileLocation, 'w')
    for hammerLine in hammerLines:
        hammerFile.write(hammerLine)
    hammerFile.write('-- Hot Keys\n')

    while input('Add a hot key [y/n]? ') == 'y':
        hotKeyName = input('What is the hot key name (one word)? ')
        hotKeyText = input('What string of text is the hot key for? ')
        hotKeySpecial = input('What are the special keys that need to be pressed (check lua script for notation)? ')
        hotKeyBinding = input('What is the letter/s that need to be pressed? ')

        hotKeyVariable = '%s = \'%s\'\n' % (hotKeyName, hotKeyText)
        hotKeyLine = ('hs.hotkey.bind(\'%s\', \'%s\', function()\n' 
                      '    hs.eventtap.keyStrokes(%s)\n'
                      'end)\n' % (hotKeySpecial, hotKeyBinding, hotKeyName))
        
        hammerFile.write(hotKeyVariable)
        hammerFile.write(hotKeyLine)
        hammerFile.write('\n')
        
    hammerFile.close()
