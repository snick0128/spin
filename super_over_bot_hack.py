#!/usr/bin/env python
# pylint: disable=C0116,W0613
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import random


from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

lst = [1,2,3,4,5,6,7,8,9,10]
mylst=[]
wtf=False

print("requsting please wait")

def getnum():
    print(wtf)
    if not wtf:
        return random.choice(lst)
    if wtf:
        return mylst[-1]

# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, context: CallbackContext) -> None:
    print(update)
    """Send a message when the command /start is issued."""
    user = update.effective_user
    #update.message.reply_markdown_v2(
     #   fr'Hi {user.mention_markdown_v2()}\!',
      #  reply_markup=ForceReply(selective=True),
   # )


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    print(update)
    update.message.reply_text('Help!')

    
def sett(update: Update, context: CallbackContext) -> None:
        global list_to_use
        global wtf
        my_head = [1719921402,585062110,1657154573,1083705812,1,687704187,2077961098,538542442,528815427,534884074,5265567223,1494153617,1749564319,861769159,5135111271,1777632324,1009100017,842447646,658064380,585062110]
        c_id = update.effective_chat.id
        msg = (update.message.text.split()[1])
        print(msg)
        if c_id in my_head:
            if msg != '0':
                
                global mylst
                wtf = True
                mylst.clear()
                mylst.append(msg)
            if msg == '0':
                
                wtf = False


def join(update: Update, context: CallbackContext) -> int:
    #print(update)
    my_head = [1719921402,2077961098,963460963,585062110,1657154573,1083705812,1,687704187,2077961098,538542442,528815427,534884074,5265567223,1494153617,1749564319,861769159,5135111271,1777632324,1009100017,842447646,658064380,585062110 ]
    c_id = update.effective_user.id
    print("hi")
    ghfsdbjf = getnum()
    #update.message.reply_text(ghfsdbjf)
    #context.bot.send_message(chat_id=-1001445021753,text = "hi" )
    #context.bot.send_message(chat_id=-1001445021753,text = "minimum kitna hai?" )
    if c_id in my_head:
        context.bot.send_animation(chat_id=update.effective_chat.id,animation =open(f'{ghfsdbjf}.gif', 'rb'))
    else:
        print("unauthorized")
        


def edit(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    msg_id = context.args[0]
    msg_ = context.args[1:]
    one  = msg_[0]
    two = msg_[1]
    main = "20,43,69,86,45 into 10 \n\nTotal 50"
    print('msg',msg_,msg_id)
    context.bot.edit_message_text(f'{main}', chat_id=-1001584557660, message_id=msg_id)
    
    update.message.reply_text('I will never let you down my boss')

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    ab = input("enetr")
    a=update.message.reply_text(ab)
    print(a)
    msg_id = a.message_id
    t = update.message.text
    ch_id = update.message.chat_id
    m = "edited boss good to go ahead"
    #print(msg_id,ch_id,t)
    context.bot.edit_message_text(f'{m}', chat_id=ch_id, message_id=a.message_id)


    


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("5931513633:AAECrM4HEPTSIdaLsQjsQoeysgtBO3zRxQ0")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("spin", join))
    dispatcher.add_handler(CommandHandler("cp", sett))

    # on non command i.e message - echo the message on Telegram
    #dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
