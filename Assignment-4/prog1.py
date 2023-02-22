# Abdullah Hasani
# ahh190004
# NLP HW 4

import sys
import os
from nltk import word_tokenize
from nltk import ngrams

def read_file(filepath):
    # Read the input file as raw text
    data = ''
    with open(filepath, 'r') as file:
        data = file.read()
    return data


if __name__ == '__main__':
    if len(sys.argv) < 2:
        # print an error message and exit the program if no sysarg provided
        print('No sysarg provided!')
    else:
        raw_text = read_file(sys.argv[1])
        print(raw_text)

