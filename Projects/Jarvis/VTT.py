import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    text = r.listen(source)
    r.pause_threshold = 1
    r.energy_threshold = 50
    convert = r.recognize_google(text)

