# Abdullah Hasani
# ahh190004
# NLP HW 4

import pickle
from nltk import word_tokenize
from nltk import ngrams


def read_dict(file_name):
    # Read the input pickle file as raw text
    with open(file_name, 'rb') as file:
        data = pickle.load(file)

        # return the dictionary
        return data


def read_file(filepath):
    # Read the input file as raw text
    file = open(filepath, 'r')
    data = file.read()
    file.close()
    data = data.splitlines()

    # return the list of lines
    return data


def calculate_unique_tokens(english_unigram_dict, french_unigram_dict, italian_unigram_dict):
    # Calculate the number of unique tokens
    num_unique_tokens = len(english_unigram_dict) + len(french_unigram_dict) + len(italian_unigram_dict)
    return num_unique_tokens


def calculate_probabilities(text, unigram_dict, bigram_dict, num_unique_tokens):
    # Calculate the probabilities of the bigrams in the text

    # Tokenize the text
    unigrams_test = word_tokenize(text)
    bigrams_test = list(ngrams(unigrams_test, 2))

    p_laplace = 1

    # Loop through the bigrams and calculate the probability using Laplace smoothing
    for bigram in bigrams_test:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        p_laplace *= (n + 1) / (d + num_unique_tokens)

    # Return the probability
    return p_laplace


def highest_probability(english_prob, french_prob, italian_prob):
    # Return the language with the highest probability
    if french_prob > english_prob and french_prob > italian_prob:
        return 'French'
    elif italian_prob > english_prob and italian_prob > french_prob:
        return 'Italian'
    else:
        return 'English'


def compare_files():
    # Compare the output file with the correct solution file
    diff_counter = 0
    diff_lines = []

    # Loop through the lines of both files and compare them
    with open('LangId.sol') as correct_solution, open('Mysol.txt') as my_solution:
        for line1, line2 in zip(correct_solution, my_solution):
            if line1 != line2:
                diff_counter += 1
                diff_lines.append(line1.split()[0])

    # Return the number of differences and the line numbers of the differences
    return diff_counter, diff_lines


def print_results(accuracy, difference, diff_lines):
    # Print the results
    print(f"Accuracy: {round(accuracy, 2)}%")
    print(f"Number of line differences: {difference}")
    print("Line numbers of incorrectly classified lines: ")
    for diff in diff_lines:
        print(diff)


if __name__ == '__main__':
    # Unpickle english, French, and italian bigram and unigram dictionaries
    english_bigram_dict = read_dict('english_bigram_dict.pickle')
    english_unigram_dict = read_dict('english_unigram_dict.pickle')
    french_bigram_dict = read_dict('french_bigram_dict.pickle')
    french_unigram_dict = read_dict('french_unigram_dict.pickle')
    italian_bigram_dict = read_dict('italian_bigram_dict.pickle')
    italian_unigram_dict = read_dict('italian_unigram_dict.pickle')

    # Calculate the number of unique tokens
    num_unique_tokens = calculate_unique_tokens(english_unigram_dict, french_unigram_dict, italian_unigram_dict)

    # Read the test data
    test_data = read_file('LangId.test')

    # Open the output file
    with open("Mysol.txt", 'w') as file:
        # Loop through the lines of the test data
        for count, line in enumerate(test_data):

            # Calculate the probabilities of the bigrams in the line
            english_prob = calculate_probabilities(line, english_unigram_dict, english_bigram_dict, num_unique_tokens)
            french_prob = calculate_probabilities(line, french_unigram_dict, french_bigram_dict, num_unique_tokens)
            italian_prob = calculate_probabilities(line, italian_unigram_dict, italian_bigram_dict, num_unique_tokens)

            # Get the language with the highest probability
            most_likely_language = highest_probability(english_prob, french_prob, italian_prob)

            # Write the line number and the most likely language to the output file
            file.write(f"{count} {most_likely_language}\n")

    # Compare the output file with the correct solution file
    difference, diff_lines = compare_files()

    # Calculate the accuracy
    accuracy = ((count - difference) / count) * 100

    # Print the results
    print_results(accuracy, difference, diff_lines)
