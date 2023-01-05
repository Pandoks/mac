# install.py
# Main installation 

import os
from utility import process

# Ask if want to be prompted for each section of install
askPrompt = True
if input('Install all Pandoks_\'s preferences at once? (recommended) [y/n]') == 'y':
    askPrompt = False

########################################
#######       Main Install      ########
########################################
# Homebrew install
# formulae
from homebrew import homebrew
formulaePaths = process.preference_file_location_list('./preferences/homebrew', 'homebrewFormulae')
homebrew.install_all(formulaePaths, askPrompt)

# cask
from homebrew import homebrewCask
caskPaths = process.preference_file_location_list('./preferences/homebrew', 'homebrewCasks')
homebrewCask.install_all(caskPaths, askPrompt)

# App Store install
from appStore import appStore
appPaths = process.preference_file_location_list('./preferences/appStore')
appStore.install_all(appPaths, askPrompt)

# Python install
from languages import python
modulePaths = process.preference_file_location_list('./preferences/python')
python.install_all(modulePaths, askPrompt)

# Terminal install
from terminal import ohmyzsh
from terminal import p10k
if input('Install Pandoks_\'s Terminal? [y/n]') == 'y':
    ohmyzsh.install()
    p10k.install()

########################################
#######     Settings Install    ########
########################################
