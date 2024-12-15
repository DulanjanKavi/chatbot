from flask import Flask, jsonify, request
from flask_cors import CORS
import numpy as np
import nltk
import string
import random
import warnings
warnings.filterwarnings("ignore")
import os
from spellchecker import SpellChecker
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('brown')

# Load and preprocess the document
with open('backend/catbot.txt', 'r', errors='ignore') as f:
    raw_doc = f.read().lower()

sentence_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)
lemmer = nltk.stem.WordNetLemmatizer()
spell = SpellChecker()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))

# Define greeting functions
greet_inputs = ("hello", "hi", "whassup", "how are you?")
greet_responses = ("Hi", "Hey", "Hello there!", "Greetings!")

def greet(sentence):
    for word in sentence.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)
    return None

# Define gratitude functions
thank_inputs = ("thank you", "thanks", "thank you so much", "thanks a lot")
thank_responses = ("You're welcome!", "No problem!", "Happy to help!", "Anytime!")

def express_gratitude(sentence):
    for word in sentence.split():
        if word.lower() in thank_inputs:
            return random.choice(thank_responses)
    return None

# Define farewell functions
farewell_inputs = ("bye", "goodbye", "see you", "talk to you later")
farewell_responses = ("Goodbye!", "See you soon!", "Take care!", "Talk to you later!")

def say_farewell(sentence):
    for word in sentence.split():
        if word.lower() in farewell_inputs:
            return random.choice(farewell_responses)
    return None

# Define sorry messages
sorry_messages = [
    "I am sorry, that item is not available right now.",
    "Apologies, we don't have that item in stock at the moment.",
    "Sorry, we currently don't have that item.",
    "Unfortunately, that item is not available at the moment.",
    "I'm afraid we don't have that item right now."
]

# Spell check function
def correct_spelling(text):
    corrected_text = []
    for word in text.split():
        corrected_word = spell.correction(word)
        if corrected_word is None:
            corrected_word = word  # Use the original word if no correction is found
        corrected_text.append(corrected_word)
    return ' '.join(corrected_text)

# Load Brown Corpus
from nltk.corpus import brown
brown_words = brown.words()
brown_text = ' '.join(brown_words).lower()

# Extract keywords using TF-IDF
tfidf_vec = TfidfVectorizer(tokenizer=LemNormalize, stop_words="english", max_features=100)
tfidf_matrix = tfidf_vec.fit_transform(sentence_tokens)
keywords = tfidf_vec.get_feature_names_out()

# Function to find relevant sentences
def find_relevant_sentences(user_keywords):
    relevant_sentences = []
    for sentence in sentence_tokens:
        lemmatized_sentence = LemNormalize(sentence)
        if any(keyword in lemmatized_sentence for keyword in user_keywords):
            relevant_sentences.append(sentence)
    return relevant_sentences

# Response generation
def response(user_response):
    user_response = user_response.lower()
    robo_response = ""
    lemmatized_user_response = LemNormalize(user_response)

    # Find relevant sentences based on lemmatized user response
    relevant_sentences = find_relevant_sentences(lemmatized_user_response)

    # Sort relevant sentences based on the number of query keywords they contain
    sorted_sentences = sorted(relevant_sentences, key=lambda s: sum(kw in LemNormalize(s) for kw in lemmatized_user_response), reverse=True)
    
    # Check if any relevant sentences were found
    if sorted_sentences:
        robo_response = " ".join(sorted_sentences)
    else:
        robo_response = random.choice(sorry_messages)
    
    return robo_response.strip()

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    corrected_message = correct_spelling(user_message)
    
    # Check for greetings
    bot_response = greet(corrected_message)
    if bot_response is None:
        # Check for expressions of gratitude
        bot_response = express_gratitude(corrected_message)
        if bot_response is None:
            # Check for farewells
            bot_response = say_farewell(corrected_message)
            if bot_response is None:
                # Generate response based on user input
                bot_response = response(corrected_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
