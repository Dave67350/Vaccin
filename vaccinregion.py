import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv
fig,ax=plt.subplots()
df= pd.read_csv(urllib.request.urlopen('https://www.data.gouv.fr/fr/datasets/r/9b1e6c8c-7e1d-47f9-9eb9-f2eeaab60d99'), sep=";")
date=df.iloc[1,1]
df.set_index('reg', inplace=True)
df.rename(index={1: "Guadeloupe",
2: "Martinique",
3 : "Guyane",
4 : "La Réunion",
6 : "Mayotte",
11 : "Ile-de-France",
24 : "Centre-Val de Loire",
27 : "Bourgogne-Franche-Comté",
28 : "Normandie",
32 : "Hauts-de-France",
44 : "Grand Est",
52 : "Pays de la Loire",
53 : "Bretagne",
75 : "Nouvelle-Aquitaine",
76 : "Occitanie",
84 : "Auvergne-Rhône-Alpes",
93 : "Provence-Alpes-Côte d’Azur",
94 : "Corse"}, inplace=True)
df=df.drop(index=7)
df=df.drop(index=5)
df=df.drop(index=8)
#df=df.drop(index=0)
df=df[['couv_tot_complet']]
df=df.sort_values('couv_tot_complet')
print(df)
#x=list(df.index)
#y=df['couv_tot_complet']
#ax.set_xticks(x)
#barlist=ax.barh(x,y,align='center', color='lawngreen')
#df.plot.bar(legend=None, color='lawngreen')
#plt.suptitle('% population totalement vaccinée par région', fontweight='bold')
#plt.yticks(fontweight='bold', color='darkgoldenrod')
#plt.subplots_adjust(left=0.36)
#for i, v in enumerate(y):
    #ax.text(v + 1,i, str(v),va='center', color='blue', fontweight='bold')
#ax.set_frame_on(False)
#plt.tick_params(axis='x', bottom=False, labelbottom=False)
#na=str("{}{}".format("par région au ",date))
#plt.title(na, fontweight="bold")
#plt.suptitle('                       % population totalement vaccinée', fontweight='bold')
#plt.show()
