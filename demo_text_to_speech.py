#pip install pyttsx3
#pip install pypiwin32

#https://pypi.org/project/pyttsx3/

import pyttsx3;
engine = pyttsx3.init();
voices = engine.getProperty('voices')
print(voices)
print(type(voices))
engine.say("I will speak this text");
engine.runAndWait() ;
#male voice

engine.setProperty('voice', voices[0].id) #change index to change voices
engine.say("I will speak this text");
engine.runAndWait() ;
#male voice

engine.setProperty('voice', voices[1].id) #change index to change voices
engine.say("I will speak this text");
engine.runAndWait() ;
#female voice
