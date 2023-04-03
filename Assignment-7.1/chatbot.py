import os
import openai
import json
from llama_index import SimpleDirectoryReader
from llama_index import GPTSimpleVectorIndex

os.environ['OPENAI_API_KEY'] = "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"
openai.api_key = "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"


class Chatbot:
    def __init__(self, api_key, index):
        self.index = index
        openai.api_key = api_key
        self.chat_history = []

    def generate_response(self, user_input):
        prompt = "\n".join([f"{message['role']}: {message['content']}" for message in self.chat_history[-5:]])
        prompt += f"\nUser: {user_input}"
        response = index.query(user_input)

        message = {"role": "assistant", "content": response.response}
        self.chat_history.append({"role": "user", "content": user_input})
        self.chat_history.append(message)
        return message
    
    def load_chat_history(self, filename):
        try:
            with open(filename, 'r') as f:
                self.chat_history = json.load(f)
        except FileNotFoundError:
            pass

    def save_chat_history(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.chat_history, f)

documents = SimpleDirectoryReader('./data').load_data()
index = GPTSimpleVectorIndex(documents)

# Swap out your index below for whatever knowledge base you want
bot = Chatbot("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", index=index)
bot.load_chat_history("chat_history.json")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Bot: Goodbye!")
        bot.save_chat_history("chat_history.json")
        break
    response = bot.generate_response(user_input)
    print(f"Bot: {response['content']}")
