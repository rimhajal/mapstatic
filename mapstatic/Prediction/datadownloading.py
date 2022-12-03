#%%
#importing modules
import pandas as pd
import numpy as np
import pooch 
import os
import matplotlib.pyplot as plt
from datetime import datetime
import csv


url = 'https://odre.opendatasoft.com/explore/dataset/eco2mix-regional-cons-def/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
path_target = './data/consumptiondata.csv'

#defining a class to download the data
class datadownloading():
    '''downloading the dataframe'''
    def __init__(selfurl=url, target_name=path_target):
        path, fname = os.path.split(path_target)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)
    '''reading the dataframe'''
    def saving():
        dataframe = pd.read_csv(path_target, usecols=['Date','Heure','Consommation (MW)','Thermique (MW)','Nucléaire (MW)','Eolien (MW)','Solaire (MW)','Hydraulique (MW)'], delimiter=";", comment="#", na_values="", parse_dates=['Date'])
        dataframe.rename(columns = {'Date':'date','Heure':'hour','Consommation (MW)':'consumption','Thermique (MW)':'thermal','Nucléaire (MW)':'nuclear','Eolien (MW)':'wind','Solaire (MW)':'solar','Hydraulique (MW)':'hydraulic'}, inplace=True)
        dataframe.index = pd.to_datetime(dataframe.index)
        dataframe.set_index('date', inplace=True)
        dataframe = dataframe.loc[['2013-12-08', '2014-12-08', '2015-12-08', '2016-12-08', '2017-12-08', '2018-12-08', '2019-12-08', '2020-12-08', '2021-12-08']]
        return(dataframe)

classe = datadownloading()
dataframe = datadownloading.saving()
print(dataframe)
dataframe.get('date')

