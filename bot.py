from telegram.ext import *
from telegram import *
import pyjokes
import os

PORT = int(os.environ.get('PORT', '8443'))
TOKEN = os.environ.get('TOKEN')

bot = Bot(TOKEN)
print(bot.get_me())

def start(update:Update, context:CallbackContext):
    update.message.reply_text("hii i am jokify bot, if you are having bad day, I'll try to make you laugh with my jokes and cheer your mood just give /joke command for jokes and /help for any kind of help")

def joke(update:Update, context:CallbackContext):
    joke = pyjokes.get_joke()
    update.message.reply_text(joke)

def help(update:Update, context:CallbackContext):
    update.message.reply_text('If you like my jokify bot pleease make sure you share it with your friends and spread smile, and for any help contact my owner on PyDeveloper')

updater = Updater(TOKEN, use_context=True)
dispatch = updater.dispatcher

dispatch.add_handler(CommandHandler("start",start))
dispatch.add_handler(CommandHandler("joke",joke))
dispatch.add_handler(CommandHandler("help",help))



updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://calm-lake-92141.herokuapp.com/"+ TOKEN )
updater.idle()