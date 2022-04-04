import telebot
import config
import random
bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Чтобы запустить рандомайзер напиши команду: /random')

@bot.message_handler(commands=['random'])
def get_message(message):
    bot.send_message(message.chat.id, 'Введите диапозон чисел (в виде число-число): ')
    bot.register_next_step_handler(message, get_number)

def get_number(message):
    number = message.text
    try:
        number = number.split('-')
        number = random.randint(int(number[0]), int(number[1])) 
        bot.send_message(message.chat.id, 'Рандомное число: ' + str(number))
    except:
        bot.send_message(message.chat.id, 'Неправильно ввиден диапозон чисел')
 


bot.polling(none_stop=True)