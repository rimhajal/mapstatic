Interactive Map
================

Folium Package & Other Ressources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Folium package allows the manipulation of the map of the world using specific coordinates. 
With the coordinates of France being known, and a geo json file found on github with the coordinates of each commune, it was easy to join those in the json file with the commune names in the dataset at hand.
Below is the link for the json file used:
__ <https://www.data.gouv.fr/fr/datasets/r/fb3580f6-e875-408d-809a-ad22fc418581>


Concept
^^^^^^^

The map is based on the power consumption database and spreads out the data on the map given the commune.
The mean of consumption throughout the past 4 years is the value represented.

Choropleth
^^^^^^^^^^

Choropleth is the function that helped introduce the data to the Folium map. The below code was used:
.. code:: python
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

