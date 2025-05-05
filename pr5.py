import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections

# Chatbot pattern-response pairs
pairs = [
    [r"hi|hello|hey", ["Hello! How can I assist you?", "Hi there! How can I help?"]],
    [r"how are you?", ["I'm just a bot, but I'm doing well. How about you?"]],
    [r"(.*) your name?", ["I'm a chatbot here to assist you."]],
    [r"bye|goodbye", ["Goodbye! Have a nice day!", "See you later!"]],
    [r"(.*)", ["Sorry, I didn't get that. Can you rephrase?"]]
]

chatbot = Chat(pairs, reflections)

# Function to handle message sending
def send_message():
    user_msg = user_entry.get()
    if user_msg.strip():
        chat_history.insert(tk.END, f"You: {user_msg}\n")
        response = chatbot.respond(user_msg)
        chat_history.insert(tk.END, f"Bot: {response}\n\n")
        user_entry.delete(0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Simple Chatbot")

chat_history = scrolledtext.ScrolledText(root, width=50, height=15, wrap=tk.WORD)
chat_history.pack(padx=10, pady=10)

user_entry = tk.Entry(root, width=40)
user_entry.pack(padx=10, pady=5)

tk.Button(root, text="Send", command=send_message).pack(pady=5)

root.mainloop()
