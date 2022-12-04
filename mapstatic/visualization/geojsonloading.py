#%%
import os
import pandas as pd
import pooch
import geopandas as gpd

url2 = "https://www.data.gouv.fr/fr/datasets/r/fb3580f6-e875-408d-809a-ad22fc418581"
#json file with the coordinates of each commune in France imported as dataframe

path_target2 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data", "geo_data.json"
)

class load_geojsondata:
    def __init__(self, url=url2, target_name=path_target2):
        path, fname = os.path.split(path_target2)
        pooch.retrieve(url, path=path, fname=fname, known_hash=None)

    @staticmethod
    def save_as_df2():
        geo_json_data = gpd.read_file(
            path_target2,
        )
        return geo_json_data
# %%
