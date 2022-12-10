import telebot
import utils_for_lessons_pd as utils
commands = { # a dictionary to store all the available commands to present those to a user
    'start'       : 'Get used to the bot',
    'free'        : 'What auditories are free right now',
    'where {Name of teacher}': 'Where is teacher today',
    'now': 'What lessons are going now',
    'help'        : 'Gives you information about the available commands',
}


# markup_free_auditories = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add("Find out")
# clipboard = [markup_free_auditories]
token = '5455514416:AAFsWy97TA08TnNmChLesS8au6tDim0uWB0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_command(m):
    bot.send_message(m.chat.id, "/help for commands")
@bot.message_handler(commands=['free'])
def free123(m):
    bot.send_message(m.chat.id,f"Free auditories: {utils.df_free()}")
@bot.message_handler(commands=['where'])
def adsfree123(m):
    teacher = m.text.partition(" ")[2]
    bot.send_message(m.chat.id,f"{utils.show(utils.df_where(teacher)).to_string()}")
@bot.message_handler(commands=['now'])
def adsfadsfree123(m):
    bot.send_message(m.chat.id,f"{utils.show(utils.df_now()).to_string()}")

@bot.message_handler(commands=['help']) # /help command handleк that will print available commands 
def command_help(m):                    # from the dictionary above
    help_text = "The following commands are available: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(m.chat.id, help_text)

bot.polling(none_stop=True, interval=0) # this is a loop that makes the bot work