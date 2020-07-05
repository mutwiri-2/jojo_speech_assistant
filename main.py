import speech_recognition as sr
import alsa_error_handler

recognizer = sr.Recognizer() # responsible for recognizing speech

def record_audio():
    with alsa_error_handler.noalsaerr():
        with sr.Microphone() as source: # the microphone will be our source
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
    if 'what is your name' in voice_data:
        print('My name is jojo')

print("How can I assist you?")
voice_data = record_audio()
respond(voice_data)