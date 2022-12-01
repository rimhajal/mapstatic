import mapstatic

data = mapstatic.load_dataset().save_as_df()
geo_json_data=mapstatic.load_geojsondata().save_as_df2()
mymap=mapstatic.map_creation(data,geo_json_data)