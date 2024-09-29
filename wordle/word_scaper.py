# word_collector.py

# imports
import requests
import json
from bs4 import BeautifulSoup
from string import ascii_uppercase

URL = input("Please provide an url to scrape for words > ")

def start(url):
    '''Load url and parse for words'''
    word_list=[]
    url_text = requests.get(url).text
    soup = BeautifulSoup(url_text, 'html.parser')
    for text in soup.get_text().replace('\n',' ').split():
        if all(letter in ascii_uppercase for letter in text.upper()):             
            word_list.append(text.lower())
    # print(word_list)
    return word_list

if __name__ == '__main__':
    with open('../wordle/wordlist.txt', 'w') as file:
        file.write("\n".join(start(URL)))
