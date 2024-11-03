from qgis.core import QgsProject
import processing

raster_layer = QgsProject.instance().mapLayersByName("Raster Layer")[0]
polygon_layer = QgsProject.instance().mapLayersByName("Polygon Layer")[0]

params = {
    'INPUT': raster_layer,
    'MASK': polygon_layer,
    'OUTPUT': 'memory:clipped_raster'
}

clipped_raster = processing.run("gdal:cliprasterbymasklayer", params)['OUTPUT']
QgsProject.instance().addMapLayer(clipped_raster)

print("Raster clipped by polygon layer and added to the project.")
