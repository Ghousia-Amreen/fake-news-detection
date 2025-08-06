# 📰 Fake News Detection using Machine Learning

This project detects whether a news article is **Fake** or **Real** using machine learning techniques. It features a trained model, text vectorization with TF-IDF, and a simple GUI built using **Tkinter** for user interaction.

---

## ✅ Features

- Classifies news as **Fake** or **Real**
- Uses **TF-IDF** for text vectorization
- Built with **Logistic Regression** for accuracy
- Clean and simple **GUI** for user input

---

## 📂 Project Structure

```
fake-news-detection/
│
├── fake_news_gui.py           # GUI code for prediction
├── fake_news_model.pkl        # Trained ML model
├── tfidf_vectorizer.pkl       # Saved TF-IDF vectorizer
├── WELFake_Dataset.csv        # Dataset used (optional)
├── requirements.txt           # All required packages
└── README.md                  # You're reading it now!
screenshots/
    ├── gui_interface.png      #GUI interface
    └── output_prediction.png  #prediction output
```

---

## 🧠 Model Details

- **Algorithm**: Logistic Regression
- **Text Preprocessing**:
  - Lowercasing
  - Removing punctuation and stopwords
  - Lemmatization
- **Vectorization**: TF-IDF

---

## 🚀 How to Run the Project

### 1. Install the dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the GUI

```bash
python fake_news_gui.py
```

### 3. Enter a news sentence and click **Predict**  
You'll see whether the news is **Fake** or **Real**.

---

## 📊 Dataset Info

- **Name**: WELFake Dataset
- **Size**: ~72,000 news articles
- **Labels**: `1` = Fake, `0` = Real

---

## 📸 Screenshots

> ## 🔍 GUI Preview

![GUI Interface](screenshots/gui_interface.png)

## 🧪 Prediction Output

![Prediction Output](screenshots/output_prediction.png)


---

## 🧪 Sample Result

```bash
Enter news: "Breaking: Government increases health budget by 40%"

Prediction: Real News ✅
```

---

## 🙋‍♀️ Author

**Ghousia Amreen**  
> Machine Learning Enthusiast 
>🔗 [Ghousia Amreen](https://github.com/<Ghousia-Amreen>)


---

## ⭐ GitHub

If you like this project, give it a ⭐ on GitHub and share!
