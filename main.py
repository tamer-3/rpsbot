import telebot
from telebot import types
import string
import random

bot = telebot.TeleBot('1028255404:AAE_nuUhbWEOB3YoLxI-lWY9Z8DnAFzJ6pE')

@bot.message_handler(commands = ['start'])
def start_message(message):
    m=bot.send_message(message.chat.id, "Привет")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['/game', '/mail']])
    bot.send_message(message.chat.id, 'Ты можешь сыграть камень ножницы бумага или же я придумаю тебе все нужное для гугл аккаунта', reply_markup=keyboard)
    bot.register_next_step_handler(m, name)

@bot.message_handler(commands = ['mail'])
def start_message(message):
    m = bot.send_message(message.chat.id, "Что выберешь сначала?")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Имя', 'Фамилия', 'Почта']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['/back', 'Пароль']])
    bot.send_message(message.chat.id, 'Ну давай,давай нажимай', reply_markup=keyboard)
    bot.register_next_step_handler(m, name)

@bot.message_handler(commands = ['game'])
def start_message(message):
    m = bot.send_message(message.chat.id, "Играем!")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Камень', 'Ножницы', 'Бумага']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['/back', 'Стикер']])
    bot.send_message(message.chat.id, 'Ходи первым!', reply_markup=keyboard)
    bot.register_next_step_handler(m, name)

@bot.message_handler(commands=['back'])
def start_message(message):
    m = bot.send_message(message.chat.id, "Вернулся?")
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['/game']])
    keyboard.add(*[types.KeyboardButton(name) for name in ['/mail']])
    bot.send_message(message.chat.id, 'Так сыграешь или как?', reply_markup=keyboard)
    bot.register_next_step_handler(m, name)

@bot.message_handler(content_types=['text'])
def message(message):
    if message.text == 'Имя':
        a = list('йцукенгшщзхъфывапролджэячсмитьбюё')
        A = list('ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ')
        First = random.choice(A)
        sec = random.choice(a)
        third = random.choice(a)
        fourth = random.choice(a)
        fifth = random.choice(a)
        sixth = random.choice(a)
        seventh = random.choice(a)
        eighth = random.choice(a)
        bot.send_message(message.chat.id, 'Имя: '+First+sec+third+fourth+fifth+sixth+seventh+eighth)
    elif message.text == 'Фамилия':
        a = list('йцукенгшщзхъфывапролджэячсмитьбюё')
        A = list('ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ')
        First = random.choice(A)
        sec = random.choice(a)
        third = random.choice(a)
        fourth = random.choice(a)
        fifth = random.choice(a)
        sixth = random.choice(a)
        seventh = random.choice(a)
        eighth = random.choice(a)
        bot.send_message(message.chat.id, 'Фамилия: '+First+sec+third+fourth+fifth+sixth+seventh+eighth+"баев")
    elif message.text == 'Почта' :
        First = random.choice(string.ascii_uppercase)
        sec = random.choice(string.ascii_lowercase)
        third = random.choice(string.ascii_lowercase)
        fourth = random.choice(string.ascii_lowercase)
        fifth = random.choice(string.ascii_lowercase)
        sixth = random.choice(string.ascii_lowercase)
        seventh = random.choice(string.ascii_lowercase)
        eighth = random.choice(string.ascii_lowercase)
        ninth = str(random.randint(1, 999))
        bot.send_message(message.chat.id, 'Почта: '+First+sec+third+fourth+fifth+sixth+seventh+eighth+ninth+'@gmail.com')
    elif message.text == 'Пароль':
        First = random.choice(string.ascii_uppercase)
        sec = random.choice(string.ascii_lowercase)
        third = random.choice(string.ascii_lowercase)
        fourth = random.choice(string.ascii_lowercase)
        fifth = random.choice(string.ascii_lowercase)
        sixth = random.choice(string.ascii_lowercase)
        seventh = random.choice(string.ascii_lowercase)
        ninth = str(random.randint(1, 999))
        bot.send_message(message.chat.id,'Пароль: '+First+sec+third+fourth+fifth+sixth+seventh+'_'+ninth)

@bot.message_handler(content_types=['text'])
def name(message):
    if message.text == 'Камень':
       if random.randint(1, 3) == 1:
           bot.send_message(message.chat.id, "Камень.Ничья./game - новая игра")
       elif random.randint(1, 3) == 2:
           bot.send_message(message.chat.id, 'Ножницы.Я Проиграл./game - новая игра')
       elif random.randint(1, 3) == 3:
           bot.send_message(message.chat.id, 'Бумага.Я Выиграл./game - новая игра')
    elif message.text == 'Ножницы':
        if random.randint(1, 3) == 1:
            bot.send_message(message.chat.id, 'Камень.Я Выиграл./game - новая игра')
        elif random.randint(1, 3) == 2:
            bot.send_message(message.chat.id, 'Ножницы.Ничья./game - новая игра')
        elif random.randint(1, 3) == 3:
            bot.send_message(message.chat.id, 'Бумага.Я Проиграл./game - новая игра')
    elif message.text == 'Бумага':
        if random.randint(1, 3) == 1:
            bot.send_message(message.chat.id, 'Камень.Я Проиграл./game - новая игра')
        elif random.randint(1, 3) == 2:
            bot.send_message(message.chat.id, 'Ножницы.Я Выиграл./game - новая игра')
        elif random.randint(1, 3) == 3:
            bot.send_message(message.chat.id, 'Бумага.Ничья./game - новая игра')
    elif message.text == 'Стикер':
        bot.send_message(message.chat.id, '''
        Стикеры по камень ножницам бумаге лол 
        https://t.me/addstickers/R_P_S_MIDTERM (зачем?)
        /game - новая игра''')


bot.polling()