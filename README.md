# Nyx

This is the source code for the custom discord bot used on one of my private discord servers.

## Features:

- Truth and Dare
- Never have I ever questions?
- Welcome Message (Coming Soon)
- Image Manipulation

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
- Image Manipulation
  - `$wanted` puts your avatar on a wanted poster
  - `$jesus` puts your avatar on Jesus's face
  - `$bad` puts your avatar on bad boy meme
  - `$trash` puts your avatar on a meme showing you as trash
