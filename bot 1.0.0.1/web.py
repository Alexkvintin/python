from bs4 import BeautifulSoup
import requests
import wget


def get_video():
    resp = requests.get('https://www.youtube.com/watch?v=8zKu3tscnJI')
    info = BeautifulSoup(resp.text, 'lxml')
    video_url = info.find('link', rel="shortlink").get('href')


def get_free_game():
    resp = requests.get('https://freesteam.ru')
    info = BeautifulSoup(resp.text, 'lxml')
    list_free_name = info.find("div", class_='post-thumb')
    last_free_more_info = info.find("div", class_='entry-content')
    return f'{list_free_name.h2.a.text}\n {last_free_more_info.p.text} '


def random_anime():
    resp = requests.get('https://yummyanime.club/random')
    info = BeautifulSoup(resp.text, 'lxml')
    rand_an = info.find("h1")
    return rand_an


def day(data):
    to_info = {}
    to_info_list = []
    resp = requests.get('https://animevost.org')
    info = BeautifulSoup(resp.text, 'lxml')
    web = info.find("div", id=data)
    name = str(web.text).split('\n')[1:-1]
    web_url = str(web).split('\n')[1:-1]
    for i in range(0, len(name)):
        to_info_list.append((name[i], 'https://animevost.org' + web_url[i].split('\"')[1]))
    to_info.update(to_info_list)
    return to_info


def get_city_name(message):
    city = message
    resp = requests.get(f'https://ua.sinoptik.ua/погода-{city}')
    info = BeautifulSoup(resp.text, 'lxml')
    if info.find("body", class_="ua p404") :
        return 'Ошибка...\nНет искомой информации.'
    else :
        num_of_days = []
        new_day_dict = {}
        weather = (info.find("div", class_="tabs").text).split()
        for i in range(0, len(weather), 7):
            days = weather[0 + i:i + 7]
            new_day_dict[days[1]] = ' '.join(days)
            num_of_days.append(days[1])
        return new_day_dict
        # kb = InlineKeyboardMarkup(row_width=2)
        # button = [InlineKeyboardButton(i) for i in num_of_days]
        # kb.add(*button)
        # bot.send_message(message.chat.id, 'Выберите дату', reply_markup=kb)
