#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import numpy as np
df=pd.read_csv(('https://www.data.gouv.fr/fr/datasets/r/9b275b84-2caa-4815-8523-2f1451e6952b'),sep=";")
df=df[df['vaccin']==0]
df.index=df['reg']
df


# In[2]:


df2=pd.read_csv(('https://www.data.gouv.fr/fr/datasets/r/46f145d4-9607-45a0-bc3c-86241136ca24'),encoding='utf8',sep=";")
df2
jour=df2.iloc[-1,1]
jour
df2=df2[df2['jour']==jour]
df2
df2.index=df2['reg']
del df2['jour']
#df2.dtypes
#df2.columns
df2['tx_indic_7J_DC'] = df2['tx_indic_7J_DC']#.map(lambda x: float(x.replace(",",".")))
df2['tx_indic_7J_hosp'] = df2['tx_indic_7J_hosp']#.map(lambda x: float(x.replace(",",".")))
df2['tx_indic_7J_SC'] = df2['tx_indic_7J_SC']#.map(lambda x: float(x.replace(",",".")))
df2['tx_prev_hosp'] = df2['tx_prev_hosp']#.map(lambda x: float(x.replace(",",".")))
df2['tx_prev_SC'] = df2['tx_prev_SC']#.map(lambda x: float(x.replace(",",".")))
#df2 = df2.transform(pd.to_numeric, errors='coerce')
#df2 = df2.apply(pd.to_numeric)
df2.dtypes
df2


# In[3]:


df3=pd.merge(df,df2,left_index=True, right_index=True)
df4=pd.concat([df,df2], axis=1)
df4
df4=df4.loc[:,['jour','n_tot_dose2','n_tot_dose3','tx_indic_7J_DC','tx_indic_7J_hosp','tx_indic_7J_SC','tx_prev_hosp','tx_prev_SC']]
df4=df4.drop([1,2,3,4,6])
df4
sns.pairplot(df4)


# In[4]:


df5=pd.read_csv(('https://www.data.gouv.fr/fr/datasets/r/9b1e6c8c-7e1d-47f9-9eb9-f2eeaab60d99'), sep=";")
df5.index=df5['reg']
df5=df5.loc[:,['reg','couv_tot_dose1','couv_tot_complet','couv_tot_rappel']]
#df5=df5.drop([7,8])
df5


# In[5]:


df6=pd.concat([df4,df5], axis=1)
#df6=df6.drop(['n_tot_dose2'], axis=1)
#del df6['couv_tot_rappel']
del df6['couv_tot_dose1']
del df6['n_tot_dose2']
del df6['n_tot_dose3']
#del df6['tx_indic_7J_DC']
#del df6['tx_indic_7J_hosp']
#del df6['tx_indic_7J_SC']
del df6['jour']
df6


# In[6]:


import pandas.plotting as pp
pp.scatter_matrix(df6, alpha=0.5)


# In[7]:


df6
#tx_indic_7J_DC = Nombre de personnes décédées durant les 7 derniers jours
#tx_indic_7J_hosp = Nombre de nouvelles hospitalisation los des 7 derniers jours
#tx_indic_7J_SC = Nombre d'hospitalisation en soin critique lors des 7 derniers jours
#tx_prev_hosp = Nombre total de personnes hospitalisées
#tx_prev_SC = Nombre total de personnes en soin critique
#dfDC7=df6.loc[:,['jour', 'tx_indic_7J_DC', 'couv_tot_dose1', 'couv_tot_complet','couv_tot_rappel']]
#dfhosp7=df6.loc[:,['jour', 'tx_indic_7J_hosp', 'couv_tot_dose1', 'couv_tot_complet','couv_tot_rappel']]
#dfSC=df6.loc[:,['jour', 'tx_indic_7J_SC', 'couv_tot_dose1', 'couv_tot_complet','couv_tot_rappel']]
#dfhosptot=df6.loc[:,['jour', 'tx_prev_hosp', 'couv_tot_dose1', 'couv_tot_complet','couv_tot_rappel']]
#dfSCtot=df6.loc[:,['jour', 'tx_prev_SC', 'couv_tot_dose1', 'couv_tot_complet','couv_tot_rappel']]


