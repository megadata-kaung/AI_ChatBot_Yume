# Yume Anime Recommendation Chatbot

Yume is an AI-powered anime recommendation chatbot developed using Python, Natural Language Processing (NLP), and machine learning techniques. The chatbot interacts with users and provides anime recommendations based on user moods, emotions, and preferences.

For example:
- If the user says "sad", Yume recommends emotional anime.
- If the user says "action", Yume recommends action-based anime.
- If the user says "romance", Yume suggests romance anime titles.

The project combines intent recognition, neural network classification, and a graphical user interface to create an interactive anime recommendation experience.

---

# Features

- Mood-based anime recommendations
- NLP intent recognition
- Interactive GUI chatbot interface
- Neural network based response system
- Custom anime intent dataset
- Anime-themed user interface
- Fast response generation

---

# Technologies Used

- Python
- TensorFlow / Keras
- NLTK
- NumPy
- PyQt5
- Pickle

---

# Project Structure

```text
Yume-AI-Chatbot/
│
├── chatbotmodel.h5
├── classes.pkl
├── words.pkl
├── intents.json
│
├── training.py
├── yume.py
├── yume_interface.py
├── yume_interface_0.2.py
│
├── assets/
│   ├── solo_leveling_1920x1080.png
│   └── other images
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# How It Works

The chatbot follows these steps:

1. User enters a message
2. NLP preprocessing is applied
3. The message is tokenized and lemmatized
4. A bag-of-words representation is created
5. The trained neural network predicts the intent
6. Yume generates a suitable anime recommendation response

---

# Example Commands

## User Input

```text
sad
```

## Chatbot Response

```text
Your Lie in April
Clannad
I Want to Eat Your Pancreas
```

---

## User Input

```text
action
```

## Chatbot Response

```text
Attack on Titan
Jujutsu Kaisen
Demon Slayer
```

---

# Installation

## Clone Repository

```bash
git clone <your-repository-link>
```

---

# Install Required Libraries

```bash
pip install tensorflow nltk numpy PyQt5
```

---

# Download NLTK Resources

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
```

---

# Running the Project

## Train the Model

```bash
python training.py
```

This generates:
- `chatbotmodel.h5`
- `words.pkl`
- `classes.pkl`

---

## Launch the Chatbot GUI

```bash
python yume_interface_0.2.py
```

---

# GUI Preview

(Add screenshots here)

---

# Current Limitations

- Limited anime recommendation dataset
- Responses depend on trained intents
- GUI compatibility may vary depending on environment setup
- Requires proper dependency installation

---

# Future Improvements

- Voice interaction support
- Larger anime recommendation database
- Better recommendation personalization
- Integration with anime APIs
- Improved GUI design
- Emotion detection using deep learning
- Real-time anime trending recommendations

---

# Contributors

- Htet Kaung Myat Oo

---

# Academic Purpose

This project was developed as part of an AI and chatbot development learning project using NLP and machine learning concepts.

---

# License

This project is for educational and learning purposes.
