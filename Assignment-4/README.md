# Assignment 4

## Overview

### Program 1:
Program 1 reads the raw text files and creates bigram and unigram dictionaries for each language.
The program then pickles the dictionaries and saves them to the current directory.

### Program 2:
Program 2  uses the bigram and unigram dictionaries created in Program 1 to classify the language of a given text.
The program uses Laplace smoothing to calculate the probability of a bigram in a given text.
Using the probabilities of the bigrams in the text, the program classifies the language of the text as English, French, or Italian and prints the results to a file. 
The program then compares the output file with the correct solution file and prints the accuracy and the line numbers of the incorrectly classified lines.

