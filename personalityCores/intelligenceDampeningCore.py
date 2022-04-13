import pyjokes
from googletrans import Translator

translator = Translator()

def joke():
    en_joke = pyjokes.get_joke()
    joke = translator.translate(en_joke, src="en", dest="de")
    return (joke.text)