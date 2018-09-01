#https://chatterbot.readthedocs.io/en/stable/quickstart.html#create-a-new-chat-bot
#pip install chatterbot

from chatterbot.trainers import ListTrainer

from chatterbot import ChatBot
chatbot = ChatBot("Ron Obvious")

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)

response = chatbot.get_response("Good morning!")
print(response)
