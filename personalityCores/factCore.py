import pywhatkit
import randfacts
import requests
import flask
from googletrans import Translator
from GoogleNews import GoogleNews

googlenews = GoogleNews()
translator = Translator()

googlenews.set_encode("utf-8")
googlenews.set_lang("de")
googlenews.set_period("1d")

def randomFact():
    en_fact = randfacts.get_fact()
    fact = translator.translate(en_fact, src="en", dest="de")
    return(fact.text)

def weatherFrog():
    api_key = "8ef61edcf1c576d65d836254e11ea420"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = "Achern"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_humidiy = str(y["humidity"]) + "%"
        z = x["weather"]
        current_temperaturetwo = str(round(current_temperature - 273.15, 2)) + " Grad Celsius"
        en_weather_description = z[0]["description"]
        weather_desc = translator.translate(en_weather_description, src="en", dest="de")

        return current_temperaturetwo, current_humidiy, weather_desc.text

    # list_weather = weatherFrog()
    # print(list_weather[0])

def wikiSearches(to_search):
    en_wiki = pywhatkit.info(to_search, lines=2, return_value=True)
    wiki = translator.translate(en_wiki, src="en", dest="de")
    return(wiki.text)

    #print(wikiSearches("dogs"))