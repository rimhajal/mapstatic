import pandas as pd
import numpy as np


def consumption_rate(df_static, log_scale=True):
    db = df_static.groupby(["departement"]).size()
    if log_scale:
        db = np.log(db)
    return db