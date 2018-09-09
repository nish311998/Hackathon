import speech_recognition as sr

s = sr.Recognizer()

with sr.Microphone() as source:
    print("Say Something!")
    audio = s.listen(source)

print(audio)

