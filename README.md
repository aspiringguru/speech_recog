# speech_recog

starting with tutorial
https://realpython.com/python-speech-recognition/



https://github.com/mdn/web-speech-api/tree/master/speech-color-changer


#spacy_tut
https://spacy.io/usage/
NB: virtual env install instructions on spacy_tut are out of date.

pip install virtualenv
#check if virtualenv is installed
pip freeze | grep virtualenv

virtualenv mypython
./mypthon/Scripts/activate


pip install -U spacy
python -m spacy download en

#long sloow install process.
copy files from
C:\2018_working\git_repos\speech_recog\spacy_tut\mypython\Lib\site-packages\en_core_web_sm\
to
C:\2018_working\git_repos\speech_recog\spacy_tut\mypython\Lib\site-packages\spacy\data\en

#then test in python interpreter using this code
import spacy
nlp = spacy.load("en")
type(nlp)
