import matplotlib.pyplot as plt
import requests
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer

def gutenberg_plot(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    words = soup.get_text()
    lowered = []
    for word in words:
        lowered.append(word.lower()) 
    text = nltk.Text(lowered)
    fdist = nltk.FreqDist(text)
    fdist.plot(30)

