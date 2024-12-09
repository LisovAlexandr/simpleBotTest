import telebot
token='2120676466:AAF67HLrzBIrLuk4ehIgomLFZQXC_5dmcG8'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")
bot.infinity_poling()