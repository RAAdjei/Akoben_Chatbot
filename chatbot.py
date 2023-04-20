import nltk
from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

# Get punkt package
nltk.download('punkt', quiet=True)

# Get the article
article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()
corpus = article.text

# print article
#print(corpus)

# Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) # list of sentences

# Print the list of sentences
# print(sentence_list)

# Function for random greeting responses
def greeting_response(text):
    text = text.lower()

    #Bots greetings response
    bot_greetings = ['howdy', 'hi', 'hey', 'hola', 'hey there!']

    #User greeting
    user_greeting = ['hi', 'hey', 'hello', 'hola', 'greetings', 'wassup']

    for word in text.split():
        if word in user_greeting:
            return random.choice(bot_greetings)

def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    #sort the indexes of the list
    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index

def bot_response(user_input):
    global bot_response
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_responses = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' '+sentence_list[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break

        if response_flag == 0:
            bot_response = bot_response + ' ' + "I apologize, I don't understand."

        sentence_list.remove(user_input)

        return bot_response


# start chat bot
print("Doc Bot: I am Doctor Bot or Doc Bot for short. I will answer your queries about Chronic kidney disease. If you want to exit, type bye.")

exit_list = ['exit', 'see you later', 'bye', 'quit', 'break']

while(True):
    user_input = input()
    if user_input in exit_list:
        print('Doc Bot: Chat with you later!')
        break
    else:
        if greeting_response(user_input) != None:
            print('Doc Bot: ' + greeting_response(user_input))




