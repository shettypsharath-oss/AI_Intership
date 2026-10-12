import tkinter as tk
from tkinter import messagebox
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("dataset.csv")

X_train, X_test, y_train, y_test = train_test_split(
    data["text"],
    data["label"],
    test_size=0.25,
    random_state=42,
    stratify=data["label"]
)

# Train AI model
model = make_pipeline(
    TfidfVectorizer(),
    MultinomialNB()
)

model.fit(X_train, y_train)

accuracy = accuracy_score(
    y_test, model.predict(X_test)
) * 100

# Statistics
total = 0
spam_count = 0
normal_count = 0

# Colors
BG = "#0F172A"
CARD = "#1E293B"
BLUE = "#3B82F6"
WHITE = "#F8FAFC"
GREEN = "#22C55E"
RED = "#EF4444"
MUTED = "#94A3B8"

# Main window
root = tk.Tk()
root.title("MailGuard AI - Spam Detection")
root.geometry("950x750")
root.configure(bg=BG)
root.minsize(800, 650)

# Header
header = tk.Frame(root, bg=BG)
header.pack(fill="x", padx=30, pady=20)

tk.Label(
    header,
    text="🛡 MailGuard AI",
    font=("Arial", 25, "bold"),
    bg=BG,
    fg=WHITE
).pack(side="left")

tk.Label(
    header,
    text="INTELLIGENT EMAIL SECURITY",
    font=("Arial", 10, "bold"),
    bg=BG,
    fg=GREEN
).pack(side="right", pady=12)

tk.Label(
    root,
    text="Spam Email Detection Dashboard",
    font=("Arial", 18, "bold"),
    bg=BG,
    fg=WHITE
).pack(anchor="w", padx=30)

tk.Label(
    root,
    text="Analyze messages using Machine Learning",
    font=("Arial", 11),
    bg=BG,
    fg=MUTED
).pack(anchor="w", padx=30, pady=(3, 18))

# Statistics cards
stats = tk.Frame(root, bg=BG)
stats.pack(fill="x", padx=25)

def make_card(parent, title, value, color):
    card = tk.Frame(parent, bg=CARD, padx=15, pady=16)
    card.pack(side="left", fill="both", expand=True, padx=5)

    tk.Label(
        card, text=title,
        font=("Arial", 10),
        bg=CARD, fg=MUTED
    ).pack()

    value_label = tk.Label(
        card, text=value,
        font=("Arial", 23, "bold"),
        bg=CARD, fg=color
    )
    value_label.pack(pady=8)

    return value_label

total_label = make_card(stats, "TOTAL CHECKED", "0", BLUE)
spam_label = make_card(stats, "SPAM DETECTED", "0", RED)
normal_label = make_card(stats, "NORMAL EMAILS", "0", GREEN)
accuracy_label = make_card(
    stats, "MODEL ACCURACY",
    f"{accuracy:.1f}%", "#C4B5FD"
)

# Input card
input_card = tk.Frame(root, bg=CARD, padx=22, pady=20)
input_card.pack(fill="x", padx=30, pady=22)

tk.Label(
    input_card,
    text="Enter Email Message",
    font=("Arial", 14, "bold"),
    bg=CARD,
    fg=WHITE
).pack(anchor="w", pady=(0, 12))

email_box = tk.Text(
    input_card,
    height=5,
    font=("Arial", 12),
    wrap="word",
    bg="#F1F5F9",
    fg="#0F172A",
    padx=12,
    pady=10,
    relief="flat"
)
email_box.pack(fill="x")

# Result display
result = tk.Label(
    input_card,
    text="Waiting for email analysis...",
    font=("Arial", 15, "bold"),
    bg=CARD,
    fg=MUTED
)
result.pack(pady=15)

# History
history_card = tk.Frame(root, bg=CARD, padx=20, pady=15)
history_card.pack(fill="both", expand=True, padx=30)

tk.Label(
    history_card,
    text="Recent Detection History",
    font=("Arial", 13, "bold"),
    bg=CARD,
    fg=WHITE
).pack(anchor="w", pady=(0, 10))

history = tk.Listbox(
    history_card,
    height=5,
    font=("Arial", 10),
    bg="#111827",
    fg=WHITE,
    selectbackground=BLUE,
    relief="flat"
)
history.pack(fill="both", expand=True)

# Functions
def check_email():
    global total, spam_count, normal_count

    text = email_box.get("1.0", "end").strip()

    if not text:
        messagebox.showwarning(
            "Empty Message",
            "Please enter an email message."
        )
        return

    prediction = model.predict([text])[0]

    total += 1

    if prediction == "spam":
        spam_count += 1
        result.config(
            text="⚠ SPAM EMAIL DETECTED",
            fg=RED
        )
        status = "SPAM"
    else:
        normal_count += 1
        result.config(
            text="✓ EMAIL IS NOT SPAM",
            fg=GREEN
        )
        status = "NORMAL"

    total_label.config(text=str(total))
    spam_label.config(text=str(spam_count))
    normal_label.config(text=str(normal_count))

    history.insert(
        0, f"{total}. {status} - {text[:55]}"
    )

def clear_email():
    email_box.delete("1.0", "end")
    result.config(
        text="Waiting for email analysis...",
        fg=MUTED
    )

def about_project():
    messagebox.showinfo(
        "About Project",
        "MailGuard AI\n\n"
        "Spam Email Classification System\n\n"
        "Algorithm: Multinomial Naive Bayes\n"
        "Text Processing: TF-IDF\n"
        "Language: Python\n"
        "Libraries: Pandas, Scikit-learn, Tkinter"
    )

# Buttons
buttons = tk.Frame(root, bg=BG)
buttons.pack(pady=18)

tk.Button(
    buttons,
    text="CHECK EMAIL",
    command=check_email,
    bg=BLUE,
    fg=WHITE,
    font=("Arial", 11, "bold"),
    width=17,
    pady=11,
    relief="flat",
    cursor="hand2"
).pack(side="left", padx=7)

tk.Button(
    buttons,
    text="CLEAR",
    command=clear_email,
    bg="#475569",
    fg=WHITE,
    font=("Arial", 11, "bold"),
    width=12,
    pady=11,
    relief="flat",
    cursor="hand2"
).pack(side="left", padx=7)

tk.Button(
    buttons,
    text="ABOUT",
    command=about_project,
    bg="#7C3AED",
    fg=WHITE,
    font=("Arial", 11, "bold"),
    width=12,
    pady=11,
    relief="flat",
    cursor="hand2"
).pack(side="left", padx=7)

tk.Button(
    buttons,
    text="EXIT",
    command=root.destroy,
    bg="#991B1B",
    fg=WHITE,
    font=("Arial", 11, "bold"),
    width=10,
    pady=11,
    relief="flat",
    cursor="hand2"
).pack(side="left", padx=7)

# Footer
tk.Label(
    root,
    text="AI Internship Project | Python + Machine Learning",
    font=("Arial", 9),
    bg=BG,
    fg=MUTED
).pack(pady=(0, 12))

root.mainloop()