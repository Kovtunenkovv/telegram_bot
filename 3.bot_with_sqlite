import telebot
import sqlite3
bot = telebot.TeleBot('******', parse_mode=None) #TOKEN
def get_db(NE:str) -> list:

    sql_query1 = '''SELECT zip, hostname, firstoccurrence, eventid FROM alarm_daily WHERE hostname ="{}" LIMIT 20'''
    try:
        db_connection = sqlite3.connect('//Users//a//Downloads//9.db')
        db_cursor = db_connection.cursor()

        db_cursor.execute(sql_query1.format(NE))
        db_connection.commit()
        result = db_cursor.fetchall()
        db_cursor.close()

    except sqlite3.Error as error:
        print("Ошибка sqlite", error)
    finally:
        if (db_connection):
            db_connection.close()
            print("Соединение с SQLite закрыто")
            
    return result

@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Send BS")
    elif message.text[0] == 'MO' or message.text[0] == 'MS' or message.text[0] == 'MR' or message.text[0] == 'MC':
        NE = str(message.text)
        data = list()
        data = get_db(NE.upper())
        if data is None:
            bot.send_message(message.from_user.id,"None")
        else:
            s = ""
            for i in data:
                s = s + str(i) + "\n"
            bot.send_message(message.from_user.id, s)
    else:
        bot.send_message(message.from_user.id, "Send me number of BS or send me '/start'")

bot.infinity_polling()
