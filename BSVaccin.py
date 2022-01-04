import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen("https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19/")
soup = BeautifulSoup(resp, from_encoding=resp.info().get_param('charset'))

for link in soup.find_all('a', href=True):
    print(link['href'])
