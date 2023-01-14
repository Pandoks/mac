#!/bin/zsh
# applicationInstallation.sh
# Install Homebrew, terminal, casks, applications

# Install Homebrew and terminal
. ./initial/cleanInstallation.sh

# Install App Store installer
if [ "$askPrompt" = "y" ]; then
    read "response?Do you want to install mas [y/n]? "
    if [ "$response" = "y" ]; then
        brew install mas
    else
        echo Exiting...
        exit
    fi

else
    brew install mas
fi

# Ask if signed into Apple ID
read "response?Are you signed into your Apple ID [y/n]? "
if [ "$response" != "y" ]; then 
    echo Make sure you are signed into your Apple ID before installation.
    open -a System\ Settings
    echo Exiting...
    exit
fi

# Install Homebrew formulae
python3 ./main/homebrewFormulae.py "$askPrompt"

# Install Homebrew casks
python3 ./main/homebrewCask.py "$askPrompt"

# Install App Store applications
python3 ./main/appStore.py "$askPrompt"