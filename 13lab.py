from tkinter import *
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Прогноз Погоды")

        self.cityField = Entry(root) #Создается поле ввода для ввода названия города и привязывается к главному окну root.
        self.cityField.pack()#Этот код отображает поле ввода на экране.

        self.get_weather_button = Button(root, text="Получить прогноз погоды", command=self.get_weather)
        self.get_weather_button.pack()

        self.info = Label(root, justify=LEFT)
        self.info.pack()

    def get_weather(self):
        city = self.cityField.get() #Получает название города из поля ввода.
        key = "a5c0e9f50e10f7bcdb1086756adda9c6"
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': city, 'units': 'metric'} #Устанавливает параметры запроса
        result = requests.get(url, params=params) #Отправляет GET-запрос к указанному URL с указанными параметрами
        weather = result.json() #Получает ответ в формате JSON и сохраняет его в переменной weather
        if 'main' in weather: # проверка есть ли город в файле
            temperature = weather['main']['temp'] #Извлекает температуру из полученной информации о погоде.
            description = weather['weather'][0]['description'] #Извлекает описание погодных условий из полученной информации о погоде.
            self.info.config(text=f'Город: {city}\nТемпература: {temperature}°C\nОписание: {description}') # первые 3 стр оформ
        else:
            self.info.config(text="Город не найден")

        weekly_result = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=params)
        weekly_weather = weekly_result.json()
        weekly_forecast = 'Ежедневный прогноз:\n' #\n стр
        for forecast in weekly_weather['list']:
            date = forecast['dt_txt']
            temperature = forecast['main']['temp']
            weekly_forecast += f'Дата: {date}, Температура: {temperature}°C\n'
        self.info.config(text=f'Город: {city}\nТемпература: {temperature}°C\nОписание: {description}\n\n{weekly_forecast}')
root = Tk()
app = WeatherApp(root)
root.mainloop()