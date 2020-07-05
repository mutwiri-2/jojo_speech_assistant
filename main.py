import speech_recognition as sr

recognizer = sr.Recognizer() # responsible for recognizing speech

def record_audio():
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

print("How can I assist you?")
voice_data = record_audio()
print(voice_data)