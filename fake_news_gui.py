import tkinter as tk
from tkinter import messagebox
import joblib

# Load the model and vectorizer
model = joblib.load("fake_news_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Predict function
def predict_news():
    text = input_field.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter some news content.")
        return
    transformed = vectorizer.transform([text])
    prediction = model.predict(transformed)[0]
    result = "🟢 Real News" if prediction == 0 else "🔴 Fake News"
    result_label.config(text=f"Prediction: {result}")

# GUI setup
window = tk.Tk()
window.title("Fake News Detection")
window.geometry("500x300")

title_label = tk.Label(window, text="Enter News Content:", font=("Arial", 14))
title_label.pack(pady=10)

input_field = tk.Text(window, height=8, width=60)
input_field.pack()

predict_button = tk.Button(window, text="Predict", command=predict_news, font=("Arial", 12))
predict_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

window.mainloop()
