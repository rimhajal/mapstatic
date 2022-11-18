import pygal_maps_fr
import pygal

def map_creation(cons_commune):
    fr_chart = pygal.maps.fr.Departments(human_readable=True)
    fr_chart.title = "Yearly Power Consumption Average by Region in France"

    fr_chart.add("Consumption", cons_commune.to_dict())

    fr_chart.render_in_browser()

