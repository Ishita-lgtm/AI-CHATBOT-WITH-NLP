import nltk
from nltk.chat.util import Chat, reflections

# 1. Define pairs of patterns and responses
# Format: ('regex pattern', ['list of possible resonses'])
pairs=[
    (r'my name is (.*)', ['Hello %1, how can I help you today?']),
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Greetings!']),
    (r'what is your name?', ['I am a simple Python chatbot.','You can call me as Chatbot v1.']),
    (r'how are you?', ['I am doing great, thank you!','I am just a computer program, but I am functioning well.']),
    (r'quit',['Bye! Take care.', 'It was nice talking to you.']),
    (r'(.*) (location|city) is (.*)', ['%1 is a wonderful place, I have heard much about %3.']),
    (r'(.*)', ['I am sorry, I do not understand that. Could you rephrase?'])
]

def chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    # 2. Create the Chat instance 
    chat=Chat(pairs, reflections)
    # 3. Start the converstion
    chat.converse()

if __name__=="__main__":
    chatbot()