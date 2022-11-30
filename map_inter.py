import visualization

data = visualization.load_dataset().save_as_df()
geo_json_data=visualization.load_geojsondata().save_as_df2()
mymap=visualization.map_creation(data,geo_json_data)