from osgeo import gdal, ogr

point_layer = QgsProject.instance().mapLayersByName("Point Layer")[0]
output_file = "/path/to/interpolated_raster.tif"

# Use GDAL to create an interpolated raster from points
gdal.UseExceptions()
gdal.Grid(output_file, point_layer.dataProvider().dataSourceUri(), algorithm="linear")

print("Values interpolated across a raster surface and saved to output file.")
