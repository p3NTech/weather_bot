import requests
import telebot
import constants

print("")
print("initialize") #сообщение в консоль
print("")
print("NURI TOPMO3 :D")

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

        if weather["main"]['temp'] < -10:   #при -10
			 status = ""+
			 bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/pog2.jpg', "🌡Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "💦Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "🏘На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
                         "-------------------------------------------------------------------"
                         "\n"+"❕Очень холодно, сидим дома!" ) #        
        elif weather["main"]['temp'] < 0:   #при 0
			 status = ""+
			 bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/pog2.jpg', "🌡Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "💦Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "🏘На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
                         "-------------------------------------------------------------------"
                         "\n"+"❕На улице холодно, одевайтесь теплее! Чтобы согреться, могу предложить Вам сходить в ресторан и выпить чашечку кофе!" )          
        elif weather["main"]['temp'] < 10:  #при +10
			 status = ""+
			 bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/pog2.jpg', "🌡Сейчас в городе " + str(weather["name"]) + " температура " +
            	         str(weather["main"]['temp']) + "°C" + "\n" +
                         "💦Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "🏘На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
                         "-------------------------------------------------------------------"
                         "\n"+"❕Погода шепчет, что сегодня вам нужно сходить на каток! Но стоит одеть шапку и шарф!" )       
           # bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение3
        elif weather["main"]['temp'] < 30:  #при +30
         	 	 status = ""+
			 bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/pog2.jpg', "🌡Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "💦Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "🏘На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
                         "-------------------------------------------------------------------"
                         "\n"+"❕Пейте много воды, на улице жарко!" )
        else:   #при +30+
		 	 status = ""+
			 bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/pog2.jpg', "🌡Сейчас в городе " + str(weather["name"]) + " температура " +
                         str(weather["main"]['temp']) + "°C" + "\n" +
                         "💦Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
                         "🏘На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
                         "-------------------------------------------------------------------"
                         "\n"+"❕Не выходите на улицу без надобности и пейте много воды, на улице жарко!" )				
            #bot.send_photo(message.chat.id, 'ссылка на изображение', "") # изображение5
        bot.send_message(message.chat.id, status) 
       # bot.send_message(message.chat.id, "Сейчас в городе " + str(weather["name"]) + " температура " +
        #                 str(weather["main"]['temp']) + "°C" + "\n" +
        #                 "Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" +
        #                 "На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+
        #                 "-------------------------------------------------------------------"
         #                "\n" + status)
		
   except: 
	
       bot.send_photo(message.chat.id, 'https://darkside.guru/files/404city.png', "Город " + city_name + " не найден ") # сообщение в случае если город не найден
		
print("Started!")
bot.polling(none_stop=True)
print("")
print("STOP+")
