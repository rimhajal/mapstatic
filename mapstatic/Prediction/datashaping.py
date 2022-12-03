#importing modules
import pandas as pd
import datadownloading

#importing the dataframe from python file datadownloading.py
dataframe = datadownloading.datadownloading.saving()
print(dataframe)

#creating all the energies's dataframes  

'''global consumption'''
def consumptiondata():
    consumptiondata = datadownloading.datadownloading.saving().copy(deep=True)
    consumptiondata = consumptiondata[['hour', 'consumption']]
    consumptiondata.dropna(inplace = True)
    consumptiondata.index = pd.to_datetime(consumptiondata.index)
    consumptiondata.set_index('hour', inplace=True)
    consumptiondata = consumptiondata.sort_values(by='hour', ascending=True)
    return(consumptiondata)

'''thermal'''
def thermaldata():
    thermaldata = datadownloading.datadownloading.saving().copy(deep=True)
    thermaldata = thermaldata[['hour', 'thermal']]
    thermaldata.dropna(inplace = True)
    thermaldata.index = pd.to_datetime(thermaldata.index)
    thermaldata.set_index('hour', inplace=True)
    thermaldata = thermaldata.sort_values(by='hour', ascending=True)
    return(thermaldata)

'''nuclear'''
def nucleardata():
    nucleardata = datadownloading.datadownloading.saving().copy(deep=True)
    nucleardata = nucleardata[['hour', 'nuclear']]
    nucleardata.dropna(inplace = True)
    nucleardata.index = pd.to_datetime(nucleardata.index)
    nucleardata.set_index('hour', inplace=True)
    nucleardata = nucleardata.sort_values(by='hour', ascending=True)
    return(nucleardata)

'''wind'''  
def winddata():
    winddata = datadownloading.datadownloading.saving().copy(deep=True)
    winddata = winddata[['hour', 'wind']]
    winddata.dropna(inplace = True)
    winddata.index = pd.to_datetime(winddata.index)
    winddata.set_index('hour', inplace=True)
    winddata = winddata.sort_values(by='hour', ascending=True)
    return(winddata)

'''solar'''
def solardata():
    solardata = datadownloading.datadownloading.saving().copy(deep=True) 
    solardata = solardata[['hour', 'solar']]
    solardata.dropna(inplace = True)
    solardata.index = pd.to_datetime(solardata.index)
    solardata.set_index('hour', inplace=True)
    solardata = solardata.sort_values(by='hour', ascending=True)
    return(solardata)

'''hydraulic'''
def hydraulicdata():  
    hydraulicdata = datadownloading.datadownloading.saving().copy(deep=True)
    hydraulicdata = hydraulicdata[['hour', 'hydraulic']]
    hydraulicdata.dropna(inplace = True)
    hydraulicdata.index = pd.to_datetime(hydraulicdata.index)
    hydraulicdata.set_index('hour', inplace=True)
    hydraulicdata = hydraulicdata.sort_values(by='hour', ascending=True)
    return(hydraulicdata)
    
 
#visualizing all the newly created energies's dataframes
consumptiondata().plot(figsize=(20, 5), title="French Global Energy Consumption on the 8th December", xlabel='Hour', ylabel='MW')
thermaldata().plot(figsize=(20, 5), title="French Thermal Energy Consumption on the 8th December", xlabel='Hour', ylabel='MW')
nucleardata().plot(figsize=(20, 5), title="French Nuclear Energy Consumption on the 8th December", xlabel='Hour', ylabel='MW')
winddata().plot(figsize=(20, 5), title="French Wind Energy Consumption on the 8th December", xlabel='Hour', ylabel='MW')
solardata().plot(figsize=(20, 5), title="French Solar Energy Consumption on the 8th December", xlabel='Hour', ylabel='MW')
hydraulicdata().plot(figsize=(20, 5), title="French Hydraulic Energy Consumption on the 8th December", xlabel='Hour', ylabel='MW')
   
