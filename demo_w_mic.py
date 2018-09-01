#https://python-sounddevice.readthedocs.io/en/0.3.11/
#alternative method



import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()

mic = sr.Microphone()
#print(".list_microphone_names() : ", sr.Microphone.list_microphone_names())

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print("type(audio):", type(audio))
print ("processing data start")
test_result = r.recognize_google(audio)

print ("test_result:", test_result)
