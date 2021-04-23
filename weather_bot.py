import requests
import telebot
import constants

print("")
print("initialize") #сообщение в консоль

bot = telebot.TeleBot(constants.api_telegram_token)

@bot.message_handler(commands=['start']) #старт
def welcome(message):
    bot.send_message(message.chat.id, f'Привет!  {message.from_user.first_name}'
                                      f' напиши название города и узнай погоду в нём. \n' 
                                      f'Для помощи напиши "/help"') #Сообщение при запуске


@bot.message_handler(commands=['help'])
def welcome(message):
    bot.send_message(message.chat.id,
                     f'/start запуск бота \n'
                     ) #сообщение(ответ) на команду /help


@bot.message_handler(content_types=['text']) #обработчик
def test(message):
    city_name = message.text

    try:
        params = {'APPID': constants.api_open_weather, 'q': city_name, 'units': 'metric', 'lang': 'ru'}
        result = requests.get(constants.url, params=params) #параметры api open weather
        weather = result.json() #экспорт параметров

        if weather["main"]['temp'] < -10:   #при -15
            status = "На улице холодно, одевайтесь теплее! Чтобы согреться, могу предложить Вам сходить в ресторан и выпить чашечку кофе! (здесь может быть ваша реклама ресторана)" # random_message1 # 
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение1
	elif weather["main"]['temp'] < 0:   #при 0
            status = "Погода радует!... Можно уже менять зимнюю резину на летнюю)) (реклама сто, шиномонтаж)"  # random_message2 # 
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение2
	elif weather["main"]['temp'] < 10:   #при 0, при -5 не дает запустить бот
            status = "На улице становится теплее. Советую Вам сегодня выйти на пробежку. А чтобы было комфортно бегать, можно приобрести зимние кроссовки в интернет-магазине. (реклама интернет магазина и фото кроссовок, которые у них продаются)"
        elif weather["main"]['temp'] < 30:  #при +10
            status = "На улице заметно теплее! Уличные тренировки в такую погоду самое то! Спортивный инвентарь и подходящую одежду можно посмотреть по ссылке ниже! (реклама шоу-рума или магазина спорттоваров)" # random_message3 # 
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение3
        else:   #при +30+
            status = "Предлагаю ознакомиться с топовыми моделями купальников в этом сезоне! Только сегодня вы можете стать обладательницей шикарного бикини!(реклама магазина купальников)" # random_message5 #
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение5

        bot.send_message(message.chat.id, "Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
                         "-------------------------------------------------------------------"
                         "\n" + status)
    except:
	
        bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Город " + city_name + " не найден ") # сообщение в случае если город не найден
		
print("Started!")
bot.polling(none_stop=True)
print("")
print("Stoped!")
