#!/bin/zsh
# preferenceInstallation.sh
# Install settings and preferences [MUST have all others installed]

# Install vim settings and preferences
. ./main/vim.sh

# Install zsh settings and preferences
python3 ./main/zsh.py "$askPrompt"

# Install tmux settings and preferences
. ./main/tmux.sh

# Install Hammerspoon key bindings
python3 ./main/hammerspoon.py "$askPrompt"