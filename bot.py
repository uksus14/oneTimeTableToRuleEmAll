import telebot
import utils_for_lessons_pd as utils
commands = {
    'start': 'Get used to the bot',
    'help': 'Gives you information about the available commands',
    'free': 'What auditories are free right now',
    'where {Name of teacher}': 'Where is teacher today',
    'now': 'What lessons are going now',
}
TODO = {
    'cab {Cab name or lab for every lab}': 'show when the cabinet is free',
}


token = '5455514416:AAFsWy97TA08TnNmChLesS8au6tDim0uWB0'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_cmd(m):
    bot.send_message(m.chat.id, "/help for commands")
@bot.message_handler(commands=['free'])
def free_cmd(m):
    bot.send_message(m.chat.id,f"Free auditories: {utils.df_free()}")
@bot.message_handler(commands=['where'])
def where_cmd(m):
    teacher = m.text.partition(" ")[2]
    bot.send_message(m.chat.id,f"{utils.show(utils.df_where(teacher)).to_string()}")
@bot.message_handler(commands=['now'])
def now_cmd(m):
    bot.send_message(m.chat.id,f"{utils.show(utils.df_now()).to_string()}")
@bot.message_handler(commands=['cab'])
def cab_cmd(m):
    cab = m.text.partition(" ")[2]
    bot.send_message(m.chat.id,f"{utils.show(utils.df_cab_free(cab)).to_string()}")
@bot.message_handler(commands=['overlap'])
def overlap_cmd(m):
    instructions = m.text.split()[1:]
    bot.send_message(m.chat.id,f"{utils.execute(instructions).to_string()}")


@bot.message_handler(commands=['help'])
def command_help(m):
    help_text = "The following commands are available: \n"
    for key in commands:
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(m.chat.id, help_text)

bot.polling(none_stop=True, interval=0)