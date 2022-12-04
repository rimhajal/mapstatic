#%%
import folium
import geojsonloading
import dataloading

df_static = dataloading.load_dataset.save_as_df()
geo_json_data = geojsonloading.load_geojsondata.save_as_df2()

def map_creation(df_static,geo_json_data):
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
    
    #designing our interactive map
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
    return(mymap)
    


    



