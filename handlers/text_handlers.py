from aiogram import types
from misc import dp,bot
import requests
from .sqlit import cheak_chat_id,cheak_traf
import random
link = "https://videocdn.tv/api/short?api_token=fHsI6ZjJ6CpgTzc8QUMZjQIVaxOuYHAc&"
title = "title={}&"
id_kk = "kinopoisk_id={}&"

#API кинопоиска:
API_KEY = "7a4e9d3d-8838-44fd-8f64-59ad0262be16" #Токен

def gen_movie_link(movie_link):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='Смотреть', url = movie_link)
    markup.add(bat_a)
    return markup

@dp.message_handler(content_types=['text'])
async def all_other_messages(message: types.message):
    from .commands_start import id_channel_1,id_channel_2,id_channel_3, id_channel_4
    from .commands_start import name_channel_1,name_channel_2,name_channel_3, name_channel_4
    try:
        proverka1 = (await bot.get_chat_member(chat_id=id_channel_1, user_id = message.chat.id)).status
    except:
        proverka1 = 'member'

    try:  # Канал 2
        proverka2 = (await bot.get_chat_member(chat_id=id_channel_2, user_id=message.chat.id)).status
    except:
        proverka2 = 'member'

    try:  # Канал 3
        proverka3 = (await bot.get_chat_member(chat_id=id_channel_3, user_id=message.chat.id)).status
    except:
        proverka3 = 'member'

    try:  # Канал 4
        proverka4 = (await bot.get_chat_member(chat_id=id_channel_4, user_id=message.chat.id)).status
    except:
        proverka4 = 'member'


    if (proverka1 == 'member' and proverka2 == 'member' and proverka3 == 'member' and proverka4 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka3 == 'administrator' or proverka4 == 'administrator' or proverka1 == 'creator' or proverka2 == 'creator' or proverka3 == 'creator' or proverka4 == 'creator':
        try:
            if 'https://www.kinopoisk.ru/' in message.text:
                print()
                id_k = ((message.text).split('/'))[-2]
                print(id_k)
                #answer = (requests.get(url=link + id_kk.format(id_k),headers= headers,proxies=random.choice(proxies))).json()  # Запрос по названию
                answer = (requests.get(timeout=2,url=link + id_kk.format(id_k))).json()  # Запрос по названию
                print('Поиск по id', answer)
            else:
                #answer = (requests.get(url=link + title.format(message.text),headers= headers,proxies=random.choice(proxies))).json()  #Запрос по названию
                print(link + title.format(message.text))
                answer = (requests.get(url=link + title.format(message.text))).json()  # Запрос по названию

            if len(answer['data']) != 0:
                print('ID ыы')
                for i in answer['data']:
                    name_movie = i['title']
                    year = i['year']
                    movie_link = 'https:' + i['iframe_src']
                    kp_id = i['kp_id']
                    previe = f'https://st.kp.yandex.net/images/film_big/{kp_id}.jpg'
                    await bot.send_message(chat_id=message.chat.id, text=f"<a href = '{previe}'>🎥</a> {name_movie} {year}",disable_web_page_preview=False,reply_markup=gen_movie_link(movie_link))
                await message.answer("""Продолжайте писать названия фильмов, мультфильмов или сериалов""")
            else:
                await message.answer("""Вы прислали что то невнятное!
Повторите попытку или отправьте мне ссылку на фильм с сайта https://www.kinopoisk.ru""")
        except: print('Ошибка поиска')
    else:
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='❌ 📣 КАНАЛ 1', url=f"{name_channel_1}")
        bat_b = types.InlineKeyboardButton(text='❌ 📣 КАНАЛ 2', url=f"{name_channel_2}")
        bat_c = types.InlineKeyboardButton(text='❌ 📣 КАНАЛ 3', url=f"{name_channel_3}")
        bat_b4 = types.InlineKeyboardButton(text='❌ 📣 КАНАЛ 4', url=f"{name_channel_4}")
        bat_d = types.InlineKeyboardButton(text='✔️Я ПОДПИСАЛСЯ✔️', callback_data=f"start_watch_0")
        markup.add(bat_a)
        markup.add(bat_b)
        markup.add(bat_c)
        markup.add(bat_b4)
        markup.add(bat_d)
        await message.answer(f"""{message.from_user.full_name}, для использования бота необходимо <b>единоразово</b> подписаться на следующие каналы:""",reply_markup=markup)