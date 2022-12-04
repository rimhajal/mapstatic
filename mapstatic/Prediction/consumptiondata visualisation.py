#!/usr/bin/env python
# coding: utf-8

# In[116]:


import pandas as pd
import numpy as np
import pooch 
import os
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)
import matplotlib.pyplot as plt
from datetime import datetime
import csv
import plotly.express as px
import pooch  # download data / avoid re-downloading
from IPython import get_ipython
from prophet import Prophet
from statsmodels.tools.eval_measures import rmse
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from prophet.plot import plot_components_plotly
from prophet.plot import plot_plotly
import pandas as dp


# In[117]:


#......DATA 2020
url = "https://bit.ly/3V81yIg"
path_target = "./eco2mix-national-cons-def(3).csv"
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
data1= pd.read_csv("eco2mix-national-cons-def(3).csv",sep=";")
data1=data1[['Date','Heure','Consommation (MW)']]
    


# In[118]:


## Changing time format
time_improved = pd.to_datetime(data1['Date'] + ' ' + data1['Heure'],format='%Y-%m-%d %H:%M')
data1['Temps'] = time_improved  
data1.set_index('Temps', inplace=True) 
del data1['Heure']
del data1['Date']
data1 = data1.sort_index(ascending=True)


# In[119]:


## Remplacer les Nan par la moyenne de la colonne
for nan in range(len(data1)-1):  
        if data1[['Consommation (MW)']].isna().iloc[:,0][nan]:
            data1['Consommation (MW)'][nan] = (data1['Consommation (MW)'][nan-1] +data1['Consommation (MW)'][nan+1])/2
            data1['Consommation (MW)'][len(data1)-1]= (data1['Consommation (MW)'][len(data1)-2]+data1['Consommation (MW)'][len(data1)-3])/2        
print("le nombre de NaN  est : ",int(data1.isna().sum()))


# In[120]:


#.......DATA 2021
url = "https://bit.ly/3UO3NRc"
path_target = "./eco2mix-national-cons-def(4).csv"
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
data2= pd.read_csv("eco2mix-national-cons-def(4).csv",sep=";")
data2=data2[['Date','Heure','Consommation (MW)']]
    ## changer le format du temps .
time_improved = pd.to_datetime(data2['Date'] +' ' + data2['Heure'],format='%Y-%m-%d %H:%M')
data2['Temps'] = time_improved  
data2.set_index('Temps', inplace=True) 
del data2['Heure']
del data2['Date']
data2021 = data2.sort_index(ascending=True)
    ## remplacer les NaN et la transformation de la consomationsur chaque 15 min.
for nan in range(len(data2)-1):  
        if data2[['Consommation (MW)']].isna().iloc[:,0][nan]:
            data2['Consommation (MW)'][nan] = (data2['Consommation (MW)'][nan-1] +data2['Consommation (MW)'][nan+1])/2
            data2['Consommation (MW)'][len(data2)-1]= (data2['Consommation (MW)'][len(data2)-2]+data2['Consommation (MW)'][len(data2)-3])/2        
print("le nombre de NaN  est : ",int(data2.isna().sum()))


# In[121]:


#....DATA 2022 from january to mai
url = "https://bit.ly/3gowmWv"
path_target = "./eco2mix-national-cons-def(5).csv"
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
data3 = pd.read_csv("eco2mix-national-cons-def(5).csv", sep=";")
    #data2022HALF1 = data2022HALF1.set_index('Date et Heure')
data3 = data3[['Date', 'Heure', 'Consommation (MW)']]
    # changer le format du temps
time_improved = pd.to_datetime(data3['Date'] +' ' + data3['Heure'],format='%Y-%m-%d %H:%M')
data3['Temps'] = time_improved
data3.set_index('Temps', inplace=True)
del data3['Heure']
del data3['Date']
data3 = data3.sort_index(ascending=True)
    # remplacer les NaN et la transformation de la consomation du 2022 sur chaque 15 min.
for nan in range(len(data3)-1):
        if data3[['Consommation (MW)']].isna().iloc[:, 0][nan]:
            data3['Consommation (MW)'][nan] = (
            data3['Consommation (MW)'][nan-1] + data3['Consommation (MW)'][nan+1])/2
            data3['Consommation (MW)'][len(data3)-1] = (data3['Consommation (MW)'][len(data3)-2]+data3['Consommation (MW)'][len(data3)-3])/2
print("le nombre de NaN  est : ", int(data3.isna().sum()))


# In[124]:


url = "https://bit.ly/3Ep9TjU"
path_target = "./eco2mix-national-tr (6).csv"
path, fname = os.path.split(path_target)
pooch.retrieve(url, path=path, fname=fname, known_hash=None,)
data4 = pd.read_csv("eco2mix-national-tr (6).csv", sep=";")
    #Data2022 = Data2022.set_index('Date et Heure')
data4 = data4[['Date', 'Heure', 'Consommation (MW)']]
    # changer le format du temps
time_improved = pd.to_datetime(data4['Date'] +' ' + data4['Heure'],format='%Y-%m-%d %H:%M')
data4['Temps'] = time_improved
data4.set_index('Temps', inplace=True)
del data4['Heure']
del data4['Date']
data4 = data4.sort_index(ascending=True)
data4 = data4.dropna()
print("le nombre de NaN  est : ",int(data4.isna().sum()))


# In[125]:


df = pd.concat([data1, data2, data3,data4], axis=0)
return df


# In[126]:


df


# In[131]:


#visualisation des données
px.area(y='Consommation (MW)',data_frame= datafinal)


# In[129]:


df.resample('Y').mean().plot()


# In[135]:





# In[ ]:




