
# Telegram Bot Using Python

telegram bot 

##  Required Packages 

Packages required to run this project 

```bash
  pip install python-telegram-bot
  pip install pyjokes
```


## Examples

```python
from telegram.ext import *
from telegram import *
import pyjokes
import os

PORT = int(os.environ.get('PORT','8443'))

TOKEN = os.environ.get('TOKEN')

bot = Bot(TOKEN)

print(bot.get_me())

def start(update:Update, context:CallbackContext):
    update.message.reply_text('your starting message')

def joke(update:Update, context:CallbackContext):
    joke = pyjokes.get_joke()
    update.message.reply_text(joke)

def help(update:Update, context:CallbackContext):
    update.message.reply_text('your help message')

updater = Updater(TOKEN,  use_context=True)
dispatch = updater.dispatcher

dispatch.add_handler(CommandHandler("start",start))
dispatch.add_handler(CommandHandler("joke",joke))
dispatch.add_handler(CommandHandler("help",help))



updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://{your-herokua-app-name}.herokuapp.com/"+ TOKEN  )
updater.idle()
```


## Important files for this Project

create file without any extension and name as Procfile

    ## Procfile
    inside Procfile write :-   web: python3 bot.py

create a file with txt extension and name as runtime

    ## runtime
    inside runtime.txt write :-   python-3.8.12

now we will create last file requirements.txt file by using a command

    ## requirements.txt
    just give this command in terminal :- pip freeze > requirements.txt
## Authors

- [@krishna sonune](https://www.github.com/krishnasonune)

