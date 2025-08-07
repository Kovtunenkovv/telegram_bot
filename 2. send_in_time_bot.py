import telebot
import time
import datetime
from datetime import datetime

count = 1
now = datetime.now().strftime("%H:%M")
token = '***'                               #toket your bot
bot = telebot.TeleBot(token)
chat_id = '***'                             #id your user
text = 'Good morning!'

while count>=0:
    now = datetime.now().strftime("%H:%M")
    if now == '09:00':
        bot.send_message(chat_id, text) 
        print(now, 'Done')
        time.sleep(59)
    else:
        print(now, 'None')
        time.sleep(59)

#________________________________________________________

import telebot
import time
import datetime
from datetime import datetime

count = 1
now = datetime.now().strftime("%H:%M")
token = '***'                               #toket your bot
bot = telebot.TeleBot(token)
chat_id = '***'                             #id your user
text = 'What happened?'

while count>=0:
    now = datetime.now().strftime("%H:%M")
    if now >= '09:00' and now <= '19:00':
        bot.send_message(chat_id, text) 
        print(now, 'Done')
        time.sleep(59)
    else:
        print(now, 'None')
        time.sleep(900)
