🎮 How to Use the Chatbot
Step 1: Install Dependencies
Make sure you have Python 3 installed. Then, install the required libraries:

bash
Copy
pip install -r requirements.txt  
Step 2: Download NLTK Datasets
Run these commands in a Python shell to download NLTK tokenizers and lemmatizers:

python
Copy
import nltk  
nltk.download('punkt')  
nltk.download('wordnet')  
Step 3: Run the Chatbot
Start the chatbot using the command:

bash
Copy
python chatbot.py  
Step 4: Chat with the Bot
Type your message after the You: prompt.

To exit, type exit.

Example Conversation
Chatbot: Hi! Type 'exit' to end the chat.  
You: Hello  
Chatbot: Hi there! How can I help?  
You: Thanks  
Chatbot: You're welcome!  
You: What’s the weather today?  
Chatbot: I didn’t understand that. Can you rephrase?  
You: exit  
Chatbot: Goodbye!
