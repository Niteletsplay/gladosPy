from __future__ import print_function
from urllib.request import urlopen
from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
import requests
import speech_recognition as sr
import pyttsx3
from bs4 import BeautifulSoup
import pywhatkit
import datetime
import webbrowser
import pyjokes
import subprocess
import wolframalpha as wolframalpha
from googlesearch import search
from pynput.keyboard import Key, Controller
from colorama import Style
from tqdm import tqdm
from colorama import Fore
import time
import urllib
import sys
import smtplib
from configparser import ConfigParser


file = "config.ini"
config = ConfigParser()
config.read(file)

loop = tqdm(total=200, position=0, leave=False)
for k in range(200):
    loop.set_description("{}Loading...".format((Fore.GREEN), k))
    loop.update()
    time.sleep(0.0001)

loop.close()

print(f""""{Style.RESET_ALL}{Fore.GREEN}

              .,-:;//;:=,
          . :H@@@MM@M#H/.,+%;,
       ,/X+ +M@@M@MM%=,-%HMMM@X/,
     -+@MM; $M@@MH+-,;XMMMM@MMMM@+-
    ;@M@@M- XM@X;. -+XXXXXHHH@M@M#@/.
  ,%MM@@MH ,@%=             .---=-=:=,.
  =@#@@@MX.,                -%HX$$%%%:;
 =-./@M@M$                   .;@MMMM@MM:
 X@/ -$MM/                    . +MM@@@M$
,@M@H: :@:                    . =X#@@@@-
,@@@MMX, .                    /H- ;@M@M=
.H@@@@M@+,                    %MM+..%#$.
 /MMMM@MMH/.                  XM@MH; =;
  /%+%$XHH@$=              , .H@@@@MX,
   .=--------.           -%H.,@@@@@MX,
   .%MM@@@HHHXX$$$%+- .:$MMX =M@@MM%.
     =XMMM@MM@MM#H;,-+HMM@M+ /MMMX=
       =%@M@M#@$-.=$@MM@@@M; %M%=
         ,:+$+-,/H#MMMMMMM@= =,
               =++%%%%+/:-.

 A.rtificial
 C.hatting
 I.ntelligence
 S.ystem
{Style.RESET_ALL}
""")



if config["main"]["va_gender"] == "none":
    print("Choose Voice: 1 - Male\n"
          "              2 - Female")
    gender = input("")

    if gender == "1":
        print("Voice set to: Male")
        config.set("main", "va_gender", "male")

        with open(file, "w") as configfile:
            config.write(configfile)
    elif gender == "2":
        print("Voice set to: Female")
        print("Voice set to: Male")
        config.set("main", "va_gender", "female")

        with open(file, "w") as configfile:
            config.write(configfile)
    else:
        print("Voice not valid... Choose 1 or 2")
        print("Choose Voice: 1 - Male\n"
              "              2 - Female")
        gender = input("")
        if gender == "1":
            print("Voice set to: Male")
            print("Voice set to: Male")
            config.set("main", "va_gender", "male")

            with open(file, "w") as configfile:
                config.write(configfile)
        elif gender == "2":
            print("Voice set to: Female")
            print("Voice set to: Male")
            config.set("main", "va_gender", "female")

            with open(file, "w") as configfile:
                config.write(configfile)
        else:
            print("Voice not valid. Stopping...")
            sys.exit("Voice option not valid")
elif config["main"]["va_gender"] == "male":
    gender = "1"
elif config["main"]["va_gender"] == "female":
    gender = "2"


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices', "de-DE")
if gender == "1":
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
elif gender == "2":
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"

