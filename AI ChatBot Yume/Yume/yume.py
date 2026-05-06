import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')


# Purpose: This function takes a sentence as input and prepares it for further processing. It tokenizes the sentence
# into individual words, lemmatizes each word to reduce it to its base form, and returns a list of lemmatized words.
# Input: A string representing a sentence.
# Output: A list of lemmatized words.
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words


# Purpose: Converts a sentence into a "bag of words" representation. It takes a sentence, tokenizes it, and then creates
# a binary vector (bag) where each element represents the presence (1) or absence (0) of a word in the sentence.
# Input: A string representing a sentence.
# Output: A binary vector (NumPy array) representing the presence of words in the sentence
def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


# Purpose: Predicts the intent of a given sentence using the trained neural network model. It converts the sentence into
# a bag of words representation and then feeds this representation into the model to get a prediction.
# The function returns a list of intents sorted by their probability, with the highest probability intent at the top.
# Input: A string representing a sentence.
# Output: A list of dictionaries, each containing an 'intent' and its 'probability'.

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})
    return return_list


# Purpose: Generates a response based on the predicted intent of the users message.
# It first calls predict_class to get the predicted intent. Then, it searches through the list of intents
# defined in intents.json to find a matching intent tag. If a match is found, it randomly selects a response from
# the list of responses associated with that intent. If no match is found,
# it returns a default response indicating that the chatbot does not understand the message.)
# Input: A string representing the user's message.
# Output: A string representing the chatbot's response.

def get_response(message):
    intents_list = predict_class(message)
    if intents_list is not None and len(intents_list) > 0:
        tag = intents_list[0]['intent']
        list_of_intents = intents['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                return random.choice(i['responses'])
    return "Sorry, I don't understand that."


print("Yume has been summoned!")

# while True:
#    message = input("")
#    ints = predict_class(message)
#    res = get_response(ints, intents)
#    print(res)

# The script also loads necessary data and models at the beginning, including a list of words (words),
# a list of classes (classes), and the trained neural network model (model).
# The lemmatizer is used to reduce words to their base form, which helps in matching
# user input to the intents defined in intents.json.
# The commented-out while loop at the end suggests that the script was intended to be run in an interactive mode,
# where it would continuously accept user input, predict the intent, and generate a response.
