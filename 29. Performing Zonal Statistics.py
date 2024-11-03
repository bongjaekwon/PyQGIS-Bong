from qgis.core import QgsProject
import processing

polygon_layer = QgsProject.instance().mapLayersByName("Polygon Layer")[0]
raster_layer = QgsProject.instance().mapLayersByName("Raster Layer")[0]

params = {
    'INPUT': polygon_layer,
    'RASTER': raster_layer,
    'OUTPUT': 'memory:zonal_statistics'
}

zonal_stats_layer = processing.run("native:zonalstatistics", params)['OUTPUT']
QgsProject.instance().addMapLayer(zonal_stats_layer)

print("Zonal statistics calculated and added to the project.")
