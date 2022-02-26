import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings, planets_feature

# Setting up logging configuration
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Additional proxy settings
PROXY = {'proxy_url': settings.PROXY_URL,
         'urllib3_proxy_kwargs': {
             'username': settings.PROXY_USERNAME,
             'password': settings.PROXY_PASSWORD}}

# Greetings function
def greet_user(update, contex):
    print('Command /start')
    update.message.reply_text('Greetings!!! You sent command /start!')

# Planet function
def planet(update, contex):
    user_text = update.message.text
    user_planet = user_text.split()
    if len(user_planet) > 1:
        answer_text = planets_feature.check_constellation(user_planet[1].capitalize())
    else:
        answer_text = "Please, text planet's name after command /planet"
    print(answer_text)
    update.message.reply_text(answer_text)

# Text function
def talk_to_me(update, contex):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f'You said: {user_text}')

# Picture function
def picture_answer(update, contex):
    update.message.reply_text("Sorry, can't handle pictures yet")
    print('Picture was sent')

# Main function
def main():
    # Initialisation of bot using Updater with bot's key
    mybot = Updater(settings.API_KEY, use_context=True)#, request_kwargs=PROXY)
    
    # Setting up dispatcher
    disp = mybot.dispatcher
    # Configuring handlers for commands
    disp.add_handler(CommandHandler('start', greet_user))
    disp.add_handler(CommandHandler('planet', planet))
    disp.add_handler(MessageHandler(Filters.text, talk_to_me))
    disp.add_handler(MessageHandler(Filters.photo, picture_answer))

    logging.info('Bot started')
    # Enable to chek up updates on Telegram
    mybot.start_polling()
    # Start of our bot
    mybot.idle()

# Start of our main() function
if __name__ == '__main__':
    main()