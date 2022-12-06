import os

url2 = "https://www.data.gouv.fr/fr/datasets/r/fb3580f6-e875-408d-809a-ad22fc418581"
#json file with the coordinates of each commune in France imported as dataframe

path_target2 = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data", "geo_data.json"
)