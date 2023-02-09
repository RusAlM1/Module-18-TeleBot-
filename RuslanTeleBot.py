import telebot
from config import keys, TOKEN
from utils import ConvertionException, CurrencyConverter

bot = telebot.TeleBot(TOKEN)

# приветственное сообщение с привязкой к пользователю.
@bot.message_handler(commands=['start', ])
def start(message: telebot.types.Message):
    text = f'Приветствую, {message.chat.username}, для продолжения работы введите: /help \nЕсли хочешь комплимент -\
отправь голосовое сообщение "Хочу комплимент"'
    bot.reply_to(message, text)

# Делает комплимент голосовому сообщению
@bot.message_handler(content_types=['voice', ])
def repeat(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Твой голос просто божественный. Я влюбляюсь в него снова и снова")


# Вызов помощника.
@bot.message_handler(commands=['help', ])
def help(message: telebot.types.Message):
    text = 'Показать список иностранных валют: /currency \nЧтобы перевести валюту, введите команду в формате:\n<название\
валюты> <в какую валюту перевести> <количество переводимой валюты>'
    bot.reply_to(message, text)

# Валюты.
@bot.message_handler(commands=['currency'])
def currency(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException('Слишком много параметров.')

        quote, base, amount = values
        total_base = CurrencyConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {float(amount)*total_base}'
        bot.send_message(message.chat.id, text)

# # Обрабатываются все документы и аудиозаписи
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass

# На сообщения с фотографией БОТ будет отвечать сообщением «Nice meme XDD»
# @bot.message_handler(content_types=['photo', ])
# def say_lmao(message: telebot.types.Message):
#     bot.reply_to(message, 'Nice meme XDD')

bot.polling()  # команда заставляет работать БОТ непрерывно, при возникновении к.-либо ошибок



