import requests
from bs4 import BeautifulSoup

city = "Zhytomyr"
language_code = "en"

url = f'https://www.google.com/search?q=weather+{city}&ie=UTF-8&hl={language_code}'
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
data_str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
weather_data = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text


data = data_str.split('\n')
time = data[0]
weather_condition = data[1]


# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text

pos = strd.find('Wind')
other_data = strd[pos:]

weather_emojis = {
    "Partly Sunny": "🌤️",
    "Scattered Thunderstorms": "⛈️",
    "Showers": "🌦️",
    "Scattered Showers": "🌧️",
    "Rain and Snow": "🌧️❄️",
    "Overcast": "☁️",
    "Light Snow": "🌨️",
    "Freezing Drizzle": "🌧️❄️☔",
    "Chance of Rain": "🌦️🌧️",
    "Sunny": "☀️",
    "Clear": "🌞",
    "Clear with periodic clouds": "🌤️",
    "Mostly Sunny": "🌤️",
    "Partly Cloudy": "⛅",
    "Mostly Cloudy": "🌥️",
    "Chance of Storm": "⛈️",
    "Rain": "🌧️",
    "Chance of Snow": "❄️🌨️",
    "Cloudy": "☁️",
    "Mist": "🌫️",
    "Storm": "⛈️🌩️",
    "Thunderstorm": "🌩️⛈️",
    "Chance of TStorm": "🌦️⛈️",
    "Sleet": "🌧️❄️",
    "Snow": "❄️",
    "Icy": "❄️🌬️",
    "Dust": "🌫️",
    "Fog": "🌫️",
    "Smoke": "🌫️",
    "Haze": "🌫️",
    "Flurries": "❄️🌨️",
    "Light Rain": "🌧️",
    "Snow Showers": "🌨️🌦️",
    "Hail": "🌨️⛈️",
}

emoji = weather_emojis.get(weather_condition, "❓")

print(emoji)