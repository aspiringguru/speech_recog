# NLTK demo

https://www.digitalocean.com/community/tutorials/how-to-work-with-language-data-in-python-3-using-the-natural-language-toolkit-nltk


python -c "import nltk"
python -c "import nltk; print(nltk.__version__);"

pip freeze | findstr nltk  

python -m nltk.downloader twitter_samples
python -m nltk.downloader averaged_perceptron_tagger

python -c "from nltk.corpus import twitter_samples; twitter_samples.fileids();"
