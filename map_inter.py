#%%
import pandas as pd
import os
import pooch
import geopandas as gpd
import folium

url_db = "https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_target = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data", "power_consumption.csv"
)


path, fname = os.path.split(path_target)
pooch.retrieve(url_db, path=path, fname=fname, known_hash=None)

df_static = pd.read_csv(
    path_target,
    low_memory=False,
    sep=";",
)

url2 = "https://www.data.gouv.fr/fr/datasets/r/fb3580f6-e875-408d-809a-ad22fc418581"
#json file with the coordinates of each commune in France imported as dataframe

path_target2 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data", "geo_data.json"
)

path, fname = os.path.split(path_target2)
pooch.retrieve(url2, path=path, fname=fname, known_hash=None)

geo_json_data = gpd.read_file(
        path_target2,
        engine="pyogrio"
)

#json file with the coordinates of each commune in France imported as dataframe
#capitalized everything because it is case sensitive 
geo_json_data['libgeo'] = geo_json_data['libgeo'].str.upper()
    
commune_avg = df_static.groupby('Nom de la commune', as_index=False)['Consommation annuelle moyenne de la commune (MWh)'].mean()
commune_avg['Nom de la commune'] = commune_avg['Nom de la commune'].str.upper()
    
#creating the dataframe that only contains the communes in both dataframes with their coordinates and consumption rates
geo_json_data=geo_json_data.loc[:,('libgeo','geometry')]
df_final = geo_json_data.merge(commune_avg, left_on='libgeo', right_on='Nom de la commune',how='outer')
df_final = df_final.dropna()

#adding our data to the map
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
    
style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}

highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}
    
#adding our interactive features
folium.features.GeoJson(
    data=df_final,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function, 
    tooltip=folium.features.GeoJsonTooltip(
        fields=['Nom de la commune','Consommation annuelle moyenne de la commune (MWh)'],
        aliases=['Neighborhood: ','Resident foreign population in %: '],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),
        localize=True,
        sticky=True,
        labels=True,
    )
).add_to(mymap)
folium.LayerControl().add_to(mymap)

mymap.save("mymap.html")

