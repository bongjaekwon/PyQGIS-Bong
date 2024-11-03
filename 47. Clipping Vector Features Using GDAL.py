from osgeo import gdal, ogr
import os

input_layer = QgsProject.instance().mapLayersByName("Input Layer")[0]
clip_layer = QgsProject.instance().mapLayersByName("Clip Layer")[0]

# Define file paths
input_file = input_layer.dataProvider().dataSourceUri()
clip_file = clip_layer.dataProvider().dataSourceUri()
output_file = "/path/to/clipped_output.shp"

# Run the clip operation using GDAL
gdal.UseExceptions()
gdal.VectorTranslate(output_file, input_file, cutlineDSName=clip_file, cropToCutline=True)

print("Vector features clipped and saved to output file.")
