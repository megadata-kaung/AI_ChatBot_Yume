import random
import json
import pickle
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer

# Purpose: Imports the necessary Python libraries for the script.
#     These include random for random number generation,
#     json for parsing JSON files,
#     pickle for serializing and deserializing Python objects,
#     numpy for numerical operations,
#     tensorflow for building and training the neural network, and
#     nltk for natural language processing tasks.


# Purpose: Initializes the WordNetLemmatizer from NLTK, which is used to reduce words to their base form.

lemmatizer = WordNetLemmatizer()

# Purpose: Loads the intents and patterns from intents.json, tokenizes the patterns into words, lemmatizes the words,
# and
# creates a bag of words representation for each pattern.
# It also creates a list of unique words and classes (intents).

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignoreLetters = ['?', '!', '.', ',', ':']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList)
        documents.append((wordList, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignoreLetters]
words = sorted(set(words))

classes = sorted(set(classes))

# Purpose: Saves the list of unique words and classes to words.pkl and classes.pkl files for later use.

pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))

# Purpose: Converts the intents and patterns into a format suitable for training a neural network.
# It creates a bag of words representation for each pattern and a
# one-hot encoded vector for the corresponding intent.

training = []
outputEmpty = [0] * len(classes)

for document in documents:
    bag = []
    wordPatterns = document[0]
    wordPatterns = [lemmatizer.lemmatize(word.lower()) for word in wordPatterns]
    for word in words:
        bag.append(1) if word in wordPatterns else bag.append(0)

    outputRow = list(outputEmpty)
    outputRow[classes.index(document[1])] = 1
    training.append(bag + outputRow)

random.shuffle(training)
training = np.array(training)

trainX = training[:, :len(words)]
trainY = training[:, len(words):]

# Purpose: Defines a neural network model with three layers and trains it on the prepared training data.
# The model is a simple feedforward neural network with dropout layers to prevent overfitting.

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(trainX[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(trainY[0]), activation='softmax'))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(trainX, trainY, epochs=200, batch_size=5, verbose=1)
model.save('chatbotmodel.h5', hist)
print('Done')
