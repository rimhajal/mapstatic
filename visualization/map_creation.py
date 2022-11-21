import pandas as pd
import os
import geopandas as gpd
import folium
import branca.colormap as cm
from branca.colormap import linear
import json
import requests

def map_creation(df_static):
    url = "https://www.data.gouv.fr/fr/datasets/r/fb3580f6-e875-408d-809a-ad22fc418581"
    #json file with the coordinates of each commune in France
    geo_json_data = json.loads(requests.get(url).text)
    commune_avg = df_static.groupby('Nom de la commune', as_index=False)['Consommation annuelle moyenne de la commune (MWh)'].mean()
    mymap = folium.Map(location=[46.2276,2.2137], zoom_start=5.5)
    folium.GeoJson(geo_json_data,zoom_on_click=True).add_to(mymap)
    colormap = linear.YlGn_09.scale(
        commune_avg['Consommation annuelle moyenne de la commune (MWh)'].min(), commune_avg['Consommation annuelle moyenne de la commune (MWh)'].max()
    )



