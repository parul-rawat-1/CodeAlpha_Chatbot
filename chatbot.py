import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

def chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message or "hey" in message:
        return random.choice([
            "Hello there!",
            "Hi! How can I help you?",
            "Hey! Nice to see you."
        ])

    elif "how are you" in message:
        return random.choice([
            "I'm doing great!",
            "I'm fine, thanks for asking!",
            "All good here!"
        ])

    elif "time" in message:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"

    elif "date" in message:
        today = datetime.date.today()
        return f"Today's date is {today}"

    elif "your name" in message:
        return "I am your Python chatbot."

    elif "thank" in message:
        return "You're welcome!"

    elif "bye" in message:
        return "Goodbye! Have a great day."

    else:
        return random.choice([
            "Interesting!",
            "Tell me more.",
            "I see.",
            "That's cool!"
        ])


def send_message(event=None):
    user_message = entry_box.get().strip()

    if user_message == "":
        return

    chat_area.config(state=tk.NORMAL)

    # user message
    chat_area.insert(tk.END, "You: " + user_message + "\n", "user")

    # bot reply
    bot_reply = chatbot_response(user_message)
    chat_area.insert(tk.END, "Bot: " + bot_reply + "\n\n", "bot")

    chat_area.config(state=tk.DISABLED)
    chat_area.yview(tk.END)

    entry_box.delete(0, tk.END)


def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete(1.0, tk.END)
    chat_area.config(state=tk.DISABLED)


window = tk.Tk()
window.title("Smart Chatbot")
window.geometry("520x600")
window.configure(bg="#1e1e2f")


title = tk.Label(
    window,
    text="Python Chatbot",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=10)


chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    width=60,
    height=25,
    font=("Arial", 11),
    bg="#2b2b3c",
    fg="white",
    bd=0
)

chat_area.pack(padx=10, pady=10)
chat_area.config(state=tk.DISABLED)


chat_area.tag_config("user", foreground="#00ffcc")
chat_area.tag_config("bot", foreground="#ffcc66")


input_frame = tk.Frame(window, bg="#1e1e2f")
input_frame.pack(pady=10)


entry_box = tk.Entry(
    input_frame,
    width=35,
    font=("Arial", 12),
    bg="#3a3a4f",
    fg="white",
    insertbackground="white"
)
entry_box.pack(side=tk.LEFT, padx=5)
entry_box.bind("<Return>", send_message)


send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#4CAF50",
    fg="white",
    width=10
)
send_button.pack(side=tk.LEFT, padx=5)


clear_button = tk.Button(
    window,
    text="Clear Chat",
    command=clear_chat,
    bg="#ff4d4d",
    fg="white",
    width=15
)
clear_button.pack(pady=5)


chat_area.config(state=tk.NORMAL)
chat_area.insert(tk.END, "Bot: Hello! I am your chatbot. Ask me something.\n\n", "bot")
chat_area.config(state=tk.DISABLED)


window.mainloop()