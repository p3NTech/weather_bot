import requests
import telebot

url = 'http://api.openweathermap.org/data/2.5/weather' #open weather url
api_open_weather = '966cc6ce89188b2bc797546a3487bf55'#ключ open weather api
api_telegram_token = '1687680321:AAHm7NH2ZsagoBAlcfNSV8U5Wwj0U9jhHK0' #токен telegram api
bot = telebot.TeleBot(api_telegram_token)
print("Weather bot [@p3ntech]")#сообщение в консоль
print("initialize")#сообщение в консоль
@bot.message_handler(commands=['start'])#старт
def welcome(message):
    bot.send_message(message.chat.id, f'Привет!  {message.from_user.first_name} \n'
                                      f' напиши название города и узнай погоду в нём. "/help"')#Сообщение при запуске


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     f'/start запуск бота \n'
                     )#сообщение(ответ) на команду /help


@bot.message_handler(content_types=['text'])#обработчик
def test(message):
    city_name = message.text

    try:
        params = {'APPID': api_open_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(url, params=params)#параметры api open weather
        weather = result.json()#экспорт параметров

        if weather["main"]['temp'] < -10:   #при -10
            status = "На улице холодно, одевайтесь теплее! Чтобы согреться, могу предложить Вам сходить в ресторан и выпить чашечку кофе!" 
            bot.send_photo(message.chat.id, 'ссылка на изображение', "")
        elif weather["main"]['temp'] < 0:   #при 0
            status = "Мороз и солнце, день чудесный! Самое время выпить глинтвейн!"
            bot.send_photo(message.chat.id, 'ссылка на изображение', "")
        elif weather["main"]['temp'] < 10:  #при +10
            status = "Погода шепчет, что сегодня вам нужно сходить на каток! Но стоит одеть шапку и шарф!"
            bot.send_photo(message.chat.id, 'ссылка на изображение', "")
        elif weather["main"]['temp'] < 30:  #при +30
            status = "Пейте много воды, на улице жарко!"
            bot.send_photo(message.chat.id, 'ссылка на изображение', "")
        else:   #при +30+
            status = "Не выходите на улицу без надобности и пейте много воды, на улице жарко!"
            bot.send_photo(message.chat.id, 'ссылка на изображение', "")

        bot.send_message(message.chat.id, "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
                         "-------------------------------------------------------------------"
                         "\n" + status)

    except:
        bot.send_photo(message.chat.id, 'ссылка на изображение', "Город " + city_name + " не найден") # сообщение в случае если город не найден
		
print("Started!")#сообщение в консоль
bot.polling(none_stop=True)
print("")
print("Stoped!")#сообщение в консоль
