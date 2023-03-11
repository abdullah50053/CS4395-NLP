# Abdullah Hasani
# AHH190004
# NLP HW 6

import re
import os
import random
import json
import pickle
import urllib.request
from nltk.corpus import stopwords
from urllib.request import Request
from urllib.error import URLError
import requests as requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

# Starting URL to scrape from
START_URL = "https://en.wikipedia.org/wiki/Formula_One"


def set_url(url):
    text = ''
    # check if url is relative or absolute
    if url.startswith("http"):
        print(url)
        text = get_text(url)
    elif url.startswith("/") or url.startswith("#"):
        print(start_url + url)
        text = get_text(start_url + url)
    return text


def read_lines(line):
    # remove leading and trailing spaces
    url = line.strip()

    # check if url is relative or absolute
    text = set_url(url)

    # check if text is empty
    if not text:
        return

    # clean text
    text = clean_text(text)

    # extract sentences
    text = extract_sentences(text)

    # post process text
    text = post_process(text)

    return text


def post_process(text):
    t = []
    for sent in text:
        sent = re.sub(r'^\W*(\w+\W+){0,2}\w+\W*$', '', sent, flags=re.MULTILINE)  # remove lines with less than 3 words
        sent = re.sub(r'\n\s*\n', '\n', sent)  # remove empty lines
        sent = re.sub(r'\.', '', sent)  # remove periods
        t.append(sent)

    return t


def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # remove html tags
    text = re.sub(r'\d+', '', text)  # remove numbers
    text = re.sub(r'[,:;()\[\]$]', '', text)  # remove punctuation
    text = re.sub(r'\n\s*\n', '\n', text)  # remove empty lines
    text = re.sub(r'\xa0', ' ', text)  # remove NBSP
    text = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', text)  # add space after period for sentence tokenization
    text = re.sub(r'^\s.*\n?', '', text, flags=re.MULTILINE)  # remove lines that start with space
    text = re.sub(r'[\'\"/]', '', text)  # remove quotes
    text = re.sub(r'-', ' ', text)  # replace hyphens with space
    text = re.sub(r'–', '', text)  # remove hyphens
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = text.strip().lower()  # remove leading and trailing spaces and convert to lowercase
    return text


def get_text(url):
    # define list of user agents
    user_agents_list = [
        'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    ]

    # set user agent randomly to avoid being blocked
    req = Request(url, headers={'User-Agent': user_agents_list[random.randint(0, 2)]})

    # check if url is valid
    try:
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e)
        return

    # parse html
    soup = BeautifulSoup(html, 'html.parser')

    # remove unnecessary tags
    for script in soup(["script", "style", "span", "meta", "link", "footer"]):
        script.extract()

    # get text from all tags
    data = soup.get_text()

    # convert list to string
    temp_str = ''.join(data)  # join list to string
    return temp_str


def extract_sentences(text):
    # extract sentences from text
    sentences = sent_tokenize(text)
    return sentences


def write_urls():
    with open('urls.txt', 'w') as f:
        # write the starting url to the file
        links = ["#"]
        f.write(links[0] + '\n')

        counter = 0

        # get all links from the page
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))

            # counter to limit no. iterations
            if counter >= 15:
                break

            # condition to check if link contains some specific text
            if not link_str.startswith("#") and not link_str.startswith("//") and not link_str.startswith("/w")\
                    and not link_str.startswith('http:') and 'wiki' not in link_str and 'archive' not in link_str:

                # check if link is already in the list
                if link_str not in links:
                    links.append(link_str)
                    f.write(link_str + '\n')
                    counter += 1


def write_text(text, counter):
    # write text to file
    fname = str(counter) + ".txt"
    with open(fname, 'w') as file:
        for line in text:
            file.write(line + '\n')


def pickle_data(knowledge_base):
    # pickle data
    with open('kb.pickle', 'wb') as file:
        pickle.dump(knowledge_base, file)


def create_knowledge_base():
    # create knowledge base
    with open('kb.txt', 'r') as f:
        kb = json.load(f)
    return kb


def read_write_urls():
    # read urls from file and write text to file
    counter = 0
    for url_line in open('urls.txt'):
        url_text = read_lines(url_line)
        if url_text:
            write_text(url_text, counter)
        counter += 1


def find_important_words():
    # find the most common words in the corpora
    dir = os.getcwd()
    most_common = {}

    # loop through all files in the directory
    for filename in os.listdir(dir):

        # check if file is a text file
        if filename.endswith(".txt"):

            # open file and read line by line
            with open(filename, 'r') as f:
                for line in f:
                    line = line.split()
                    for word in line:

                        # check if word is not a stop word
                        if word not in stopwords.words('english'):
                            if word in most_common:
                                most_common[word] += 1
                            else:
                                most_common[word] = 1
    return most_common


def top_words(sort_dict, most_common):
    # Get the 30 most common words
    top_30 = []
    for i in reversed(sort_dict):
        top_30.append(i)
    top_30 = top_30[:30]

    # Print the 30 most common words and their counts
    print_top_words(top_30, most_common)


def print_top_words(top_30, most_common):
    # Print the 30 most common words and their counts
    print("Top 30 most common words:")
    for i in top_30:
        print(i + ':' + str(most_common[i]))


if __name__ == "__main__":
    # get the starting url
    start_url = START_URL

    # get the html
    r = requests.get(start_url)

    # parse the html
    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    # write urls to a file
    write_urls()

    # read urls from file and write text to file
    read_write_urls()

    # find important words in the text
    most_common = find_important_words()

    # Sort the dictionary by value
    sort_dict = dict(sorted(most_common.items(), key=lambda item: item[1]))

    # Get the top 30 words
    top_words(sort_dict, most_common)

    # Top 10 words/phrases:
    top_10 = ['formula one', 'race', 'season', 'championship', 'team', 'driver', 'grand prix', 'car', 'points', 'fia']

    # create knowledge base
    knowledge_base = create_knowledge_base()

    # pickle knowledge base
    pickle_data(knowledge_base)
