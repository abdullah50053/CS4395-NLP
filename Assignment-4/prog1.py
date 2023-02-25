# Abdullah Hasani
# ahh190004
# NLP HW 4

import pickle
from nltk import word_tokenize
from nltk import ngrams


def process(file_name):
    raw_text = read_file(file_name)
    tokens = tokenize(raw_text)
    bigrams = create_bigrams(tokens)
    unigrams = tokens
    bigram_dict = create_bigram_dict(bigrams)
    unigram_dict = create_unigram_dict(unigrams)
    return bigram_dict, unigram_dict


def read_file(filepath):
    # Read the input file as raw text
    file = open(filepath, 'r')
    data = file.read()
    file.close()
    data = data.replace('\n', '')
    return data


def tokenize(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    return tokens


def create_bigrams(tokens):
    # Create a list of bigrams
    bigrams = list(ngrams(tokens, 2))
    return bigrams


def create_bigram_dict(bigrams):
    # Create a dictionary of bigrams
    bigram_dict = {b: bigrams.count(b) for b in set(bigrams)}
    return bigram_dict


def create_unigram_dict(unigrams):
    # Create a dictionary of unigrams
    unigram_dict = {t: unigrams.count(t) for t in set(unigrams)}
    return unigram_dict


def pickle_file(file_name, data):
    # Pickle the file
    with open(file_name, 'wb') as file:
        pickle.dump(data, file)


if __name__ == '__main__':
    english_bigram_dict, english_unigram_dict = process('LangId.train.English')
    pickle_file('english_bigram_dict.pickle', english_bigram_dict)
    pickle_file('english_unigram_dict.pickle', english_unigram_dict)

    french_bigram_dict, french_unigram_dict = process('LangId.train.French')
    pickle_file('french_bigram_dict.pickle', french_bigram_dict)
    pickle_file('french_unigram_dict.pickle', french_unigram_dict)

    italian_bigram_dict, italian_unigram_dict = process('LangId.train.Italian')
    pickle_file('italian_bigram_dict.pickle', italian_bigram_dict)
    pickle_file('italian_unigram_dict.pickle', italian_unigram_dict)







