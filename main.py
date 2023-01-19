from telegram.ext import *

import keys

print('Starting up bot...')

def start_command(update,context):
    update.message.reply_text('Hello there i\'m a bot. Nice to meet you ')


def help_command(update,context):
    update.message.reply_text('Try type anything and i will responde')

def custom_command(update,context):
    update.message.reply_text('this is a custom command!')

def handle_response(text : str):
    if 'hello' in text:
            return 'heyoooo!'
        
    if 'how are you' in text : 
            return 'I\'m goodie des!'
    
def handle_message(update,context):
     message_type = update.message.chat.type()
     text = str(update.message.text).lower()
     response = ''

     if message_type == 'group':
          if'@mrbytesbot' in text : 
               new_text = text.replace('@EmilysBot','').strip()
               response = handle_response(new_text)

     else:
        response = handle_response(text)

        update.message.reply_text(response)


def error(update, context):
     print('update {update} caused error : {context.error}')

if __name__ == "--main--":
     updater = Updater(keys.token, use_context = True)
     dp = updater.dispatcher
     #Commands
     dp.add_handler(CommandHandler('start', start_command))
     dp.add_handler(CommandHandler('help', help_command))
     dp.add_handler(CommandHandler('custom', custom_command))
    #  dp.add_handler(CommandHandler('start', start_command))


# Mesages
     dp.add_handler(MessageHandler(Filters.text, handle_message))

# Errors
     dp.add_error_handler(error)
# Run bot : check for updates every 1second
     updater.start_polling(1.0)
     updater.idle()
