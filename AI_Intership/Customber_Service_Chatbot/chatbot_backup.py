import tkinter as tk


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

    if message:
        chat.insert(tk.END, "You: " + message + "\n")

        response = get_response(message)

        chat.insert(tk.END, "Bot: " + response + "\n\n")

        entry.delete(0, tk.END)


root = tk.Tk()
root.title("Customer Service AI Chatbot")
root.geometry("650x550")
root.configure(bg="#0F172A")

title = tk.Label(
    root,
    text="Customer Service AI Chatbot",
    font=("Arial", 22, "bold"),
    bg="#0F172A",
    fg="white"
)
title.pack(pady=20)
