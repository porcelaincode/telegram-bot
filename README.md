<p align="center">
  <a href="https://github.com/porcelaincode/telegram-bot">
    <img src="https://img.icons8.com/color/344/telegram-app--v1.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Telegram Bot Template</h3>

  <p align="center">
    Telegram Bot | Custom Functions
  </p>
</p>


## Table of contents
* [General info](#general-info)
* [Requirements](#requirements)
* [Setup](#setup)
* [Build](#build)

## General info
This project is a simple template to pull, edit and launch your own telegram bot
	
## Requirements
Project requirements are simple:
* python 3.6 and above
* requests==2.25.1
```sh
$ pip install requests
```

## Setup

- To run this project, install it locally:

```sh
$ git clone https://github.com/porcelaincode/telegram-bot.git
```

- if you haven't yet registered a bot of your own, head to [@BotFather](https://t.me/BotFather) and follow instructions to continue

- Head back to your project directory after getting your Bot Token

- in `config.cfg` file, fill in your bot token and user id

```
  token =
  user_id =
```

- run `telegram.py` file

```sh
  $ python telegram.py
```

## Build

You use or design your own modules returning a value

```python

def sampleFunction(message):
    # Do something with the message
    return reply

your_text = str(message["text"])
sampleReply = sampleFunction(your_text)
telebot.send_message(sampleReply, user_id)

```

See the [Telegram API Documentation](https://core.telegram.org/) for a list of features to build upon this template.

