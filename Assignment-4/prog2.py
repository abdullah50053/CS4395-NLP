# Abdullah Hasani
# ahh190004
# NLP HW 4

import pickle


def read_dict(file_name):
    with open(file_name, 'rb') as file:
        data = pickle.load(file)
        return data


def read_file(filepath):
    # Read the input file as raw text
    file = open(filepath, 'r')
    data = file.read()
    file.close()
    return data


def calculate_num_tokens(english_unigram_dict, french_unigram_dict, italian_unigram_dict):
    num_tokens = 0
    for key in english_unigram_dict:
        num_tokens += english_unigram_dict[key]
    for key in french_unigram_dict:
        num_tokens += french_unigram_dict[key]
    for key in italian_unigram_dict:
        num_tokens += italian_unigram_dict[key]
    return num_tokens


def calculate_unique_tokens(english_unigram_dict, french_unigram_dict, italian_unigram_dict):
    num_unique_tokens = len(english_unigram_dict) + len(french_unigram_dict) + len(italian_unigram_dict)
    return num_unique_tokens


if __name__ == '__main__':
    english_bigram_dict = read_dict('english_bigram_dict.pickle')
    english_unigram_dict = read_dict('english_unigram_dict.pickle')
    french_bigram_dict = read_dict('french_bigram_dict.pickle')
    french_unigram_dict = read_dict('french_unigram_dict.pickle')
    italian_bigram_dict = read_dict('italian_bigram_dict.pickle')
    italian_unigram_dict = read_dict('italian_unigram_dict.pickle')

    num_tokens = calculate_num_tokens(english_unigram_dict, french_unigram_dict, italian_unigram_dict)
    num_unique_tokens = calculate_unique_tokens(english_unigram_dict, french_unigram_dict, italian_unigram_dict)

    test_data = read_file('LangId.test')

    print('Number of tokens: ', num_tokens)
    print('Number of unique tokens: ', num_unique_tokens)
    print('Test data: ', test_data)
