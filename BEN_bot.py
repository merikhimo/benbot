import random
import telebot
bot = telebot.TeleBot("5630319249:AAFanfvoS6f2B-pZlvd0NoOprG-qiSpu4xk")
from telebot import types
benmessages=["ugh","yes","no","ho-ho-ho"]
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Ben")
        Keyboard=types.InlineKeyboardMarkup()
        CallBn=types.InlineKeyboardButton(text="CALL TO BEN", callback_data="Call")
        Keyboard.add(CallBn)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Дарова, педик")
    if message.text !="Stop" and message.text !="/help" and message.text !="/start" :
        mmsg = random.choice(benmessages)
        bot.send_message(message.from_user.id, mmsg)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Call": 
        msg = random.choice(Y) + ' ' + random.choice(N) + ' ' + random.choice(U) + ' ' + random.choice(X)
        bot.send_message(call.message.chat.id, msg)
bot.polling(none_stop=True, interval=0)
    
    