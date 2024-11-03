from qgis.core import QgsProject
import processing

# Define input shapefiles
input_layers = [
    "path/to/shapefile1.shp",
    "path/to/shapefile2.shp",
    "path/to/shapefile3.shp"
]

params = {
    'INPUT': input_layers,
    'OUTPUT': 'memory:merged_layer'
}

merged_layer = processing.run("native:mergevectorlayers", params)['OUTPUT']
QgsProject.instance().addMapLayer(merged_layer)

print("Shapefiles merged into one layer and added to the project.")
