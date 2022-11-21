import pandas as pd
import matplotlib.pyplot as mp

def consumption_rate(df_static):
    p1 = df_static.plot(x="Année", y=["Consommation annuelle totale de l'adresse (MWh)"], kind="bar", figsize=(9, 8))
    return p1