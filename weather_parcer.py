from bs4 import BeautifulSoup as bs
import requests
import argparse

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"
# US English
LANGUAGE = "en-US,en;q=0.5"


def scrape_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results in this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text

    weather_emojis = {
        "Partly sunny": "🌤️",
        "Scattered thunderstorms": "⛈️",
        "Showers": "🌦️",
        "Scattered showers": "🌧️",
        "Rain and snow": "🌧️❄️",
        "Overcast": "☁️",
        "Light snow": "🌨️",
        "Freezing drizzle": "🌧️❄️☔",
        "Chance of rain": "🌦️🌧️",
        "Sunny": "☀️",
        "Clear": "🌞",
        "Clear with periodic clouds": "🌤️",
        "Mostly sunny": "🌤️",
        "Partly cloudy": "⛅",
        "Mostly cloudy": "🌥️",
        "Chance of storm": "⛈️",
        "Rain": "🌧️",
        "Chance of snow": "❄️🌨️",
        "Cloudy": "☁️",
        "Mist": "🌫️",
        "Storm": "⛈️🌩️",
        "Thunderstorm": "🌩️⛈️",
        "Chance of tstorm": "🌦️⛈️",
        "Sleet": "🌧️❄️",
        "Snow": "❄️",
        "Icy": "❄️🌬️",
        "Dust": "🌫️",
        "Fog": "🌫️",
        "Smoke": "🌫️",
        "Haze": "🌫️",
        "Flurries": "❄️🌨️",
        "Light rain": "🌧️",
        "Snow showers": "🌨️🌦️",
        "Hail": "🌨️⛈️",
    }

    result['emoji'] = weather_emojis.get(result['weather_now'], "❓")
    return result


def get_weather(region):
    URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather&hl=en"
    if region:
        region = region.replace(" ", "+")
        language = '&hl=en'
        URL += f"+{region}+{language}"


    data = scrape_weather_data(URL)
    return data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
    parser.add_argument("region", nargs="?",
                        help="""Region to get weather for. Default is your current location determined by your IP Address.""",
                        default="")

    args = parser.parse_args()
    weather_data = get_weather(args.region)

    # Print the weather data
    print("Weather Data:")
    for key, value in weather_data.items():
        print(f"{key}: {value}")