import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()


harvard = sr.AudioFile('file.wav')
with harvard as source:
    audio = r.record(source)

print("type(audio):", type(audio))

test_result = r.recognize_google(audio)

print ("test_result:", test_result)
