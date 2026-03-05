import re
import datetime
import random

knowledge_base = {
    "what is ai": "AI (Artificial Intelligence) is the simulation of human intelligence in machines.",
    "what is machine learning": "Machine Learning is a subset of AI that allows systems to learn from data.",
    "what is deep learning": "Deep Learning is a subset of Machine Learning based on neural networks.",
    "what is nlp": "NLP (Natural Language Processing) enables computers to understand human language.",
}

intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning", "good evening"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help you?"]
    },
    "help": {
        "patterns": ["help", "what can you do", "support"],
        "responses": ["I can answer AI-related questions and do small talk!"]
    },
    "smalltalk": {
        "patterns": ["how are you", "what's up", "how is it going"],
        "responses": [
            "I'm just a bot, but I'm doing great!",
            "All good here! How about you?",
            "I'm functioning perfectly!"
        ]
    },
    "bye": {
        "patterns": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "See you later!", "Have a nice day!"]
    }
}

def match_intent(user_input):
    text = user_input.lower()

    # Knowledge base check
    for question in knowledge_base:
        if question in text:
            return knowledge_base[question]

    # Intent check
    for intent in intents.values():
        for pattern in intent["patterns"]:
            if re.search(pattern, text):
                return random.choice(intent["responses"])

    return "Sorry, I don't understand that. Try asking about AI."


def log_conversation(user_input, bot_response):
    with open("chat_history.txt", "a", encoding="utf-8") as file:
        time = datetime.datetime.now()
        file.write(f"{time}\nUser: {user_input}\nBot: {bot_response}\n\n")


print("Simple Rule-Based Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = match_intent(user_input)
    print("Bot:", response)

    log_conversation(user_input, response)

