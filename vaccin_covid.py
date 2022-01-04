import pandas as pd
import matplotlib.pyplot as plt
vac= {"2021-01-11T20:32:45Z":{"Auvergne-Rhône-Alpes":"12 037","Bourgogne-Franche-Comté":"7 114","Bretagne":"4 534","Corse":"958","Centre-Val-de-Loire":"4 257","Grand Est":"11 335","Hauts-de-France":"10 162","Île-de-France":"30 248","Nouvelle Aquitaine":"18 841","Normandie":"12 300","Occitanie":"12 582","Provence-Alpes-Côte-D'azur":"6 726","Pays-de-la-Loire":"7 002","Guadeloupe":"96","Martinique":"159"}}
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
