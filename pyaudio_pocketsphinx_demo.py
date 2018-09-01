#from https://www.codesofinterest.com/2017/03/python-speech-recognition-pocketsphinx.html

# pip install pocketsphinx
# pip install SpeechRecognition

import speech_recognition as sr

 # obtain audio from the microphone
r = sr.Recognizer()
mic = sr.Microphone()


with mic as source:
    print("Please wait. Calibrating microphone...")
    r.adjust_for_ambient_noise(source, duration=5)
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
print("processing voice into text.")

try:
    print("Sphinx thinks you said '" + r.recognize_sphinx(audio) + "'")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
