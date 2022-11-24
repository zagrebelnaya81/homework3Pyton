import os

import time

import telebot
from telebot import types


TOKEN = os.environ.get('API_KEY')

commands = {  # command description used in the "help" command
    'start': 'Get used to the bot',
    'help': 'Gives you information about the available commands',
    'test': 'try to test message'
}


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener


def writechats(chatid):
    with open("chats.txt", "w") as file:
        file.write(str(chatid) + '\n')
    file.close()
    return None


def validateuser(m, command):
    if os.environ.get('USER'):
        if int(m.from_user.id) == int(os.environ.get('USER')):
            writechats(m.chat.id)
            if command == 'start':
                bot.send_message(m.chat.id, "Hello!")
                command_help(m)
            elif command == 'help':
                help_text = "The following commands are available: \n"
                for key in commands:  # generate help text out of the commands dictionary defined at the top
                    help_text += "/" + key + ": "
                    help_text += commands[key] + "\n"
                bot.send_message(m.chat.id, help_text)  # send the generated help page
            else:
                command_default(m)
        else:
            writechats(m.chat.id)
            bot.send_message(m.chat.id, "Hello, stranger, you can't use this bot...")
    else:
        bot.send_message(m.chat.id, "NO USER IN CONFIGURATION")
    return None


# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    validateuser(m, "start")


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    validateuser(m, "help")


@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(message.chat.id, message)


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    bot.send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help page at /help")


bot.infinity_polling()
