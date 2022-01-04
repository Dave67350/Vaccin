import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import matplotlib.pyplot as plt
import bs4
from bs4 import BeautifulSoup
import requests
import time
url="https://www.data.gouv.fr/fr/datasets/donnees-relatives-aux-personnes-vaccinees-contre-la-covid-19/#"
time.sleep(1)
reponse=requests.get(url)
soup=BeautifulSoup(reponse.text, "html.parser")
print(soup.findAll('a'))
lien=soup.findAll('a')[12]
print(lien)
l=str(lien)
ls=l.split()
print(l)
print(ls)
link=ls[6]
print(link)
li=link.split('"')
print(li)
link=li[1]
print(link)
#vac=urllib.request.urlretrieve(link)
vac= urllib.request.urlopen(link).read()
vac=json.loads(vac)
print(vac)
tups=[]
dates=[]
for elt in vac:
    date=elt["date"]
    nom= elt["nom"]
    totalvaccins=elt["totalVaccines"]
    tup=(nom,totalvaccins)
    tups.append(tup)
    dates.append(date)
print(tups)
date=dates[-1]
dic={}
for k,v in tups:
    if k not in dic:
        dic[k]=[v]
    else:
        dic[k].append(v)
print(dic)
df=pd.DataFrame(dic)
print(df)
df.to_csv("vaccinregion.csv")
df.to_json("vaccinregion.json")
n=len(df.index)
n=n-1
df=df.iloc[n]
print(df)
total=df.sum()
print(total)
nam=str("{}{}{}".format(total," vaccins administrés à la date du ", date))
df.name=nam
df.plot.bar()
plt.title(nam, fontweight="bold")
plt.tick_params(axis = 'x', rotation = 90)
plt.show()
