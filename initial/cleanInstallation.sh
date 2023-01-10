#!/bin/zsh
# cleanInstallation.sh
# Install bare minimum: Homebrew, terminal

# Import utility functions
source ./initial/utility/utility.sh

# Install Homebrew
if [ "$askPrompt" = "y" ]; then
    read "response?Do you want to install Homebrew [y/n]? "
    if [ "$response" = "y" ]; then
        homebrew_install
    else
        echo Exiting...
        exit
    fi

    read "response?Do you want to install brew-cu [y/n]? "
    if [ "$response" = "y" ]; then
        brew_cu_install
    else
        echo Exiting...
        exit
    fi

else
    homebrew_install
    brew_cu_install
fi

# Installation of python for installation help
if [ "$askPrompt" = "y" ]; then
    read "response?Do you want to install python [y/n]? "
    if [ "$response" = "y" ]; then
        brew install python
    else
        echo Exiting...
        exit
    fi

else
    brew install python
fi

# Install python modules
python3 ./main/python.py "$askPrompt"

# Install terminal
python3 ./main/ohmyzsh.py "$askPrompt"
python3 ./main/p10k.py "$askPrompt"