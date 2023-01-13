#!/bin/zsh
# vim.sh
# Install vim settings

# Pull up instructions for complete installation for the user after install
if [ "$askPrompt" = "y" ]; then
    read "response?Do you want to install Pandoks_'s vim settings [y/n]? "
    if [ "$response" = "y" ]; then
        echo Installing vim settings
        echo "Please IGNORE the error message and continue with ENTER"
        mkdir ~/.vim
        cp ./preferences/appSettings/vim/vimrc ~/.vim
        vim ./preferences/appSettings/vim/instructions.txt
        echo vim settings installed
    else
        echo Skipping
        exit
    fi
else
    echo Installing vim settings
    echo "Please IGNORE the error message and continue with ENTER"
    mkdir ~/.vim
    cp ./preferences/appSettings/vim/vimrc ~/.vim
    vim ./preferences/appSettings/vim/instructions.txt
    echo vim settings installed
fi