import os
import pandas as pd
import pooch
import geopandas as gpd
from visualization.geodata import url2,path_target2

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