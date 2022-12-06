import os

import time

import logging
import telebot
from telebot import types


logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
TOKEN = os.environ.get('API_KEY')
users = {}
commands = {  # command description used in the "help" command
    'start': 'Get used to the bot',
    'help': 'Gives you information about the available commands',
    'getid': 'try to test message'
}


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.from_user.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener


def validateuser(m, command):
        users.update({m.from_user.username: m.from_user.id})
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


# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    validateuser(m, "start")


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    validateuser(m, "help")


@bot.message_handler(commands=['getid'])
def getid(m):
    users.update({m.from_user.username: m.from_user.id})
    bot.send_message(m.chat.id, m.from_user.id)


@bot.message_handler(commands=['getuserslist'])
def getuserslist(m):
        bot.send_message(m.chat.id, users.keys())


@bot.message_handler(commands=['kill!'])
def kill(message):
    username = message.text[message.text.find('@'):]
    try:
        bot.kick_chat_member(message.chat.id, message.from_user.id)
        bot.send_message(message.chat.id, username + " was deleted from chart")
    except TypeError:
        bot.send_message(message.chat.id, username + " was can't be deleted from chart ERROR!")


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    users.update({m.from_user.username: m.from_user.id})
    bot.send_message(m.chat.id, "I don't understand \"" + m.text + "\"\nMaybe try the help page at /help")


bot.infinity_polling()
