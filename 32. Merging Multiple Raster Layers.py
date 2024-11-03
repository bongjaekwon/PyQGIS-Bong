from qgis.core import QgsProject
import processing

# Define input raster layers
input_rasters = [
    "path/to/raster1.tif",
    "path/to/raster2.tif",
    "path/to/raster3.tif"
]

params = {
    'INPUT': input_rasters,
    'OUTPUT': 'memory:merged_raster'
}

merged_raster = processing.run("gdal:merge", params)['OUTPUT']
QgsProject.instance().addMapLayer(merged_raster)

print("Rasters merged into one layer and added to the project.")
