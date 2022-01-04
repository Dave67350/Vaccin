
import urllib.request, urllib.parse, urllib.error, json
import pandas as pd
import matplotlib.pyplot as plt
vac= urllib.request.urlopen('https://www.data.gouv.fr/fr/datasets/r/16cb2df5-e9c7-46ec-9dbf-c902f834dab1')
vac=json.loads(str(vac))
cle=list(vac.keys())
print(cle)
date=cle[0]
print(date)
dic=vac["2021-01-11T20:32:45Z"]
total=0
for k,v in dic.items():
    print(v)
    v=v.split()
    v="".join(v)
    v=int(v)
    total=total+v
    print(v)
    dic[k]=v
print(dic)
nam=str("{},{},{}".format(total,"vaccins administrés à la date du", date))
s=pd.Series(dic)
s.name=nam
print(s)
s.plot.bar()
plt.title(nam)
plt.tick_params(axis = 'x', rotation = 90)
plt.show()
