# Abdullah Hasani
# ahh190004
# NLP HW 2

# assumes sysarg is /anat19.txt
import os
import sys
import nltk
import re
from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


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
    # print(nouns)
    print('Number of tokens: ' + str(len(new_tokens)))
    print('Number of nouns:' + str(len(nouns)))
    return new_tokens, nouns


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('No sysarg provided!')
    else:
        filepath = sys.argv[1]
        print("The file path is " + filepath)
        contents = read_file(filepath)
        calculate_lexical_diversity(contents)
        tokens, nouns = preprocess(contents)

