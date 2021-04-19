import requests
import telebot
import random

url = 'http://api.openweathermap.org/data/2.5/weather' #open weather url
api_open_weather = ''#ключ open weather api
api_telegram_token = '' #токен telegram api
bot = telebot.TeleBot(api_telegram_token)
print("")
print("Weather bot [Telegram: @p3ntech]") #сообщение в консоль
print("initialize") #сообщение в консоль

message1 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']
message2 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']
message3 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']
message4 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']
message5 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']

random_message1 = lambda: random.choice(message1)
random_message2 = lambda: random.choice(message2)
random_message3 = lambda: random.choice(message3)
random_message4 = lambda: random.choice(message4)
random_message5 = lambda: random.choice(message5)

@bot.message_handler(commands=['start']) #старт
def welcome(message):
    bot.send_message(message.chat.id, f'Привет!  {message.from_user.first_name}'
                                      f' напиши название города и узнай погоду в нём. \n' 
                                      f' Для помощи напиши "/help"') #Сообщение при запуске


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     f'/start запуск бота \n'
                     ) #сообщение(ответ) на команду /help


@bot.message_handler(content_types=['text']) #обработчик
def test(message):
    city_name = message.text

    try:
        params = {'APPID': api_open_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params) #параметры api open weather
        weather = result.json() #экспорт параметров

        if weather["main"]['temp'] < -10:   #при -10
            status = "На улице холодно, одевайтесь теплее! Чтобы согреться, могу предложить Вам сходить в ресторан и выпить чашечку кофе!"  #random_message1 # 
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение1
        elif weather["main"]['temp'] < 0:   #при 0
            status = "Мороз и солнце, день чудесный! Самое время выпить глинтвейн!" # random_message2 # 
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение2
        elif weather["main"]['temp'] < 10:  #при +10
            status = "Погода шепчет, что сегодня вам нужно сходить на каток! Но стоит одеть шапку и шарф!" # random_message3 # 
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение3
        elif weather["main"]['temp'] < 30:  #при +30
            status = "Пейте много воды, на улице жарко!" # random_message4 # 
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение4
        else:   #при +30+
            status = "Не выходите на улицу без надобности и пейте много воды, на улице жарко!" # random_message5 # 
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение5

        bot.send_message(message.chat.id, "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
                         "-------------------------------------------------------------------"
                         "\n" + status)
    except:
        bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Город " + city_name + " не найден") # сообщение в случае если город не найден
		
print("Started!")
bot.polling(none_stop=True)
print("")
print("Stoped!")
