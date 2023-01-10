#!/bin/zsh
# utility.sh
# Script functions to help other installations

# Install Homebrew
homebrew_install() {
    printf "Installing Homebrew\n"

    # Install Homebrew
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    printf "Homebrew installed\n"

    # Add Homebrew to PATH
    printf "Adding Homebrew to PATH\n"
    echo '# Set PATH, MANPATH, etc., for Homebrew.' >> ~/.zprofile
    echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/opt/homebrew/bin/brew shellenv)"
    printf "Homebrew added to PATH\n"    
}

# brew cu Install
brew_cu_install() {     # MUST run homebrew_install() before running
    printf "Installing brew cu\n"
    brew tap buo/cask-upgrade
    printf "brew cu installed\n"
}