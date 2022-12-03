from mapstatic.visualization import * 

data = load_dataset.save_as_df()
geo_json_data=load_geojsondata().save_as_df2()
mymap=map_creation(data,geo_json_data)