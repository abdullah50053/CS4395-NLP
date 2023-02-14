# Abdullah Hasani
# ahh190004
# NLP HW 2

# assumes sysarg is /anat19.txt
import os
import random
import sys
import nltk
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


def read_file(filepath):
    # Read the input file as raw text
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read()
    return text_in


def calculate_lexical_diversity(text):
    nltk.download('popular')

    # Calculate the lexical diversity of the tokenized text
    tokens = word_tokenize(text)
    token_set = set(tokens)
    lexical_diversity = len(token_set)/len(tokens)

    # output lexical diversity
    print("Lexical Deversity: %.2f" % lexical_diversity)


def preprocess(text):
    # reduce the tokens to only those that are alpha
    clean_text = re.sub(r'[.?!,:;()\-\n\d]', ' ', text.lower())

    # tokenize the lower-case raw text
    tokens = word_tokenize(clean_text)

    # reduce to words not in the NLTK stopword list and have length > 5
    stop_words = stopwords.words('english')
    new_tokens = [t for t in tokens if t not in stop_words and len(t) > 5]

    # lemmatize the tokens
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in new_tokens]

    # use set() to make a list of unique lemmas
    lemmas = list(set(lemmas))

    # do pos tagging on the unique lemmas
    tags = nltk.pos_tag(lemmas)
    ftwenty = tags[:20]

    #  print the first 20 tagged
    print("First 20 tagged: ")
    print(ftwenty)

    # create a list of only those lemmas that are nouns
    noun_list = ['NN', 'NNS', 'NNP', 'NNPS']
    nouns = [t for t in tags if t[1] in noun_list]

    # print the number of tokens
    print('Number of tokens: ' + str(len(new_tokens)))

    # print the number of nouns
    print('Number of nouns:' + str(len(nouns)))

    # return tokens and nouns
    return new_tokens, nouns


def make_dict(tokens, nouns):
    # Make a dictionary of {noun:count of noun in tokens} items from the nouns and tokens lists
    new_dict = {}
    new_nouns = [i[0] for i in nouns if i[0] in tokens]
    for i in new_nouns:
        new_dict[i] = tokens.count(i)

    # Sort the dict by count
    sort_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))

    # Save top 50 words to a list
    top_50 = []
    for i in reversed(sort_dict):
        top_50.append(i)
    top_50 = top_50[:50]

    # Print the 50 most common words and their counts
    print("Top 50 most common words:")
    for i in top_50:
        print(i + ':' + str(new_dict[i]))
    return top_50


def guessing_game(t50):
    # Give the user 5 points to start with
    user_pts = 5
    print(f"The game has begun! You have {user_pts} points.")

    # Randomly choose one of the 50 words in the top 50 list
    word = random.choice(t50)
    guesses = []

    while user_pts > 0:
        wrong = 0
        for i in word:
            if i in guesses:
                # fill in all matching letter _ with the letter
                print(i, end=' ')
            else:
                # output to console an “underscore space” for each letter in the word
                print('_', end=' ')
                wrong += 1

        # end game if user guesses the answer
        if wrong == 0:
            print("\nYou got it! The word was: " + word)
            print(f"You had {user_pts} points")
            break

        # ask the user for a letter
        guess = input("\nGuess a letter: ")

        if guess == '!':
            # If user guesses '!' end game
            print("\nGame Quit by User")
            exit(0)

        elif guess not in word:
            if guess not in guesses:
                # Subtract 1 from their score
                user_pts -= 1

                # End game if pts = 0
                if user_pts == 0:
                    print("\nYou lost! The word was \'" + word + "\'")
                    exit(0)

                # If the letter is not in the word
                print(f'Sorry, guess again. You have {user_pts} points')
                guesses.append(guess)
            else:
                print(f"You've already guessed {guess}!")

        else:
            if guess not in guesses:
                # Add 1 point to their score
                user_pts += 1

                # If the letter is in the word
                print(f'Right! You have {user_pts} points')
                guesses.append(guess)
            else:
                print(f"You've already guessed {guess}!")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        # print an error message and exit the program if no sysarg provided
        print('No sysarg provided!')
    else:
        filepath = sys.argv[1]
        contents = read_file(filepath)
        calculate_lexical_diversity(contents)
        tokens, nouns = preprocess(contents)
        top_50 = make_dict(tokens, nouns)
        guessing_game(top_50)
