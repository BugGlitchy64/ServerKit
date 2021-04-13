# ServerKit

[Invite link](https://discord.com/oauth2/authorize?client_id=828582617254461481&permissions=2587094358&scope=bot%20applications.commands)

ServerKit is a Discord bot that combats bot features that are locked by paywall and reduce the number of bots needed in a server.

## Table of contents

* [Technologies used](#technologies-used)
* [Setup](#setup)
* [Features](#features)
* [Roadmap](#roadmap)
* [Support](#support)
* [Self-hosting and using the bot's code](#self-hosting-or-using-the-bots-code-in-general)
* [Contributing](#contributing)
* [Project status](#project-status)
* [Inspiration](#Inspiration)
* [License](#license)

## Technologies used

| Technology | Description | Link |
| ----------- | ----------- | ----------- |
| Python | A beginner-friendly programming language | https://www.python.org/ |
| python-dotenv | Read key-value pairs from a .env file and set them as environment variables. | https://pypi.org/project/python-dotenv/ |
| discord.py | Modern, easy to use, feature-rich, and async ready API wrapper for Discord in Python. | https://github.com/Rapptz/discord.py/ |
| discord-py-slash-command | A simple discord slash command handler for discord.py. | https://github.com/eunwoo1104/discord-py-slash-command |
| PyNaCl | Python binding to the Networking and Cryptography (NaCl) library. | https://github.com/pyca/pynacl |
| FFmpeg | A complete, cross-platform solution to record, convert and stream audio and video. | https://www.ffmpeg.org/ |
| youtube-dl | Command-line program to download videos from YouTube.com and other video sites. | https://github.com/ytdl-org/youtube-dl |

## Setup

1. Install latest version of above list.
2. Create a .env file with the contents:
```
PRODUCTION=False
PRODUCTIONTOKEN=(Leave blank)
DEVTOKEN=(Your bot token)
```
3. Start `main.py`

## Features

### Open Source (and being Libre)
Being open source benefits the users, everyone can submit bugs, check code, or even pull request to make the bot work better.

### Free, forever
No patreon bs.

### Other features
* Slash Command Support
* Moderation commands
* Music commands
* Fun commands

## Roadmap
- More fun features (View memes and create memes)
- Welcomer features
- More moderation features (Logging, etc.)

## Support

Join the Support server on [Discord](https://discord.gg/CqRkKpZR), or if the bug impacts all users, submit a issue here.

## Self-hosting (or using the bot's code in general)

You can only self-host this bot if you want to test your changes.
As per the license requires, PLEASE DON'T TAKE THE BOT'S CODE AS YOUR OWN.

## Contributing

I am ABSOLUTELY open to any contributions, please make sure you state what changed.

## Project status

Project is in progress and allow everyone to use and test.

## Inspiration

Thanks to all major Discord bots out there to make me develop this bot! Specially those bots that it's features are locked by paywalls.

## License
Up until version 0.3.5.1, it is in [GPL license](https://www.gnu.org/licenses/gpl-3.0.html), after 0.3.5.1, it will be switched to [AGPL License](https://www.gnu.org/licenses/agpl-3.0.html) since Discord Bots counts as server software (duh.)
