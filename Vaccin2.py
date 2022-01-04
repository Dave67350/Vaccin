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
total=total1+total2
print(date,total,total1,total2)
df=df.iloc[:,0:4]
del df['jour']
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
dict={"Guadeloupe":393401, "Martinique":373762,"Guyane":278472,"La Réunion":865507,"Mayotte":256500,"Ile-de-France":12328447,"Centre-Val de Loire":2631697,"Bourgogne-Franche-Comté":2881889,
"Normandie":3400150,
"Hauts-de-France":6096682,
"Grand Est":5658527,
"Pays de la Loire":3871617,
"Bretagne":3425074,
"Nouvelle-Aquitaine":6117956,
"Occitanie":6009622,
"Auvergne-Rhône-Alpes":8167945,
"Provence-Alpes-Côte d’Azur":5128856,
"Corse":343726}
s=pd.Series(dict, name="pop")
d=pd.concat([df,s], axis=1)
d.rename(columns={"n_tot_dose1":"dose1","n_tot_dose2":"dose2"}, inplace=True)
d["%pop"]=d["dose1"]/d["pop"]*100
print(d)
d=d.drop(index=7)
del d['pop']
print(d)
d.sort_values(by=['dose1'], ascending=[False], inplace=True)
print(d)
print (type(d))
nam=str("{}{}{}{}".format(total1," vaccinés dont ",total2," avec 2 doses"))
d.name=nam
d.plot( kind='bar', secondary_y='%pop')
plt.title(nam, fontweight="bold")
plt.tick_params(axis = 'x', rotation = 90)
plt.suptitle(date, fontweight="bold")
plt.show()

#for line in vac:
    #line=str(line)
    #line=line.rstrip("\n")
    #print(line)
    #print(type(line))
    #line=line.rstrip("\n")
    #line=line.split(";")
    #print(line)
    #list_lines.append(line)
#vac=json.loads(str(vac))
#cle=list(vac.keys())
#print(cle)
#date=cle[0]
#print(date)
#dic=vac["2021-01-11T20:32:45Z"]
#total=0
#for k,v in dic.items():
    #print(v)
    #v=v.split()
    #v="".join(v)
    #v=int(v)
    #total=total+v
    #print(v)
    #dic[k]=v
#print(dic)
#nam=str("{},{},{}".format(total,"vaccins administrés à la date du", date))
#s=pd.Series(dic)
#s.name=nam
#print(s)
#s.plot.bar()
#plt.title(nam)
#plt.tick_params(axis = 'x', rotation = 90)
#plt.show()
