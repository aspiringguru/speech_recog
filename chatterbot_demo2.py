#https://chatterbot.readthedocs.io/en/stable/quickstart.html#create-a-new-chat-bot
#pip install chatterbot


from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

chatterbot = ChatBot("Training Example")
chatterbot.set_trainer(ChatterBotCorpusTrainer)

chatterbot.train(
    #"chatterbot.corpus.english"
    #use subsets of english corpus as below
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)

response = chatterbot.get_response("Good morning!")
print(response)

#todo: while true repeat loop to keep chatbot going
#todo: enable selection fo different trained chatbots for diff tasks
#add voice input and output
