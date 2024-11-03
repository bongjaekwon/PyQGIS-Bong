from osgeo import ogr

layer_a = QgsProject.instance().mapLayersByName("Layer A")[0]
layer_b = QgsProject.instance().mapLayersByName("Layer B")[0]

# Open layers with GDAL
a_ds = ogr.Open(layer_a.dataProvider().dataSourceUri())
b_ds = ogr.Open(layer_b.dataProvider().dataSourceUri())
output_file = "/path/to/spatial_join_output.shp"

# Use GDAL to perform spatial join
gdal.UseExceptions()
gdal.SpatialJoin(a_ds, b_ds, output_file)

print("Spatial join performed and saved to output file.")
