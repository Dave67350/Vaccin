import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import matplotlib.pyplot as plt
import csv
df= pd.read_csv(urllib.request.urlopen('https://www.data.gouv.fr/fr/datasets/r/9b1e6c8c-7e1d-47f9-9eb9-f2eeaab60d99'), sep=";")
print(df)
print(type(df))
date=df.iloc[1,1]
print(date)
total1=df['n_tot_dose1'].sum()
total2=df['n_tot_dose2'].sum()
total=int(total1+total2)
ppop=total1/67422000*100
npop=100-ppop
plt.figure(figsize = (8, 8))
#m=[Ppfizer, Pmoderna, Pastra]
x=[ppop, npop]
plt.pie(x, labels = ['vaccinés', 'non vaccinés'],colors = ['green', 'crimson'], explode=[0.2,0], shadow=True, autopct = lambda x: str(round(x, 2)) + '%', normalize = True)
plt.legend()
na=str("{}{}".format("% de vaccinés avec au moins une dose en France au ",date))
#plt.title(na, fontweight="bold")
#plt.show()
ppop2=total2/67422000*100
ppop1=ppop-ppop2
plt.figure(figsize = (8, 8))
#m=[Ppfizer, Pmoderna, Pastra]
y=[ppop2, ppop1, npop]
plt.pie(y, labels = ['totalement avec 2 doses', 'partiellement avec 1 dose', 'non vaccinés'],colors = ['lawngreen', 'mediumaquamarine', 'crimson'], explode=[0.2,0.1,0], shadow=True, autopct = lambda y: str(round(y, 2)) + '%', normalize = True)
plt.legend()
na2=str("{}{}".format("% de vaccinés en fonction du nb de doses en France au ",date))
plt.title(na2, fontweight="bold")
plt.show()
