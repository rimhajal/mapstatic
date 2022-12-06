import os

url_db = "https://data.enedis.fr/explore/dataset/consommation-annuelle-residentielle-par-adresse/download/?format=csv&timezone=Europe/Berlin&lang=fr&use_labels_for_header=true&csv_separator=%3B"
path_target = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "..", "data", "power_consumption.csv"
)