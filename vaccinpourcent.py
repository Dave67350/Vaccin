import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import matplotlib.pyplot as plt
import bs4
from bs4 import BeautifulSoup
import requests
import time
vac= urllib.request.urlopen("https://www.data.gouv.fr/fr/datasets/r/349bba1b-21d3-4763-9b47-419407d9ab4e").read()
vac=json.loads(vac)
print(vac)
l=[]
for dic in vac:
    elts= dic['fields']
    print(dic['fields'])
    l.append(elts)
print(l)
tups=[]
dates=[]
for dic in l:
    print(dic.keys())
    if 'percent_pop_vac' in dic.keys():
        date=dic['date']
        nom=dic['reg_name']
        totalvaccins=dic['total_vaccines']
        pcentpop=dic['percent_pop_vac']
        tup=(date,nom,totalvaccins, pcentpop)
        tups.append(tup)
        dates.append(date)
    else:
        continue
print(tups)
df=pd.DataFrame(tups, columns=['date','nom','totvaccins','%pop'])
recent=df['date'].max()
print(recent)
df.sort_values(by=['date','nom'], inplace=True)
df.set_index('date', inplace=True)
df=df.tail(17)
df.set_index('nom', inplace=True)
total=df['totvaccins'].sum()
print(total)
df.sort_values(by=['totvaccins'], ascending=[False], inplace=True)
print(df)
nam=str("{}{}{}".format(total," vaccins administrés à la date du ", recent))
df.name=nam
df.plot( kind='bar', secondary_y='%pop')
plt.title(nam, fontweight="bold")
plt.tick_params(axis = 'x', rotation = 90)
plt.show()
#date=dates[-1]
#dic={}
#for n,t,p in tups:
    #if n not in dic:
        #dic[n]=[t,p]
    #else:
        #dic[k].append(t,p)
#print(dic)
#df=pd.DataFrame(dic)
#print(df)
#n=len(df.index)
#n=n-1
#df=df.iloc[n]
#print(df)
#total=df.sum()
#print(total)
#nam=str("{}{}{}".format(total," vaccins administrés à la date du ", date))
#df.name=nam
#df.plot.bar()
#plt.title(nam, fontweight="bold")
#plt.tick_params(axis = 'x', rotation = 90)
#plt.show()
