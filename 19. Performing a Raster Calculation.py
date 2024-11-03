from qgis.core import QgsProject
import processing

# Define raster layers
raster1 = QgsProject.instance().mapLayersByName("Raster Layer 1")[0]
raster2 = QgsProject.instance().mapLayersByName("Raster Layer 2")[0]

# Raster calculation parameters
params = {
    'EXPRESSION': '("Raster Layer 1@1" + "Raster Layer 2@1") / 2',  # Average of two rasters
    'OUTPUT': 'memory:raster_result'
}

result_raster = processing.run("gdal:warpreproject", params)['OUTPUT']
QgsProject.instance().addMapLayer(result_raster)

print("Raster calculation performed and result added to the project.")
