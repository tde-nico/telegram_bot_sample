import telebot

API_TOKEN = '' # put the API token here

bot = telebot.TeleBot(API_TOKEN)


# Handle commads like '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Hello')

# Handle text messages
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == 'test':
    	bot.reply_to(message, 'success')
    else:
    	bot.reply_to(message, 'message was not test')


bot.polling()
