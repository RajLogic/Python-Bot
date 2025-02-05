# RajLogic Discord Bot

This is a Discord bot built with Python. :  

## Features

- All commands are Slash


## Commands
- ping - shows bots latencey  and uptime
- hello - Hello
- botinvite - Invite the bot 
- serverinvite - bot creates a bot invite link for your server
- serverinfo - get info for server
- movie - searches for info on movie   
- help -  shows command
- warn -  warns a user and saves it to json file
- warnings - reads json file and responds with the number of warnings
- clearwarnings - removes all warnings  from json file
- kick - kicks  a member from the server
- ban - bans a member from the server
- unban - unbans a member from the server

## Installation

1. Clone the repository: 
```bash
git clone https://github.com/RajLogic/Python-Bot.git
```
2. Install the required dependencies: 
```bash
pip install -r requirements.txt
```
3. Rename all Data Files by removing Example from Them.
Example
```bash
bansExample.json   ---->  bans.json
```
4. Configure the bot token: Replace `YOUR_BOT_TOKEN` in `.env` with your Discord bot token.

## Usage

1. Run the bot: 
```bash
python main.py
```
2. Invite the bot to your Discord server using the following link: [Invite Bot](https://discord.com/developers/applications))

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
