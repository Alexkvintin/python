from telebot import TeleBot
from telebot.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from config import *
import random
from web import *
from bs4 import BeautifulSoup
import requests

bot = TeleBot(TOKEN)
'''
Прячет ссылку, но текст остается без линка
    # url = 'https://store.steampowered.com'
    # bot.send_message(message.chat.id, f'Текст[.]({url})', parse_mode='markdown')
'''
@bot.message_handler(commands=['start'])
def starting(message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    butt1 = KeyboardButton(text='Выбрать комплектующие')
    butt2 = KeyboardButton(text='Рандомноре число')
    butt3 = KeyboardButton(text='Собрать ПК')
    butt4 = KeyboardButton(text='Зайти в стим')
    butt5 = KeyboardButton(text='>')
    kb.add(butt1, butt2, butt3, butt4, butt5)
    bot.send_message(message.chat.id, f'Приветствую тебя, {message.chat.first_name} !', reply_markup=kb)

# @bot.message_handler(commands=['weather'])
# def weather(message) :
#     bot.send_message(message.chat.id, text='Введите город: ')
#     bot.register_next_step_handler(message, get_city_name)
#
#
# def get_city_name(message) :
#     city = message.text
#     resp = requests.get(f'https://ua.sinoptik.ua/погода-{city}')
#     info = BeautifulSoup(resp.text, 'lxml')
#     if info.find("body", class_="ua p404") :
#         bot.send_message(message.chat.id, 'Ошибка...\nНет искомой информации.')
#     else :
#         num_of_days = []
#         new_day_dict = {}
#         weather = (info.find("div", class_="tabs").text).split()
#         for i in range(0, len(weather), 7) :
#             days = weather[0 + i :i + 7]
#             new_day_dict[days[1]] = ' '.join(days)
#             num_of_days.append(days[1])
#         kb = InlineKeyboardMarkup(row_width=2)
#         button = [InlineKeyboardButton(i) for i in num_of_days]
#         kb.add(*button)
#         bot.send_message(message.chat.id, 'Выберите дату', reply_markup=kb)
#         bot.send_message(message.chat.id, text=new_day_dict[call.data])


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == 'Зайти в стим':
        kr = InlineKeyboardMarkup(row_width=2)
        but1 = InlineKeyboardButton(text='Главная', url='https://store.steampowered.com')
        but2 = InlineKeyboardButton(text='Торговя площадка', url='https://steamcommunity.com/market/')
        but3 = InlineKeyboardButton(text='Статистика', url='https://store.steampowered.com/stats/')
        but4 = InlineKeyboardButton(text='Скидки', url='https://store.steampowered.com/specials')
        but5 = InlineKeyboardButton(text='Чат', url='https://steamcommunity.com/chat/')
        kr.add(but1, but2, but3, but4, but5)
        bot.send_message(message.chat.id, 'Куда пойдём ?', reply_markup=kr)
    elif message.text == 'Собрать ПК':
        bot.send_message(message.chat.id, 'https://telemart.ua/assembly.html')
    elif message.text == 'Рандомноре число':
        bot.send_message(message.chat.id, str(random.randint(1, 100)))
    elif message.text == 'Выбрать комплектующие':
        kb1 = InlineKeyboardMarkup(row_width=2)
        but1 = InlineKeyboardButton(text='Материнские платы', url='https://ek.ua/k187.htm')
        but2 = InlineKeyboardButton(text='Процессоры', url='https://ek.ua/k186.htm')
        but3 = InlineKeyboardButton(text='Видеокарты', url='https://ek.ua/k189.htm')
        but4 = InlineKeyboardButton(text='Блоки питания', url='https://ek.ua/k351.htm')
        but5 = InlineKeyboardButton(text='Оперативная память', url='https://ek.ua/k188.htm')
        but6 = InlineKeyboardButton(text='Жесткие диски', url='https://ek.ua/k190.htm')
        but7 = InlineKeyboardButton(callback_data='more', text='Ещё...')
        kb1.add(but1, but2, but3, but4, but5, but6, but7)
        bot.send_message(message.chat.id, 'Выберите комплектующие.', reply_markup=kb1)
    elif message.text == '>':
        kb = ReplyKeyboardMarkup(resize_keyboard=True)
        butt1 = KeyboardButton(text='Погода')
        butt2 = KeyboardButton(text='Аниме')
        butt3 = KeyboardButton(text='Халявные игры')
        butt4 = KeyboardButton(text='Soon...')
        butt6 = KeyboardButton(text='<')
        kb.add(butt1, butt2, butt3, butt4, butt6)
        bot.send_message(message.chat.id, 'переход...', reply_markup=kb)
    elif message.text == '<':
        kb = ReplyKeyboardMarkup(resize_keyboard=True)
        butt1 = KeyboardButton(text='Выбрать комплектующие')
        butt2 = KeyboardButton(text='Рандомноре число')
        butt3 = KeyboardButton(text='Собрать ПК')
        butt4 = KeyboardButton(text='Зайти в стим')
        butt5 = KeyboardButton(text='>')
        kb.add(butt1, butt2, butt3, butt4, butt5)
        bot.send_message(message.chat.id, 'переход...', reply_markup=kb)
    elif message.text == 'скачать файл':
        bot.send_message(message.chat.id, 'В разработке...')
    elif message.text == 'Погода':
        pass
    #     bot.send_message(message.chat.id, text='Введите город: ')
    #     bot.register_next_step_handler(message, get_city_name(message.text))
    #     if get_city_name(message.text) == True:
    #         kb = InlineKeyboardMarkup(row_width=2)
    #         button = [InlineKeyboardButton(i) for i in num_of_days]
    #         kb.add(*button)
    #         bot.send_message(message.chat.id, 'Выберите дату', reply_markup=kb)
    #     else:
    #         print('error')
    elif message.text == 'Халявные игры':
        bot.send_message(message.chat.id, text=f'ВНИМАНИЕ ! это тестовая функция !\n{get_free_game()}')
    elif message.text == 'Аниме':
        kb = ReplyKeyboardMarkup(resize_keyboard=True)
        butt1 = KeyboardButton(text='Онгоинги')
        butt2 = KeyboardButton(text='Случайное')
        butt3 = KeyboardButton(text='Soon...')
        butt4 = KeyboardButton(text='Soon...')
        butt5 = KeyboardButton(text='<')
        kb.add(butt1, butt2, butt3, butt4, butt5)
        bot.send_message(message.chat.id, 'переход...', reply_markup=kb)
    elif message.text == 'Онгоинги':
        kb1 = InlineKeyboardMarkup(row_width=2)
        button = [InlineKeyboardButton(callback_data=name_of_days[key], text=key) for key in name_of_days]
        kb1.add(*button)
        bot.send_message(message.chat.id, 'Веберите день', reply_markup=kb1)
    elif message.text == 'Случайное':
        bot.send_message(message.chat.id, random_anime())
    elif message.text == 'Soon...':
        bot.send_message(message.chat.id, 'Этот пункт находится в разработке.')
    else:
        bot.send_message(message.chat.id, text=f'у меня нет функции {message.text}')

    @bot.callback_query_handler(func=lambda call: True)
    def callback(call):
        if call.data == 'more':
            hk = InlineKeyboardMarkup(row_width=2)
            button1 = InlineKeyboardButton(text='SSD', url='https://ek.ua/k61.htm')
            button2 = InlineKeyboardButton(text='Корпуса', url='https://ek.ua/k193.htm')
            button3 = InlineKeyboardButton(text='Системы охлаждения', url='https://ek.ua/k303.htm')
            button4 = InlineKeyboardButton(text='Звуковые карты', url='https://ek.ua/k192.htm')
            button5 = InlineKeyboardButton(text='Термопаста', url='https://ek.ua/k247.htm')
            hk.add(button1, button2, button3, button4, button5)
            bot.send_message(call.message.chat.id, 'Выберите комплектующие.', reply_markup=hk)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text='переход...', reply_markup=None)
        # elif bool(days.count(call.data)):
        #     bot.send_message(message.chat.id, new_day_dict[call.data])
        elif call.data == 'raspisMon' or 'raspisTue' or 'raspisWed' or 'raspisThu' or 'raspisFri' or 'raspisSat' or 'raspisSun':
            bot.send_message(call.message.chat.id, 'Подождите немного')
            ikb = InlineKeyboardMarkup(row_width=1)
            buttons = [InlineKeyboardButton(text=i, url=day(call.data)[i]) for i in day(call.data)]
            ikb.add(*buttons)
            bot.send_message(call.message.chat.id, 'Вот какие аниме выходят в этот день:', reply_markup=ikb)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=name_of_days_revers[call.data], reply_markup=None)


if __name__ == '__main__' :
    print('bot start')
    bot.infinity_polling(True)
