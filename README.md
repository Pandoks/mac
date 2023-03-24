mac
===

An installer for Pandoks_'s macOS applications and settings.

![Overview](https://user-images.githubusercontent.com/35944715/212475437-4f92c22e-b22b-4787-abe8-425ff12b1aca.gif)

Table of Contents
-----------------

- [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation](#installation)
- [Features](#features)
    - [Prompts](#prompts)
    - [Full Installation](#1-full-installation)
    - [Clean Installation](#2-clean-installation)
    - [Application Installation](#3-application-installation)
    - [Preference Installation](#4-preference-installation)
- [Configuration](#configuration)
    - [App Store](#app-store)
    - [Homebrew](#homebrew)
    - [Python](#python)
- [Upcoming Features](#upcoming-features)
    - [Multi-Threading](#multi-threading)
    - [Command Line Interface](#command-line-interface)
    - [Saving](#saving)

Installation
------------

### Requirements:

- macOS only
- zsh as default shell
- signed into Apple ID

---

### Installation:

To use the installer, run the following from the terminal.

```
git clone https://github.com/Pandoks/mac.git
cd mac
./install
```

![Install](https://user-images.githubusercontent.com/35944715/212465540-d191fdd8-1c05-4d7e-8b13-d1c9cae4d7ca.gif)

**NOTE:** If this is the first command to ever run in your terminal (fresh install of macOS), you may need to install command line developer tools. Run the above commands and you will be prompted to install the tools. Then run the code again after installation.

**Troubleshooting:** Only run `install` inside of the `mac` directory.

Features
-------- 

### Prompts:

This is similar to verbose flags for command line interfaces. If you answer `y` to the question `Do you want to be prompted about what is being installed [y/n]?`, you will be asked a prompt for each step of the installation. If you answer `n`, it will automatically install everything without prompting you what is being installed. You can use `ctrl+c` to cancel the install at any time.

![Prompt](https://user-images.githubusercontent.com/35944715/212465999-db6e9111-a6da-4c93-817c-1a0438583f69.gif)

---

### 1. Full Installation:

This installation option will run all other installations at once. 

**See:** [Clean Installation](#2-clean-installation), [Application Installation](#3-application-installation), [Preference Installation](#4-preference-installation) for more information.

---

### 2. Clean Installation:

This installation option will only install [Homebrew](https://brew.sh/) with no formulae or casks and Pandoks_'s terminal setup ([Oh-My-Zsh](https://ohmyz.sh/), [powerlevel10k](https://github.com/romkatv/powerlevel10k), and [Pandoks_'s Python modules](https://github.com/Pandoks/mac/tree/master/preferences/python)).

---

### 3. Application Installation:

This installation option will install all of Pandoks_'s Homebrew [formulae](https://github.com/Pandoks/mac/tree/master/preferences/homebrewFormulae) and [casks](https://github.com/Pandoks/mac/tree/master/preferences/homebrewCasks), and [App Store apps](https://github.com/Pandoks/mac/tree/master/preferences/appStore) using [mas](https://github.com/mas-cli/mas) in addition to the installations made in the [Clean Installation](#2-clean-installation) option.

**Troubleshooting:** You must be logged into your Apple ID for a successful App Store app installation

---

### 4. Preference Installation:

This installation option will install all of Pandoks_'s [vim](https://github.com/Pandoks/mac/tree/master/preferences/appSettings/vim), [tmux](https://github.com/Pandoks/mac/tree/master/preferences/appSettings/tmux) ([oh-my-tmux](https://github.com/gpakosz/.tmux)), [zsh](https://github.com/Pandoks/mac/tree/master/preferences/appSettings/zsh), and [hammerspoon](https://github.com/Pandoks/mac/tree/master/preferences/appSettings/hammerspoon) settings. In addition, you will be asked if you want to add Github API tokens or [sshpass](https://www.cyberciti.biz/faq/noninteractive-shell-script-ssh-password-provider/) aliases to your `.zshrc` file. If yes, you will be asked to enter the information needed and it will automatically add it to your `.zshrc` file. You will also be asked if you want to add any hot key bindings for hammerspoon to load. If yes, you will be asked to enter the information needed and it will automatically add it to your `init.lua` file.

![Preference](https://user-images.githubusercontent.com/35944715/212472729-8fe05529-664a-4432-9a04-69a942854760.gif)

Configuration
-------------

### Syntax:

The syntax used for the `.txt` files in the subdirectories of `preferences` is quite simple. Lines that are blank or contain `#` anywhere will be ignored. Everything else will be processed for installation. 

**NOTE:** Feel free to add `.txt` files. The installer will detect them.

---

### App Store:

Each application in the Mac App Store has a product identifier which is used for installation. There are two ways of finding a product identifier:

1. Find the product identifier from the share link in the App Store
2. Use `mas search`

![mas](https://user-images.githubusercontent.com/35944715/212473470-fe951e94-142a-4531-a27d-0e112593b51f.gif)

After finding the product identifier for the app you want, add it to a new or existing `.txt` file in the [appStore directory](https://github.com/Pandoks/mac/tree/master/preferences/appStore).

**Troubleshooting:** You must be logged into your Apple ID for a successful App Store app installation

---

### Homebrew:

Find the name of the formula or cask. There are two ways of finding the name:

1. Use `brew search` (**Recommended:** this is the preferred method of finding formulae or casks since it is always updated)
2. Search it up on [https://brew.sh/](https://brew.sh/) (The website may not show an available formula or cask)

![Homebrew](https://user-images.githubusercontent.com/35944715/212474448-cebc7225-bb97-4af2-b049-9ac98afdae5e.gif)

After finding the name of the package you want to install, if it is a formula, add it to a new or existing `.txt` file in the [homebrewFormulae directory](https://github.com/Pandoks/mac/tree/master/preferences/homebrewFormulae); but if it is a cask, add it to a new or existing `.txt` file in the [homebrewCasks directory](https://github.com/Pandoks/mac/tree/master/preferences/homebrewCasks).

---

### Python:

Find the package you want to install on [PyPi](https://pypi.org/). 

After finding a Python module you want to install, add it to a new or existing `.txt` file in the [python directory](https://github.com/Pandoks/mac/tree/master/preferences/python).

Upcoming Features
-----------------

### Multi-Threading:

Wanna see some speed? Multi-threaded downloads will make multiple installations parallel.

---

### Command Line Interface:

Wanna access the installer at any time? Type in a command in the terminal to access the application like any other command line interface application.

---

### Saving:

Don't want to manually edit the preference files? Saving will allow you to generate the files by detecting all of your downloads.

---

### Rust:

Letting the rustaceans take over 🦀
