import telebot;
from telebot import *

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('241a53fd4a30449e2f512d23dd470a4b')
mgr = owm.weather_manager()

token = "5125268199:AAE3cP_Sejf6Ai3e3qX3Bh6J4j-qLKZjyLo"
bot = telebot.TeleBot(token);
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(True,False)
    keyboard.row("Цитата","Поговорка","Анекдот", "/help", "/time", "/weather")
    bot.send_message(message.chat.id, 'Здравствуйте, я бот для лабораторной работы', reply_markup = keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Данный бот умеет рассказывать анекдоты, поговорки, цитаты, а также определять текущее время (используйте команду /time) и погоду (используйте команду /weather) для определения погоды используется сервис OpenWeather')
@bot.message_handler(commands=['time'])
def start_message(message):
    bot.reply_to(message, "Время: " + str(datetime.now()))
@bot.message_handler(commands=['weather'])
def start_message(message):
    observation = mgr.weather_at_place('Moscow, RU')
    w = observation.weather
    w.detailed_status  # 'clouds'
    w.wind()  # {'speed': 4.6, 'deg': 330}
    w.humidity  # 87
    w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    w.rain  # {}
    w.heat_index  # None
    w.clouds  # 75
    temp = w.temperature('celsius')["temp"]
    oblako = w.detailed_status
    bot.send_message(message.chat.id, "Температура в Москве: " + str(temp) + "    Небо: " + oblako)
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "анекдот":
        bot.send_message(message.chat.id, 'Пока в продаже есть хлеб, яйца и пельмени — холостяки так просто не сдадутся.')
    elif message.text.lower() == "поговорка":
        bot.send_message(message.chat.id, 'Роса с вечера выпала — быть ясному дню.')
    elif message.text.lower() == "цитата":
        bot.send_message(message.chat.id, 'Лишь утратив всё до конца, мы обретаем свободу.')
bot.polling( none_stop = True)
