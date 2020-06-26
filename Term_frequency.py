import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def remove_puctuation(filename):
    with open(filename.text, "r") as file:
        text = file.read()

    tokenizer = nltk.RegexpTokenizer(r"\w+")  # Removes all punctuation marks in the text
    new_words = tokenizer.tokenize(text)      # Returns a text as a list of words with punctuations removed.
    #print (new_words)
    return new_words

def lower_case(filename):
    with open(filename.text, "r") as file:
        text = file.read()

    words = nltk.word_tokenize(text)  # Breaks text paragraph into words
    words = [word.lower() for word in words if word.isalpha()]  # Changes all the words into lower case
    #print(words)

    return words

def stop_words(filename):
    with open(filename.text, "r") as file:
        text = file.read()

    stop_words = set(stopwords.words('english')) # Creating a List of stopwords

    word_tokens = word_tokenize(text) # Split sentences in the text into words

    filtered_words = [w for w in word_tokens if not w in stop_words] # Filter out a list of tokens from the text.
    filtered_words = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_words.append(w)    # Add all words after stopwords have been removed
    print ("Filtered_words:",filtered_words )
    return filtered_words

