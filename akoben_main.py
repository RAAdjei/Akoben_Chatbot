import nltk
import numpy as np
from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

from akoben_bot import Bot

warnings.filterwarnings('ignore')

f = open('act29', 'r', errors='ignore')
raw_text = f.read()  # Read the text
raw_text = raw_text.lower()  # Converts text to lower case
#nltk.download('punkt')
# nltk.download('wordnet')


sent_tokens = nltk.sent_tokenize(raw_text)  # Converts doc to list of sentences
word_tokens = nltk.word_tokenize(raw_text)  # Converts doc to list of words

# Preprocessing, Stemming
lemmer = nltk.stem.WordNetLemmatizer()


def lemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def lemNormalize(text):
    return lemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# User greetings
USER_GREETINGS = ('hi', 'hello', 'wassup', 'whatsup', 'wossop',
                  'good morning', 'good afternoon', 'good evening')

# bot greeeting
BOT_GREETING = ['Hi', 'Hello there!', 'Hi there!', 'Nice to meet you']


def greeting(user_input):
    #user_input = user_input.lower()

    for word in user_input.split():
        if word.lower() in USER_GREETINGS:
            return random.choice(BOT_GREETING)


# Getting bot responses

def response(user_response):
    #global response
    bot_response = ''
    TfidfVec = TfidfVectorizer(tokenizer=lemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    cosine = cosine_similarity(tfidf[-1], tfidf)
    ids = cosine.argsort()[0][-2]
    flat = cosine.flatten()
    flat.sort()
    req_tfidf = flat[-2]

    if req_tfidf == 0:  # Exceptions in case the chatbot doesn't understand the user input
        bot_response = bot_response + "I am sorry I don't understand you"
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[ids]
        return bot_response


# Conversations and start and end commands
flag = True

# print("I am Akoben, your legal assistant, how may I assist you?, "
#      "if you want to end this conversation type 'bye' Thanks!")

if __name__ == "__main__":
    while flag == True:
        user_input = input()
        user_input = user_input.lower()

        if user_input != 'bye':
            if user_input == 'thanks' or user_input == 'thank you':
                flag = False
                print("Akoben: You are welcome")
            else:
                if greeting(user_input) is not None:
                    print("BOT: " + greeting(user_input))
                else:
                    sent_tokens.append(user_input)
                    word_tokens = word_tokens + nltk.word_tokenize(user_input)
                    last_words = list(set(word_tokens))
                    print("Bot: ", end="")
                    print(response(user_input))
                    sent_tokens.remove(user_input)

        else:
            flag = False
            print("Bot: Goodbye!")


# while flag == True:
#     user_input = input()
#     user_input = user_input.lower()
#
#     if user_input != 'bye':
#         if user_input == 'thanks' or user_input == 'thank you':
#             flag = False
#             print("Akoben: You are welcome")
#         else:
#             if greeting(user_input) is not None:
#                 print("BOT: " + greeting(user_input))
#             else:
#                 sent_tokens.append(user_input)
#                 word_tokens = word_tokens + nltk.word_tokenize(user_input)
#                 last_words = list(set(word_tokens))
#                 print("Bot: ", end="")
#                 print(response(user_input))
#                 sent_tokens.remove(user_input)
#
#     else:
#         flag = False
#         print("Bot: Goodbye!")

# Start chatbot
# bot = Bot()
#
# print("I am Akoben, your legal assistant, how may I assist you?")
# exit_list = ['exit', 'see you later', 'bye', 'quit', 'break']
#
# while True:
#     user_input = input()
#     if user_input in exit_list:
#         print("Akoben: Talk to you later, Bye!")
#         break
#     else:
#         if bot.greeting_response(user_input)!= None:
#             print("Akoben:" + bot.greeting_response(user_input))
