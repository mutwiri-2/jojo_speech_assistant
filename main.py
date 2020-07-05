import speech_recognition as sr

recognizer = sr.Recognizer() # responsible for recognizing speech

with sr.Microphone() as source:
    print("Say something...")
    audio = recognizer.listen(source)
    voice_data = recognizer.recognize_google(audio)
    print(voice_data)

