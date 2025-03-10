import random
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Initialize Lemmatizer
lemmatizer = WordNetLemmatizer()

# Define intents and responses
intents = {
    "greeting": {
        "patterns": ["hi", "hello", "hey", "good morning"],
        "responses": ["Hello!", "Hi there!", "Hey! How can I help?"]
    },
    "goodbye": {
        "patterns": ["bye", "goodbye", "see you"],
        "responses": ["Goodbye!", "See you later!", "Take care!"]
    },
    "thanks": {
        "patterns": ["thanks", "thank you", "appreciate it"],
        "responses": ["You're welcome!", "My pleasure!", "Anytime!"]
    },
    "default": {
        "responses": ["I didn't understand that. Can you rephrase?", "Could you clarify?"]
    }
}

# Process user input
def process_input(user_input):
    tokens = word_tokenize(user_input.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

# Detect intent
def get_intent(user_input):
    processed_input = process_input(user_input)
    for intent, data in intents.items():
        for pattern in data.get("patterns", []):
            if any(word in processed_input for word in process_input(pattern)):
                return intent
    return "default"

# Generate chatbot response
def chatbot_response(user_input):
    intent = get_intent(user_input)
    return random.choice(intents[intent]["responses"])

# Main loop
print("Chatbot: Hi! Type 'exit' to end the chat.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)