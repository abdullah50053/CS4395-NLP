# Abdullah Hasani
# AHH190004
# NLP HW 5

import re
import urllib.request
from bs4 import BeautifulSoup
import requests as requests


def read_lines(line):
    url = line.strip()
    if url.startswith("http"):
        print(url)
        text = get_text(url)
    elif url.startswith("/"):
        print(start_url + url)
        text = get_text(start_url + url)
    text = clean_text(text)
    return text


def clean_text(text):
    text = re.sub(r'<.*?>', '', text)
    text = re.sub(r'\t', '', text)
    text = re.sub(r'\n\s*\n', '\n', text)
    text = re.sub(r'(\d+)?Sorry Something\'s gone wrong(\.)?', '', text)
    text = text.strip()
    print(text)
    return text


def get_text(url):
    try:
        html = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        return
    soup = BeautifulSoup(html, 'html.parser')
    for script in soup(["script", "style", "span", "meta", "link", "a", "footer"]):
        script.extract()
    data = soup.find_all('p')
    temp_list = list(data)  # list from filter
    temp_list = [str(i) for i in temp_list]  # convert to string
    temp_str = ''.join(temp_list)  # join list to string
    return temp_str


def write_urls():
    with open('urls.txt', 'w') as f:
        links = []
        counter = 0
        for link in soup.find_all('a'):
            link_str = str(link.get('href'))
            # if counter >= 15:
            #     break
            if "/latest/article" in link_str:
            # if "/f1/news" in link_str:
                if link_str not in links:
                    links.append(link_str)
                    f.write(link_str + '\n')
                    counter += 1


def write_text(text, line):
    fname = line[21:60] + ".txt"
    with open(fname, 'w') as f:
        f.write(text + '\n')


if __name__ == "__main__":
    start_url = "https://www.formula1.com"
    # start_url = "https://us.motorsport.com"
    r = requests.get(start_url)

    data = r.text
    soup = BeautifulSoup(data, 'html.parser')

    # write urls to a file
    write_urls()

    for line in open('urls.txt'):
        url_text = read_lines(line)
        write_text(url_text, line)
