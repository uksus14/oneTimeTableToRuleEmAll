import telebot

commands = { # a dictionary to store all the available commands to present those to a user
    'start'       : 'Get used to the bot',
    'help'        : 'Gives you information about the available commands',
}


# markup_free_auditories = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Find out")
# clipboard = [markup_free_auditories]
token = '5455514416:AAFsWy97TA08TnNmChLesS8au6tDim0uWB0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_command(m):
    f = open("file.txt",'r',encoding = 'utf-8')
    auditories = f.read()
    print(*auditories)
    bot.send_message(m.chat.id,f"Free auditories: {auditories}")

@bot.message_handler(commands=['help']) # /help command handleк that will print available commands 
def command_help(m):                    # from the dictionary above
    help_text = "The following commands are available: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(m.chat.id, help_text)

bot.polling(none_stop=True, interval=0) # this is a loop that makes the bot work