engine.setProperty('voice', en_voice_id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        if config["client"]["gender"] == "male":
            talk("Hello. Good Morning sir")
            print("Hello. Good Morning, Sir")
        elif config["client"]["gender"] == "female":
            talk("Hello. Good Morning miss")
            print("Hello., Good Morning, Miss")
        elif config["client"]["gender"] == "none":
            talk("Hello. Good Morning")
            print("Hello. Good Morning")
    elif hour >= 12 and hour < 18:
        if config["client"]["gender"] == "male":
            talk("Hello. Good Afternoon sir")
            print("Hello. Good Afternoon, Sir")
        elif config["client"]["gender"] == "female":
            talk("Hello. Good Afternoon miss")
            print("Hello., Good Afternoon, Miss")
        elif config["client"]["gender"] == "none":
            talk("Hello. Good Afternoon")
            print("Hello. Good Afternoon")
    else:
        if config["client"]["gender"] == "male":
            talk("Hello. Good Evening sir")
            print("Hello. Good Evening, Sir")
        elif config["client"]["gender"] == "female":
            talk("Hello. Good Evening miss")
            print("Hello., Good Evening, Miss")
        elif config["client"]["gender"] == "none":
            talk("Hello. Good Evening")
            print("Hello. Good Evening")



wishMe()

def take_command():
    command = False
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
                return command
    except:

        pass
    return command


def take_subcommand():
    subcommand = False
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            subcommand = listener.recognize_google(voice)
            subcommand = subcommand.lower()
            if 'alexa' in subcommand:
                command = subcommand.replace('alexa', '')
                print(subcommand)
                return subcommand
    except:

        pass
    return subcommand



def run_alexa():
    command = take_command()
    if command == False:
        return
    print(command)
    if "talk" in command:
        talk("Great! Lets talk a bit!")
        while True:
            you_ = take_subcommand()

            print("You: " + you_)
            response = chatbot.get_response(you_)
            print("Bot: ", response)
            talk(response)
    elif 'news for today' in command:
        from bs4 import BeautifulSoup, soup
        try:
            news_url = "https://news.google.com/news/rss"
            Client = urlopen(news_url)
            xml_page = Client.read()
            Client.close()
            soup_page = soup(xml_page,"xml")
            news_list = soup_page.findAll("item")
            for news in news_list[:15]:
                talk(news.title.text.encode('utf-8'))
        except Exception as e:
                print(e)
    elif "calculate" in command:
        talk("You want me to calculate something? Alright... Answer these three questions.")
        talk("Tell me the first number")

        num1 = take_subcommand

        talk("Now tell me the operator")

        operator = take_subcommand

        talk("And now the last number")

        num2 = take_subcommand

        talk("Done!")

        num1 = float(num1)
        num2 = float(num2)

        out = None

        if operator == "+":
            out = num1 + num2
        elif operator == "-":
            out = num1 - num2
        elif operator == "*":
            out = num1 * num2
        elif operator == "/":
            out = num1 / num2

        print("Answer: " + str(out))
        talk("The answer is " + str(out))

    elif "volume" in command:
        talk("Do you want to raise the volume or lower it? Say up or down")

        up_or_down = take_subcommand

        if "down" in up_or_down:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == "vlc.exe":
                    print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
                    volume.SetMasterVolume(0.6, None)
        if "up" in up_or_down:
            sessions = AudioUtilities.GetAllSessions()
            for session in sessions:
                volume = session._ctl.QueryInterface(ISimpleAudioVolume)
                if session.Process and session.Process.name() == "vlc.exe":
                    print("volume.GetMasterVolume(): %s" % volume.GetMasterVolume())
                    volume.SetMasterVolume(0.6, None)

    elif "open" in command:
        print(f"""
        Websites, you can open:\n
        1 - Google\n
        2 - GMail\n
        3 - YouTube\n
        4 - {config["web"]["website4"]}\n
        5 - {config["web"]["website5"]}\n
        6 - {config["web"]["website6"]}\n
        7 - {config["web"]["website7"]}\n
        8 - {config["web"]["website8"]}\n
        9 - {config["web"]["website9"]}\n
        10 - {config["web"]["website10"]}\n

        Type the number, to open that website. If you want to add a website, just type the number and then follow those instrcutions.
        """)
        talk("Here are all website you can open. Type the number of the website, to open it. Follow the instructions to customize")

        choice = input("Type here: ")

        if choice == "1":
            url = "https://google.com"
            webbrowser.get().open(url)
            talk("Here you go")
        elif choice == "2":
            url = "https://mail.google.com/"
            webbrowser.get().open(url)
            talk("Here you go")
        elif choice == "3":
            url = "https://www.youtube.com/"
            webbrowser.get().open(url)
            talk("Here you go")
        elif choice == "4":
            if config["web"]["website4"] != "none":
                url = config["web"]["website4"]
                webbrowser.get().open(url)
                talk("Here you go")
            else:
                talk("This number is not sorted to a website. Now enter the full website with 'https://' ")
                print("This number is not sorted to a website. Now enter the full website with 'https://' ")

                new_web = input("Type here: ")

                if "htts://" in new_web:
                    config.set("web", "website4", new_web)

                    with open(file, "w") as configfile:
                        config.write(configfile)
                else:
                    talk("URL does not include htts. Opening cancelled")
                    return
        elif choice == "5":
            if config["web"]["website5"] != "none":
                url = config["web"]["website5"]
                webbrowser.get().open(url)
                talk("Here you go")
            else:
                talk("This number is not sorted to a website. Now enter the full website with 'https://' ")
                print("This number is not sorted to a website. Now enter the full website with 'https://' ")

                new_web = input("Type here: ")

                if "htts://" in new_web:
                    config.set("web", "website5", new_web)

                    with open(file, "w") as configfile:
                        config.write(configfile)
                else:
                    talk("URL does not include htts. Opening cancelled")
                    return
        elif choice == "6":
            if config["web"]["website6"] != "none":
                url = config["web"]["website6"]
                webbrowser.get().open(url)
                talk("Here you go")
            else:
                talk("This number is not sorted to a website. Now enter the full URL with 'https://' ")
                print("This number is not sorted to a website. Now enter the full URL with 'https://' ")

                new_web = input("Type here: ")

                if "htts://" in new_web:
                    config.set("web", "website6", new_web)

                    with open(file, "w") as configfile:
                        config.write(configfile)
                else:
                    talk("URL does not include htts. Opening cancelled")
                    return
        elif choice == "7":
            if config["web"]["website7"] != "none":
                url = config["web"]["website7"]
                webbrowser.get().open(url)
                talk("Here you go")
            else:
                talk("This number is not sorted to a website. Now enter the full URL with 'https://' ")
                print("This number is not sorted to a website. Now enter the full URL with 'https://' ")

                new_web = input("Type here: ")

                if "htts://" in new_web:
                    config.set("web", "website7", new_web)

                    with open(file, "w") as configfile:
                        config.write(configfile)
                else:
                    talk("URL does not include htts. Opening cancelled")
                    return
        elif choice == "8":
            if config["web"]["website8"] != "none":
                url = config["web"]["website8"]
                webbrowser.get().open(url)
                talk("Here you go")
            else:
                talk("This number is not sorted to a website. Now enter the full URL with 'https://' ")
                print("This number is not sorted to a website. Now enter the full URL with 'https://' ")

                new_web = input("Type here: ")

                if "htts://" in new_web:
                    config.set("web", "website8", new_web)

                    with open(file, "w") as configfile:
                        config.write(configfile)
                else:
                    talk("URL does not include htts. Opening cancelled")
                    return
        elif choice == "9":
            if config["web"]["website9"] != "none":
                url = config["web"]["website9"]
                webbrowser.get().open(url)
                talk("Here you go")
            else:
                talk("This number is not sorted to a website. Now enter the full URL with 'https://' ")
                print("This number is not sorted to a website. Now enter the full URL with 'https://' ")

                new_web = input("Type here: ")

                if "htts://" in new_web:
                    config.set("web", "website9", new_web)

                    with open(file, "w") as configfile:
                        config.write(configfile)
                else:
                    talk("URL does not include htts. Opening cancelled")
                    return
        elif choice == "10":
            if config["web"]["website10"] != "none":
                url = config["web"]["website10"]
                webbrowser.get().open(url)
                talk("Here you go")
            else:
                talk("This number is not sorted to a website. Now enter the full URL with 'https://' ")
                print("This number is not sorted to a website. Now enter the full URL with 'https://' ")

                new_web = input("Type here: ")

                if "htts://" in new_web:
                    config.set("web", "website10", new_web)

                    with open(file, "w") as configfile:
                        config.write(configfile)
                else:
                    talk("URL does not include htts. Opening cancelled")
                    return
        else:
            talk("Invalid answer. Opening cancelled")#
            return


    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + time)
    elif "weather" in command:
        api_key = "8ef61edcf1c576d65d836254e11ea420"
        base_url = "https://api.openweathermap.org/data/2.5/weather?"
        talk("whats the city name")
        city_name = take_subcommand()
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            current_temperaturetwo = round(current_temperature - 273.15, 2)
            weather_description = z[0]["description"]
            talk("Heres the weather for " + city_name)
            talk(" Temperature in Celsius is " +
                  str(current_temperaturetwo) +
                  "\n humidity in percentage is " +
                  str(current_humidiy) +
                  "\n description  " +
                  str(weather_description))
            print("Weather for: "+ city_name)
            print(" Temperature in Celsius = " +
                  str(current_temperaturetwo) +
                  "\n humidity (in percentage) = " +
                  str(current_humidiy) +
                  "\n description = " +
                  str(weather_description))
        else:
            talk(" City Not Found ")
    elif 'help' in command:
        print("You can do the following things:\n"
              "\n"
              "Ask me to tell a joke\n"
              "or\n"
              "Ask me about the time\n"
              "or\n"
              "Ask me to play a song\n"
              "or\n"
              "Ask me to send an email\n"
              "or\n"
              "Close ACIS")
        talk("You can do the following things:\n"
             "\n"
             "Ask me to tell a joke\n"
             "or\n"
             "Ask me about the time\n"
             "or\n"
             "Ask me to play a song\n"
             "or\n"
             "Ask me to send an email\n"
             "or\n"
             "Close ACIS")
    elif 'ask' in command:
        talk('I can answer to computational and geographical questions. What question do you want to ask now')
        question = take_subcommand
        app_id = "R2K75H-7ELALHR35X"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        answer = next(res.results).text
        talk(answer)
        print(answer)
    elif "type" in command:
        talk("What do you want me to write?")

        text = take_subcommand

        keyboard = Controller()
        keyboard.type(text)
    elif "note" in command:

        talk("What do you want me to note?")

        to_note = take_subcommand()

        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"

        with open(file_name, "w") as f:
            f.write(to_note)

        subprocess.Popen(["notepad.exe", file_name])
    elif "my name" in command:
        if config["client"]["first_name"] != "none":
            talk("Your name is " + config["client"]["first_name"] + config["client"]["last_name"])
        else:
            talk("I dont know. Can you tell me, so i will remember next time?")
            f_n = input("Can you tell me your first name, so i will remember next time?\n"
                        "")

            config.set("client", "first_name", f_n)

            with open(file, "w") as configfile:
                config.write(configfile)

            talk("So your first name is " + f_n + " Can you please also tell me your last name?")
            l_n = input("Can you tell me your last name too, so i will remember next time?\n"
                        "")

            config.set("client", "last_name", l_n)

            with open(file, "w") as configfile:
                config.write(configfile)

            talk(f"Nice! So your full name is {f_n} {l_n}.")
    elif "my gender" in command:
        if config["client"]["gender"] != "none":
            talk("You are " + config["client"]["gender"])
        else:
            talk("I dont know... Can you tell me?")

            gend = input("What is your gender? Choose 1 or 2.   1 - Male\n"
                         "                                      2 - Female")

            if gend == "1":
                talk("You are registered as male.")

                config.set("client", "gender", "male")

                with open(file, "w") as configfile:
                    config.write(configfile)
            elif gend == "2":
                talk("You are registered as female.")

                config.set("client", "gender", "female")

                with open(file, "w") as configfile:
                    config.write(configfile)
            else:
                talk("That is an invalid answer... Please try again next time!")
                return
    elif "location" in command:
        location = take_subcommand()

        url = "https://google.com/maps/place/" + location + "/amp;"
        webbrowser.get().open(url)
        talk(f"Heres what ive found for {location}")
    elif "search" in command:
        talk("What do you want to search for?")
        query = take_subcommand()

        for j in search(query, tld="com", num=10, stop=10, pause=2):
            print(j)

        talk(f"Heres what ive found for {query}")
    elif "quit" in command:
        talk("Do you want to exit ACIS? Please say yes or no")
        print("Do you want to exit A.C.I.S? Say yes or no")

        subcommand = take_subcommand()

        if "yes" in subcommand:
            talk("Quitting...")
        elif "no" in subcommand:
            talk("Quitting canceled")
        else:
            talk("Invalid answer. Quitting cancelled")
            return
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "wikipedia" in command:
        talk("What should i search for on wikipedia?")
        to_search = take_subcommand()

        talk(pywhatkit.info(to_search, lines=5))
    elif "your name" in command:
        talk("My name is A.C.I.S")
        talk("It means:\n"
             "Artificial\n"
             "Chatting\n"
             "Intelligence\n"
             "System")
    elif "message" in command:
        if config["mail"]["pw"] != "none":
            talk(
                "You are try to send an email? We dont want any issues in misunderstanding, etc. so you have to type this by yourself")

            talk("Please enter the email adress, of the person, that should recieve the mail")
            rec_mail = input("Please enter the email adress, from the person, that should recieve the mail: ")

            talk("Now as a last step, enter the message.")
            message = input("Now as last step, enter the message: ")

            sender_mail = config["mail"]["adress"]
            mail_pw = config["mail"]["pw"]
            server = config["mail"]["server"]
            server = smtplib.SMTP(server, 587)
            server.starttls()
            server.login(sender_mail, mail_pw)
            print("Login success")
            talk("Login success")
            server.sendmail(sender_mail, rec_mail, message)
            print("Email has been sent to " + rec_mail)
            talk("Email has been sent to " + rec_mail)
        else:
            talk("You are trying to send an email, but i dont have you in my config yet. Please enter the following informations first.")

            talk("Please enter the email adress, of the person, that should send the mail")
            sender_mail = input("Please enter the email adress, from the person, that should send the mail: ")

            config.set("mail", "adress", sender_mail)
            with open(file, "w") as configfile:
                config.write(configfile)


            talk("Please enter the email-server, from the account, that you want to send the mail from.")
            print("Please enter E-Mail server, from the account, that you want to send the mail from: 1 - Gmail\r"
                  "                                                                                   2 - Yahoo\r"
                  "                                                                                   3 - Outlook")
            mail_server = input(str(""))
            if mail_server == 1:
                config.set("mail", "server", "smtp.gmail.com")
                with open(file, "w") as configfile:
                    config.write(configfile)
            elif mail_server == 2:
                config.set("mail", "server", "smtp.mail.yahoo.com")
                with open(file, "w") as configfile:
                    config.write(configfile)
            elif mail_server == 3:
                config.set("mail", "server", "smtp-mail.outlook.com")
                with open(file, "w") as configfile:
                    config.write(configfile)
            else:
                print("Invalid option. Try again")
                talk("Invalid option. Try again")
                talk("Please enter the email-server, from the account, that you want to send the mail from.")
                print("Please enter E-Mail server, from the account, that you want to send the mail from: 1 - Gmail\r"
                      "                                                                                   2 - Yahoo\r"
                      "                                                                                   3 - Outlook")
                mail_server = input(str(""))
                if mail_server == 1:
                    config.set("mail", "server", "smtp.gmail.com")
                    with open(file, "w") as configfile:
                        config.write(configfile)
                elif mail_server == 2:
                    config.set("mail", "server", "smtp.mail.yahoo.com")
                    with open(file, "w") as configfile:
                        config.write(configfile)
                elif mail_server == 3:
                    config.set("mail", "server", "smtp-mail.outlook.com")
                    with open(file, "w") as configfile:
                        config.write(configfile)
                else:
                    print("Invalid option. Sending cancelled")
                    talk("Invalid option. Sending cancelled")
                    return

            talk("Please enter the Password, from the account, that you want to send the mail from.")
            mail_pw = (str("Please enter the Password, from the account, that you want to send the mail from: "))

            config.set("mail", "pw", mail_pw)
            with open(file, "w") as configfile:
                config.write(configfile)

            talk("Everything is finally ready to go! Just say the command again to send an email!")

    elif "my age" or "my birthday" in command:
        if config["client"]["bday_year"] != "none":
            talk("You are " + config["client"]["age"] + " years old. You are born at " + config["client"][
                "bday_day"] + "." + config["client"]["bday_month"] + "." + config["client"]["bday_year"])
        else:
            talk("I dont know. Please tell me your age")

            age_ = input("Tell me your age")
            config.set("client", "age", age_)
            with open(file, "w") as configfile:
                config.write(configfile)

            talk("Now tell me the day you were born. Use Numbers")

            bday_day_ = input("Enter the day you were born. (Number 1-31)")
            config.set("client", "bday_day", bday_day_)
            with open(file, "w") as configfile:
                config.write(configfile)

            talk("Now your month. Still in numbers from one to twelve")

            bday_month_ = input("Enter the month you were born in. (Number 1-12)")
            config.set("client", "bday_month", bday_month_)
            with open(file, "w") as configfile:
                config.write(configfile)

            talk("And as last thing, tell me the year you were born.")

            bday_year_ = input("Enter the year you were born.")
            config.set("client", "bday_year", bday_year_)
            with open(file, "w") as configfile:
                config.write(configfile)

            talk("Great!")


        #SocialInteraction

    elif 'hello' in command:
        talk('Hi')
    elif "hi" in command:
        talk("Hey!")
    elif "hey" in command:
        talk("Heyho!")
    elif "how are" in command:
        talk("I am fine, how about you?")
    elif "stupify" in command:
        talk("protego!")
    elif "up up down down left right left right a b a b" in command:
        talk("Ultra Acis activated. Unlimited coins unlocked")
    else:
        talk('Please say the command again.')

while True:
    run_alexa()