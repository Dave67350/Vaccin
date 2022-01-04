import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import urllib.request
df= pd.read_csv(urllib.request.urlopen('https://www.data.gouv.fr/fr/datasets/r/b8d4eb4c-d0ae-4af6-bb23-0e39f70262bd'), sep=";")
print(df, df.shape)
date=df.iloc[1,2]
print(date)
#janssen=df['vaccin']==4
#tot=df['vaccin']==0
#dftot=df[tot]
#dfjanssen=df[janssen]
#totjanssen=dfjanssen['n_tot_dose1'].sum()
dftotdose1=df.iloc[4,3]
dftotdose2=df.iloc[4,4]
dftotdose3=df.iloc[4,5]
dftotdose4=df.iloc[4,6]
#totdose1=dftotdose1.sum()
#totdose2=dftotdose2.sum()
#totalvaccine=totdose2+totjanssen
#partvaccine=totdose1-totjanssen-totdose2
ppop=dftotdose1/67407000*100
ppop2=(dftotdose2-dftotdose3)/67407000*100
ppop3=(dftotdose3)/67407000*100
ppop4=dftotdose4/67407000*100
ppop1=(dftotdose1-dftotdose2)/67407000*100
npop=100-ppop
#plt.figure(figsize = (8, 8))
#m=[Ppfizer, Pmoderna, Pastra]
x=[ppop1,ppop2,ppop3,npop]
plt.pie(x, labels = ['vaccinés avec 1 dose','vaccinés avec 2 doses','vaccinés avec 3 doses', 'non vaccinés'], shadow=True, colors = ['green','forestgreen','limegreen','crimson'], explode=[0.2,0.15,0.10,0], autopct = lambda x: str(round(x, 2)) + '%', normalize = True)
#    plt.legend()
#na=str("{}{}".format("% de vaccinés en France au ",date))
#plt.title(na, fontweight="bold")
nat=str("{}{}{}".format(dftotdose1, " français vaccinés au ",date))
plt.suptitle(nat, fontweight="bold")
plt.show()
#    plt.savefig('media/ppop.png')
