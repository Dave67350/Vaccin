import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import matplotlib.pyplot as plt
import csv
df= pd.read_csv(urllib.request.urlopen("https://www.data.gouv.fr/fr/datasets/r/b8d4eb4c-d0ae-4af6-bb23-0e39f70262bd"), sep=";")
print(df)
date=df.iloc[0,2]
print(date)
Pfizer=int(df.iloc[0,3])
Moderna=int(df.iloc[1,3])
Astra=int(df.iloc[2,3])
Janssen=int(df.iloc[3,3])
Total=int(df.iloc[4,3])
Ppfizer=float(Pfizer/Total*100)
Pmoderna=float(Moderna/Total*100)
Pastra=float(Astra/Total*100)
Pjanssen=float(Janssen/Total*100)
print(Ppfizer,Pmoderna,Pastra)
plt.figure(figsize = (8, 8))
#m=[Ppfizer, Pmoderna, Pastra]
plt.pie([Ppfizer, Pmoderna, Pastra, Pjanssen], labels = ['Pfizer', 'Moderna', 'Astra', 'Janssen'],autopct = lambda x: str(round(x, 2)) + '%', normalize = True)
plt.legend()
na=str("{}{}".format("% par vaccin administrés en France à la date du ",date))
plt.title(na , fontweight="bold")
plt.show()
