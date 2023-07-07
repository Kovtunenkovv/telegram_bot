import telebot

bot = telebot.TeleBot("***")			#toket your bot

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Im echo bot, can you text me? \nFor example: Hi, Hello, Hey")

@bot.message_handler(func=lambda message: True)

def echo_all(message):
    if message.text == 'Hi':
        bot.reply_to(message, 'Hi, what is your name?')
    elif message.text == 'Hello':
        bot.reply_to(message, 'Hello, tell me about yourself')
    elif message.text == 'Hey':
        bot.reply_to(message, 'Hey, how you doin?')
    else:
    	bot.reply_to(message, 'You said: '+ message.text.title())

bot.infinity_polling()
