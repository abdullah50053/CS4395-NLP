# Abdullah Hasani
# AHH190004
# NLP HW 6

import re
import urllib.request
import requests as requests
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize


# Starting URL to scrape from
START_URL = "https://formula1.com"


def read_lines(line):
    url = line.strip()
    text = ''
    if url.startswith("http"):
        print(url)
        text = get_text(url)
    elif url.startswith("/") or url.startswith("#"):
        print(start_url + url)
        text = get_text(start_url + url)
    text = clean_text(text)
    text = extract_sentences(text)
    print(text)
    return text


def clean_text(text):
    text = re.sub(r'<.*?>', '', text)  # remove html tags
    text = re.sub(r'\t', '', text)  # remove tabs
    text = re.sub(r'\n\s*\n', '\n', text)  # remove empty lines
    text = re.sub(r'(\d+)?Sorry Something\'s gone wrong(\.)?', '', text)  # remove error messages
    text = re.sub(r'This feature is currently not available because you need to provide consent to functional cookies\. Please update your ','', text)  # remove error messages
    text = re.sub(r'([a-z])\.([A-Z])', r'\1. \2', text)  # add space after period for sentence tokenization
    text = text.strip()  # remove leading and trailing spaces
    print(text)
    return text


def get_text(url):
    # get text from url
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        return
    soup = BeautifulSoup(html, 'html.parser')

    # remove unnecessary tags tags
    for script in soup(["script", "style", "span", "meta", "link", "a", "footer"]):
        script.extract()

    # get text from p tags
    data = soup.find_all('p')

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
        links = []
        counter = 0  # for limiting no. iterations

        # get all links from the page
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            # if counter >= 15:
            #     break

            # condition to check if link contains some specific text
            if "/latest/article" in link_str:
            # # if "/f1/news" in link_str:
                # check if link is already in the list
                if link_str not in links:
                    links.append(link_str)
                    f.write(link_str + '\n')
                    counter += 1


def write_text(text, url_line):
    fname = url_line[19:60] + ".txt"
    with open(fname, 'w') as f:
        for line in text:
            f.write(line + '\n')


def tf_idf():
    pass


def create_tf_dict():
    pass


def term_frequency(text):
    pass


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
    for url_line in open('urls.txt'):
        url_text = read_lines(url_line)
        write_text(url_text, url_line)