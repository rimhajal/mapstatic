import os
import pandas as pd
import pooch
from visualization.dataset import url_db,path_target

class load_dataset:
    def __init__(self, url=url_db, target_name=path_target):
        path, fname = os.path.split(path_target)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        df_static = pd.read_csv(
            path_target,
            sep=";",
        )
        return df_static

