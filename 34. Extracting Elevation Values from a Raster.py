from qgis.core import QgsProject
import processing

point_layer = QgsProject.instance().mapLayersByName("Point Layer")[0]
raster_layer = QgsProject.instance().mapLayersByName("Elevation Raster")[0]

params = {
    'POINTS': point_layer,
    'RASTERCOPY': raster_layer,
    'OUTPUT': 'memory:elevation_extraction'
}

extracted_values_layer = processing.run("native:extractvaluesfromlayer", params)['OUTPUT']
QgsProject.instance().addMapLayer(extracted_values_layer)

print("Elevation values extracted and added to the project.")
