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
    mymap.choropleth(
        geo_data=geo_json_data,
        name='Communes',
        data=commune_avg,
        columns=['Nom de la commune','Consommation annuelle moyenne de la commune (MWh)'],
        key_on="feature.properties.libgeo",
        fill_color='YlGnBu', nan_fill_color="#FF000000",
        fill_opacity=1,
        line_opacity=0.2,
        legend_name='Consommation moyenne des 4 dernières années (MWh)',
        smooth_factor=0
        )
    folium.LayerControl().add_to(mymap)
    return(mymap)
    


    



