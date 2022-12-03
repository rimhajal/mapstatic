import mapstatic.visualization as mv

data = mv.dataset.load_dataset().save_as_df()
geo_json_data=mv.geodata.load_geojsondata().save_as_df2()
mymap=mv.vis.map_creation(data,geo_json_data)