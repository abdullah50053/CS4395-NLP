# Abdullah Hasani
# AHH190004
# NLP HW 5

import re
import os
import random
import nltk
import urllib.request
from nltk.corpus import stopwords
from urllib.request import Request
from urllib.error import URLError
import requests as requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

# Starting URL to scrape from
START_URL = "https://us.motorsport.com/f1/"


def read_lines(line):
    url = line.strip()  # remove leading and trailing spaces
    text = ''

    # check if url is relative or absolute
    if url.startswith("http"):
        print(url)
        text = get_text(url)
    elif url.startswith("/") or url.startswith("#"):
        print(start_url + url)
        text = get_text(start_url + url)

    # check if text is empty
    if not text:
        return

    # clean text
    text = clean_text(text)

    # extract sentences
    text = extract_sentences(text)
    return text


def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # remove html tags
    text = re.sub(r'\t', '', text)  # remove tabs
    text = re.sub(r'\n\s*\n', '\n', text)  # remove empty lines
    text = re.sub(r'\xa0', ' ', text)  # remove nonbreaking spaces
    text = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', text)  # add space after period for sentence tokenization
    text = re.sub(r'\[\d+\]', '', text)  # remove references
    text = re.sub(r'^\s.*\n?', '', text, flags=re.MULTILINE)  # remove lines that start with space
    text = text.strip()  # remove leading and trailing space
    return text.lower()


def get_text(url):
    user_agents_list = [
        'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    ]

    req = Request(url, headers={'User-Agent': user_agents_list[random.randint(0, 2)]})

    # get text from url
    try:
        html = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print(e)
        return

    soup = BeautifulSoup(html, 'html.parser')

    # remove unnecessary tags
    for script in soup(["script", "style", "span", "meta", "link", "footer"]):
        script.extract()

    # get text from p tags
    # data = soup.find_all(['p', 'a'])

    # get text from all tags
    data = soup.get_text()
    # print(data)

    # convert list to string
    temp_list = list(data)  # list from filter
    temp_list = [str(i) for i in temp_list]
    temp_str = ''.join(temp_list)  # join list to string
    return temp_str


def extract_sentences(text):
    # extract sentences from text
    sentences = sent_tokenize(text)
    return sentences


def write_urls():
    with open('urls.txt', 'w') as f:
        links = ["#"]
        f.write(links[0] + '\n')
        counter = 0  # for limiting no. iterations

        # get all links from the page
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))

            if counter >= 2:
                break

            # condition to check if link contains some specific text
            if not link_str.startswith("#") and not link_str.startswith("//") and not link_str.startswith("/w") and 'wiki' not in link_str:
                # check if link is already in the list
                if link_str not in links:
                    links.append(link_str)
                    f.write(link_str + '\n')
                    counter += 1


def write_text(text, counter):
    fname = str(counter) + ".txt"
    with open(fname, 'w') as f:
        for line in text:
            f.write(line + '\n')


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
    counter = 0
    for url_line in open('urls.txt'):
        url_text = read_lines(url_line)
        if url_text:
            write_text(url_text, counter)
        counter += 1


    # find important words in the text
    dir = os.getcwd()

    for filename in os.listdir(dir):
        if filename.endswith(".txt"):
            with open(filename, 'r') as f:
                most_common = {}
                for line in f:
                    line = line.split()
                    for word in line:
                        if word not in stopwords.words('english'):
                            if word in most_common:
                                most_common[word] += 1
                            else:
                                most_common[word] = 1
                sort_dict = dict(sorted(most_common.items(), key=lambda item: item[1]))

                top_50 = []
                for i in reversed(sort_dict):
                    top_50.append(i)
                top_50 = top_50[:50]

                # Print the 50 most common words and their counts
                print("Top 50 most common words:")
                for i in top_50:
                    print(i + ':' + str(most_common[i]))



