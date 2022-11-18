import pandas as pd
import numpy as np


def consumption_rate(df_static, log_scale=True):
    cons_commune = df_static.groupby(["Consommation annuelle moyenne de la commune (MWh)"]).size()
    if log_scale:
        cons_commune = np.log(cons_commune)
    return cons_commune