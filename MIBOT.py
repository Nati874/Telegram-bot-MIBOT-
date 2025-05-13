import api_address as api
import Response_of_bot as R
from telegram.ext import *
import random

print("Intiate.....")


# intro message
def start_message(update, context):
    update.message.reply_text("Welcome! I am MIBOT")
    update.message.reply_text("press /help")

# help messages
def help_message(update, context):
    update.message.reply_text("Write the medical term you want to know.")
    update.message.reply_text("""
    /list : list of words in the bot
    /NRW : non root words(prefixes and suffixes)
    /RW : root words
    /tips : to get random tips
    """)


def handle_message(update, context):
    txt = str(update.message.text).lower()
    response = R.greet(txt)
    update.message.reply_text(response)


# All Term listing code
def list_of_MT(update, context):
    update.message.reply_text(R.Words)


# non-root words
def list_of_NRW(update, context):
    update.message.reply_text(R.NoR)


# Root words
def list_of_RW(update,context):
     update.message.reply_text(R.RoW)


# log Error
def error(update, context):
    print(f'Update {update} caused error {context.error}')


def tips(update, context):
    rand_tip = random.randint(0, R.tips_num-1)
    update.message.reply_text(R.tip_list[rand_tip])


# Main function
def main():
    updater = Updater(api.api_txt, use_context=True)
    disp = updater.dispatcher

    # Start command
    disp.add_handler(CommandHandler("start", start_message))

    # Help command+
    disp.add_handler(CommandHandler("help", help_message))

    # list command
    disp.add_handler(CommandHandler("list", list_of_MT))

    # non-root words command
    disp.add_handler(CommandHandler("NRW", list_of_NRW))

    # Root command
    disp.add_handler(CommandHandler("RW", list_of_RW))

    #Tip command
    disp.add_handler(CommandHandler("tips",tips))

    # Filtering responses to fit the texts
    disp.add_handler(MessageHandler(Filters.text, handle_message))

    disp.add_error_handler(error)

    updater.start_polling(1)

    updater.idle()

main()


