# Skool Gang Discord Bot
This is the repo for the custom discord bot used on the [Skool Gang]() discord server
## Features:
- Truth and Dare

## Setup
- Clone the repository: `git clone https://github.com/krishaayjois21/nyx.git`
- Move into the directory `cd nyx/`
- Install dependencies: `pip install -r requirements.txt`
- Create a new app on the [Discord Developer Portal](https://discord.com/developers/)
- Edit the `.env` file and replace `<token>` with the bot token
- Uncomment line `5` and `6` from `main.py`

## Run the bot
- Run with `python main.py`

## Extensions
To add extensions
- Add the extension python file to the `modules` directory
- edit `config/config.json` and add an entry in the following format
    - Format: `modules.<extension_filename_without_.py>`
- Rerun the `main.py` file
## Commands: Prefix(`$`)
- Help
    - `$help` displays all the availale commands
- Truth and Dare
    - `$truth` or `$t` for truth questions
    - `$dare` or `$d` for dare questions
    - `$never` or `$n` for never have I ever questions
