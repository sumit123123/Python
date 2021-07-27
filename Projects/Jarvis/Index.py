import pyttsx3 as sound
import speech_recognition as sr
import datetime as dt
import wikipedia as wiki
import os
from pygame import mixer
import webbrowser as wb


def Speaking(string_speak):
    engine = sound.init()
    engine.setProperty("rate", 250)
    engine.say(string_speak)
    engine.runAndWait()

def Greeting():
    now = dt.datetime.now()

    if (now.hour>12):
        Speaking("Good Afternoon Sir")

    elif (now.hour>17):
        Speaking("Good Evening Sir")

    else:
        Speaking("Good Morning")

    Speaking("How can i help you")

# Greeting()

def Search_wiki():
    
    Speaking("What you want to search")
    input_search = str(input("Enter here:\n"))

    try:
        search_text = wiki.summary(input_search)
        Speaking(search_text)
        print(search_text)
    except Exception as E:
        print(f"Please re-write the search no\nany searches found for\n{input_search}")
# Search_wiki()

def Play_Music():
    path = r"C:\Users\Dell\Music\Playlists"

    path2 = os.chdir(path)

    Speaking("Enter P for pause and N for Next")
    
    for item in os.listdir(path2):

        
        if (item.endswith('.mp3')):
            mixer.init()
            mixer.music.load(item)
            mixer.music.play()

            inp = input("Enter Here:\n")

            if (inp.capitalize() == 'P'):
                mixer.music.pause()
            elif (inp.capitalize() == 'N'):
                continue
            else:
                pass
            
        
        else:
            pass

        

Play_Music()


def Google_search():
    Speaking("Type What you want to search")
    serarch = input("Enter te search\n")

    wb.open_new(f"https://www.google.com/query={serarch}")

# Google_search()

