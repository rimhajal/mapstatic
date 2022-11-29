#importing modules
import pandas as pd
import numpy as np
import pooch 
import os
import matplotlib.pyplot as plt
from datetime import datetime

#defining a class to download the data
class datadownloading:
    '''downloading the dataframe'''
    def __init__(self):
        url = 'https://odre.opendatasoft.com/explore/dataset/eco2mix-regional-cons-def/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B'
        path_target = './data/consumptiondata.csv'
        path, fname = os.path.split(path_target)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)
    '''reading the dataframe'''
    @staticmethod
    def read():
        dataframe = pd.read_csv("consumptiondata.csv", delimiter=";", comment="#", na_values="", parse_dates=['Date'])
        return(dataframe)

#calling the dataframe from the previous class
classe = datadownloading()
data = datadownloading.read()
print(data)

#shaping the data to improve their use
data = data.loc[["2013-12-08", "2014-12-08", "2015-12-08", "2016-12-08", "2017-12-08", "2018-12-08", "2019-12-08", "2020-12-08", "2021-12-08"]]
data = data.rename(columns = {'Date':'date', 'Heure':'hour', 'Consommation (MW)':'consumption', 'Thermique (MW)':'thermal', 'Nucléaire (MW)':'nuclear', 'Eolien (MW)':'wind', 'Solaire (MW)':'solar', 'Hydraulique (MW)':'hydraulic' ''})
data = data.set_index('date')
data.index = pd.to_datetime(data.index)

#creating all the energy dataframes and visualizing them
'''global consumption'''
consumptiondata = data[['hour', 'consumption']]
consumptiondata.dropna(inplace = True)
consumptiondata.set_index('hour', inplace=True)
consumptiondata = consumptiondata.sort_values(by='hour', ascending=True)
consumptiondata.plot(style='.', figsize=(20, 5), title=" French Global Energy Consumption (MW)")
'''thermal'''
thermaldata = data[['hour', 'thermal']]
thermaldata.dropna(inplace = True)
thermaldata.set_index('hour', inplace=True)
thermaldata = thermaldata.sort_values(by='hour', ascending=True)
thermaldata.plot(style='.', figsize=(20, 5), title="French Thermal Energy Consumption (MW)")
'''nuclear'''
nucleardata = data[['hour', 'nuclear']]
nucleardata.dropna(inplace = True)
nucleardata.set_index('hour', inplace=True)
nucleardata = nucleardata.sort_values(by='hour', ascending=True)
nucleardata.plot(style='.', figsize=(20, 5), title="French Nuclear Energy Consumption (MW)")
'''wind'''
winddata = data[['hour', 'wind']]
winddata.dropna(inplace = True)
winddata.set_index('hour', inplace=True)
winddata = winddata.sort_values(by='hour', ascending=True)
winddata.plot(style='.', figsize=(20, 5), title="French Wind Energy Consumption (MW)")
'''solar'''
solardata = data[['hour', 'solar']]
solardata.dropna(inplace = True)
solardata.set_index('hour', inplace=True)
solardata = solardata.sort_values(by='hour', ascending=True)
solardata.plot(style='.', figsize=(20, 5), title="French Solar Energy Consumption (MW)")
'''hydraulic'''
hydraulicdata = data[['hour', 'hydraulic']]
hydraulicdata.dropna(inplace = True)
hydraulicdata.set_index('hour', inplace=True)
hydraulicdata = hydraulicdata.sort_values(by='hour', ascending=True)
hydraulicdata.plot(style='.', figsize=(20, 5), title="French Hydraulic Energy Consumption (MW)")
