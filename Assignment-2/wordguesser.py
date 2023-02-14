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
from random import randint


def read_file(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        text_in = f.read()
    print("\nThe current file reads:")
    return text_in


def calculate_lexical_diversity(text):
    nltk.download('popular')
    tokens = word_tokenize(text)
    token_set = set(tokens)
    lexical_diversity = len(token_set)/len(tokens)
    print("Lexical Deversity: %.2f" % lexical_diversity)


def preprocess(text):
    clean_text = re.sub(r'[.?!,:;()\-\n\d]', ' ', text.lower())
    tokens = word_tokenize(clean_text)
    stop_words = stopwords.words('english')
    new_tokens = [t for t in tokens if t not in stop_words and len(t) > 5]
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in new_tokens]
    lemmas = list(set(lemmas))
    tags = nltk.pos_tag(lemmas)
    ftwenty = tags[:20]
    print("First 20 tags: ")
    print(ftwenty)
    noun_list = ['NN', 'NNS', 'NNP', 'NNPS']
    nouns = [t for t in tags if t[1] in noun_list]
    print('Number of tokens: ' + str(len(new_tokens)))
    print('Number of nouns:' + str(len(nouns)))
    return new_tokens, nouns


def make_dict(tokens, nouns):
    new_dict = {}
    new_nouns = [i[0] for i in nouns if i[0] in tokens]
    for i in new_nouns:
        new_dict[i] = tokens.count(i)
    sort_dict = dict(sorted(new_dict.items(), key=lambda item: item[1]))
    top_50 = []
    for i in reversed(sort_dict):
        top_50.append(i)
    top_50 = top_50[:50]
    print("Top 50 most common words:")
    for i in top_50:
        print(i)
    return top_50


def guessing_game(t50):
    user_pts = 5
    print(f"The game has begun! You have {user_pts} points.")
    word = random.choice(t50)
    guesses = []

    while user_pts > 0:
        wrong = 0
        for i in word:
            if i in guesses:
                print(i, end=' ')
            else:
                print('_', end=' ')
                wrong += 1

        if wrong == 0:
            print("\nYou got it! The word was: " + word)
            break

        guess = input("\nGuess a letter: ")
        guesses.append(guess)

        if guess not in word:
            print('Sorry, guess again.')
            user_pts -= 1
        elif guess == '!':
            print("Game Quit")
            exit(0)
        else:
            print('Right!')
            user_pts += 1

        if user_pts == 0:
            print("\nYou lost! The word was " + word)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No sysarg provided!')
    else:
        filepath = sys.argv[1]
        print("The file path is " + filepath)
        contents = read_file(filepath)
        calculate_lexical_diversity(contents)
        tokens, nouns = preprocess(contents)
        top_50 = make_dict(tokens, nouns)
        guessing_game(top_50)