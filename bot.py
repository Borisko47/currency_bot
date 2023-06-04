import telebot
from config import TOKEN, currency
from utils import ConvertionException, CurrencyMethod

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def instruction(message: telebot.types.Message):
    text = '''Для начала работы бота, введите команду в следующем формате:\n <имя валюты><в какую валюту хотите перевести> \
    <количество переводимой валюты>\n Чтобы узнать доступные валюты введите команду /values'''
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in currency.keys():
        text = "\n".join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException("Должно быть всего 3 параметра!")

        quote, base, amount = values
        total_base = CurrencyMethod.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя..\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Бот не может обработать запрос...\n{e}')
    else:
        text = f'{amount} {currency[quote]} это {round(total_base, 2)} {currency[base]}'
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)


# # import requests
# # import lxml.html
# # from lxml import etree
# #
# # # html = requests.get('https://www.python.org/')
# #
# # tree = etree.parse('Добро пожаловать в Python.org.html', lxml.html.HTMLParser())
# #
# # ul = tree.findall('//*[@id="content"]/div/section/div[2]/div[1]/div/ul/li')
# #
# # for li in ul:
# #     a = li.find('a')
# #     print(a.text)
#
#
# # html = requests.get('https://www.python.org/').content
# #
# # tree = lxml.html.document_fromstring(html)
# # title = tree.xpath('/html/head/title/text()')
# #
# # print(title)
#
# # import redis
# # import json
# #
# # red - redis.Redis(
# #     host=
# #     port=
# #     password=
# # )
#
# while True:
#     action = input('Какую команды выполнить:\t')
#     if action == 'write':
#         name = input('name:\t')
#         phone = input('phone:\t')
#         red.set(name, phone)
#     elif action == 'read':
#         name = input('name:\t')
#         phone = red.get(name)
#         if phone:
#             print(f'{name} имеет номер {str(phone)}')
#     elif action == 'delete':
#         name = input('name:\t')
#         phone = red.delete(name)
#         if phone:
#             print(f'{name} номер удалён')
#         else:
#             print(f'Нет такого')
#     elif action == 'stop':
#         break

