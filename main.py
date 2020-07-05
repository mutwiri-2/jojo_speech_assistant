import speech_recognition as sr
import alsa_error_handler
from datetime import date
import time
import webbrowser

recognizer = sr.Recognizer() # responsible for recognizing speech

def record_audio(ask=False):
    with alsa_error_handler.noalsaerr():
        with sr.Microphone() as source: # the microphone will be our source
            if ask:
                print(ask)
            audio = recognizer.listen(source)
            voice_data = ''
            try:
                voice_data = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                print("Sorry, I did not get that")
            except sr.RequestError:
                print("Sorry, my speech service is down at the moment")
            return voice_data

def respond(voice_data):
    # get name
    if 'what is your name' in voice_data:
        print('My name is jojo')
    # get today's date
    today = date.today()
    date_today = today.strftime("%B %d, %Y")
    if 'what date is it' in voice_data:
        print('Today\'s date is ' + date_today)
    
    # get the current time
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    if 'what is the time' in voice_data:
        print('The time is ' + current_time)

    # search 
    if 'search' in voice_data:
        search_term = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search_term
        webbrowser.get().open(url)
        print("Here is what I found for " + search_term)

    # find a place on Google maps
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)

time.sleep(1)
print("How can I assist you?")
while True:
    voice_data = record_audio()
    respond(voice_data)