import random

url = 'http://api.openweathermap.org/data/2.5/weather' #open weather url
api_open_weather = '966cc6ce89188b2bc797546a3487bf55'#ключ open weather api
api_telegram_token = '1687680321:AAHm7NH2ZsagoBAlcfNSV8U5Wwj0U9jhHK0' #токен telegram api

message1 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']
message2 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']
message3 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']
message4 = ['1', '2', '3', '4','5']
message5 = ['Сообщение1', 'Сообщение2', 'Сообщение3', 'Сообщение4','Сообщение5']

random_message1 = lambda: random.choice(message1)
random_message2 = lambda: random.choice(message2)
random_message3 = lambda: random.choice(message3)
random_message4 = lambda: random.choice(message4)
random_message5 = lambda: random.choice(message5)


bot.send_photo(message.chat.id, 'http://f0535055.xsph.ru/1/pog2.jpg', "🌡Сейчас в городе " + str(weather["name"]) + " температура " +
str(weather["main"]['temp']) + "°C" + "\n" + "💦Влажность: " + str(int(weather['main']['humidity'])) + "%" + "\n" + "🏘На улице сейчас " + str(weather['weather'][0]["description"]) + "\n"+"Очень холодно, сидим дома!" ) #