# In[8]:


#df6
#type(df6.iloc[2,1])


# In[9]:


sns.pairplot(df6)
#pp.scatter_matrix(dfDC7, alpha=0.5)


# In[10]:


pp.scatter_matrix(df6, alpha=0.5)


# In[11]:


#pp.scatter_matrix(dfSCtot, alpha=0.5)


# In[12]:


#import seaborn as sns
#sns.pairplot(df6)


# In[13]:


import numpy as np
#dffin=df6.drop(['couv_tot_dose1','tx_indic_7J_DC'], axis=1)
dffin=df6.rename(columns={'tx_prev_hosp':'tx_precedent_hosp','tx_prev_SC':'tx_precedent_SC','reg':'region','couv_tot_complet':'couverture vaccinale'})
dffin.index.name = 'region'
#del dffin['n_tot_dose2']
#del dffin['n_tot_dose3']
#del dffin['jour']
#del dffin['tx_precedent_hosp']
#del dffin['tx_precedent_SC']
#del dffin['couv_tot_rappel']
dffin['region'].replace({11 : "Ile-de-France",
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
dffin


# In[14]:


#pp.scatter_matrix(dffin, alpha=0.5)
sns.pairplot(dffin)
#sns.pairplot(dffin, x_vars=['couv_tot_complet','tx_precedent_hosp','tx_precedent_SC'], y_vars=['tx_indic_7J_hosp','tx_indic_7J_SC'], kind='reg')


# In[15]:


plot=sns.pairplot(dffin, x_vars=['couverture vaccinale','tx_precedent_hosp','tx_precedent_SC'], y_vars=['tx_indic_7J_hosp','tx_indic_7J_SC','tx_indic_7J_DC'], kind='reg')


# In[16]:


#plot.savefig('relationvaccin.png')


# In[17]:


#dfcouv=dffinmetro.iloc[:,[3,4,5]]
#dfcouv


# In[18]:


from scipy.stats import pearsonr
#y=dfcouv['tx_precedent_SC']
#y2=dfcouv['tx_precedent_hosp']
#x=dfcouv['couv_tot_complet']
#stat, p= pearsonr(x,y)
#stat2, p2=pearsonr(x,y2)
#stat,p,stat2,p2


# In[19]:


import matplotlib.pyplot as plt
def corrfunc(x, y, **kws):
    (r, p) = pearsonr(x, y)
    ax = plt.gca()
    ax.annotate("r = {:.2f} ".format(r),
                xy=(.2, .9), xycoords=ax.transAxes)
    ax.annotate("p = {:.8f}".format(p),
                xy=(.5, .8), xycoords=ax.transAxes)
plot.map(corrfunc)


# In[20]:


plot.savefig('relationvaccin2.png')


# In[23]:


plot2=sns.pairplot(dffin, y_vars=['couverture vaccinale'], x_vars=['tx_indic_7J_hosp','tx_indic_7J_SC','tx_indic_7J_DC'], kind='reg')
plot2.fig.set_size_inches(10,5)
ax2=plot2.map(corrfunc)
plot3=sns.pairplot(dffin, y_vars=['couverture vaccinale'], x_vars=['tx_indic_7J_hosp','tx_indic_7J_SC','tx_indic_7J_DC'], kind='reg', hue='region')
plot3.fig.set_size_inches(15,5)
na=str("{}{}".format("corrélation vaccination/hosp/soins critiques SC/décès moyenne 7j au ", jour))
#plt.title()
ax3=plot3.fig.suptitle(na, fontweight="bold", va='bottom')


# In[24]:


import matplotlib.pyplot as plt
plot2.map(corrfunc)
plot2.fig.set_size_inches(20,20)
na=str("{}{}".format("vaccination coverage/hosp/critical care SC/death DC au ", jour))
#plt.title()
plot2.fig.suptitle(na, fontweight="bold")


# In[26]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:
