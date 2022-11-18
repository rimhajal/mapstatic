import os
import pandas as pd
import pooch

url_db = "https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_target = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data", "power_consumption.csv"
)

class load_dataset:
    def __init__(self, url=url_db, target_name=path_target):
        path, fname = os.path.split()
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df():
        df_static = pd.read_csv(
            path_target,
            sep=",",
        )
        return df_static