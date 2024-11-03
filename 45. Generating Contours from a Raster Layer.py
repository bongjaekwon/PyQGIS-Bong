from qgis.core import QgsProject
import processing

raster_layer = QgsProject.instance().mapLayersByName("Elevation Raster")[0]

params = {
    'INPUT': raster_layer,
    'BAND': 1,
    'INTERVAL': 10,  # Contour interval
    'OUTPUT': 'memory:contours'
}

contour_layer = processing.run("gdal:contour", params)['OUTPUT']
QgsProject.instance().addMapLayer(contour_layer)

print("Contour lines generated from the raster layer and added to the project.")
