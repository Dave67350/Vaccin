import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import matplotlib.pyplot as plt
import csv
df= pd.read_csv(urllib.request.urlopen('https://www.data.gouv.fr/fr/datasets/r/9b275b84-2caa-4815-8523-2f1451e6952b'), sep=";")
print(df)
date=df['jour'][1]
janssen=df['vaccin']==4
tot=df['vaccin']==0
dftot=df[tot]
dfjanssen=df[janssen]
print(dfjanssen)
totjanssen=dfjanssen['n_tot_dose1'].sum()
print(totjanssen)
dftotdose1=dftot['n_tot_dose1']
dftotdose2=dftot['n_tot_dose2']
totdose1=dftotdose1.sum()
totdose2=dftotdose2.sum()
print(dftot)
print(totdose1)
print(totdose2)
totalvaccine=totdose2+totjanssen
partvaccine=totdose1-totjanssen-totdose2
print("totalement vaccinés", totalvaccine)
print("partiellement vaccinés", partvaccine)
ppop=totdose1/67422000*100
npop=100-ppop
plt.figure(figsize = (8, 8))
#m=[Ppfizer, Pmoderna, Pastra]
x=[ppop, npop]
plt.pie(x, labels = ['vaccinés', 'non vaccinés'],colors = ['green', 'crimson'], explode=[0.2,0], shadow=True, autopct = lambda x: str(round(x, 2)) + '%', normalize = True)
na=str("{}{}".format("% de vaccinés avec au moins une dose en France au ",date))
plt.title(na, fontweight="bold")
nat=str("{}{}".format(totdose1, " français vaccinés"))
plt.suptitle(nat, fontweight="bold")
#plt.show()
ppop2=totalvaccine/67422000*100
ppop1=partvaccine/67422000*100
plt.figure(figsize = (8, 8))
#m=[Ppfizer, Pmoderna, Pastra]
y=[ppop2, ppop1, npop]
plt.pie(y, labels = ['totalement avec 1 ou 2 doses', 'partiellement avec 1 dose', 'non vaccinés'],colors = ['lawngreen', 'mediumaquamarine', 'crimson'], explode=[0.2,0.1,0], shadow=True, autopct = lambda y: str(round(y, 2)) + '%', normalize = True)
na2=str("{}{}".format("% de vaccinés en fonction du nb de doses en France au ",date))
plt.title(na2, fontweight="bold")
plt.suptitle(nat, fontweight="bold")
plt.show()
