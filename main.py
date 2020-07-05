import speech_recognition as sr

recognizer = sr.Recognizer() # responsible for recognizing speech

def record_audio:
    with sr.Microphone() as source: # the microphone will be our source
        print("Say something...")
        audio = recognizer.listen(source)
        try:
            voice_data = recognizer.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("Sorry, I did not get that")
        except sr.RequestError:
            print("Sorry, my speech service is down at the moment")

