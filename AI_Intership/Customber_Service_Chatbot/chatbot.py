import tkinter as tk
from tkinter import scrolledtext


def get_response(message):
    message = message.lower().strip()

    if "hello" in message or "hi" in message:
        return "Hello! Welcome to Customer Support. How can I help you?"

    elif "order" in message:
        return "Please provide your order ID so we can check your order status."

    elif "delivery" in message or "shipping" in message:
        return "Standard delivery usually takes 3-5 business days."

    elif "refund" in message or "return" in message:
        return "You can request a return or refund within 7 days of receiving your order."

    elif "payment" in message:
        return "We accept UPI, debit cards, credit cards and online payments."

    elif "price" in message:
        return "Please tell me the product name to check its price."

    elif "support" in message or "contact" in message:
        return "You can contact our support team at support@example.com."

    elif "bye" in message:
        return "Thank you for contacting us. Have a great day!"

    else:
        return "Sorry, I didn't understand. Please ask about orders, delivery, returns, refunds, payments or support."


def send_message():
    message = entry.get().strip()

    if not message:
        return

    chat.insert(tk.END, "You: " + message + "\n", "user")

    response = get_response(message)

    chat.insert(tk.END, "Bot: " + response + "\n\n", "bot")

    entry.delete(0, tk.END)
    chat.see(tk.END)


def clear_chat():
    chat.delete("1.0", tk.END)
    chat.insert(
        tk.END,
        "Bot: Hello! Welcome to Customer Support. How can I help you?\n\n",
        "bot"
    )


root = tk.Tk()
root.title("Customer Service AI - Support Assistant")
root.geometry("850x700")
root.minsize(750, 600)
root.configure(bg="#0F172A")


# Header
header = tk.Frame(root, bg="#0F172A")
header.pack(fill="x", padx=25, pady=(20, 10))

title = tk.Label(
    header,
    text="Customer Service AI",
    font=("Arial", 26, "bold"),
    bg="#0F172A",
    fg="white"
)
title.pack(anchor="w")

subtitle = tk.Label(
    header,
    text="AI-powered customer support assistant",
    font=("Arial", 11),
    bg="#0F172A",
    fg="#94A3B8"
)
subtitle.pack(anchor="w", pady=(3, 0))


# Status
status = tk.Label(
    header,
    text="● Online",
    font=("Arial", 11, "bold"),
    bg="#0F172A",
    fg="#22C55E"
)
status.pack(anchor="w", pady=(8, 0))


# Chat card
chat_frame = tk.Frame(
    root,
    bg="#1E293B"
)
chat_frame.pack(
    fill="both",
    expand=True,
    padx=25,
    pady=10
)


chat = scrolledtext.ScrolledText(
    chat_frame,
    font=("Arial", 12),
    bg="#1E293B",
    fg="white",
    insertbackground="white",
    wrap=tk.WORD,
    relief="flat"
)
chat.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=15
)


chat.tag_config("user", foreground="#60A5FA")
chat.tag_config("bot", foreground="#4ADE80")


chat.insert(
    tk.END,
    "Bot: Hello! Welcome to Customer Support. How can I help you?\n\n",
    "bot"
)


# Input section
input_frame = tk.Frame(
    root,
    bg="#0F172A"
)
input_frame.pack(
    fill="x",
    padx=25,
    pady=(5, 15)
)


entry = tk.Entry(
    input_frame,
    font=("Arial", 13),
    bg="white",
    fg="black",
    relief="flat"
)
entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=11,
    padx=(0, 10)
)


send_button = tk.Button(
    input_frame,
    text="SEND",
    command=send_message,
    font=("Arial", 11, "bold"),
    bg="#3B82F6",
    fg="white",
    activebackground="#2563EB",
    activeforeground="white",
    relief="flat",
    width=10,
    cursor="hand2"
)
send_button.pack(
    side="left",
    ipady=6,
    padx=(0, 8)
)


clear_button = tk.Button(
    input_frame,
    text="CLEAR",
    command=clear_chat,
    font=("Arial", 11, "bold"),
    bg="#475569",
    fg="white",
    relief="flat",
    width=10,
    cursor="hand2"
)
clear_button.pack(
    side="left",
    ipady=6
)


# Enter key support
entry.bind(
    "<Return>",
    lambda event: send_message()
)


root.mainloop()