#!/bin/zsh
# tmux.sh
# Install oh-my-tmux settings

# Install oh-my-tmux from github repository
if [ "$askPrompt" = "y" ]; then
    read "response?Do you want to install Pandoks_'s tmux settings [y/n]? "
    if [ "$response" = "y" ]; then
        echo Installing tmux settings
        git clone https://github.com/gpakosz/.tmux.git ~/.tmux
        ln -s -f ~/.tmux/.tmux.conf ~/.tmux.conf
        cp ./preferences/appSettings/tmux/.tmux.conf.local ~/.tmux.conf.local
        vim ./preferences/appSettings/tmux/instructions.txt
        tmux
        echo tmux settings installed
    else
        echo Skipping
        exit
    fi

else
    echo Installing tmux settings
    git clone https://github.com/gpakosz/.tmux.git ~/.tmux
    ln -s -f ~/.tmux/.tmux.conf ~/.tmux.conf
    cp ./preferences/appSettings/tmux/.tmux.conf.local ~/.tmux.conf.local
    vim ./preferences/appSettings/tmux/instructions.txt
    tmux
    echo tmux settings installed
fi