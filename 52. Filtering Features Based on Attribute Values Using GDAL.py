from osgeo import ogr

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
output_file = "/path/to/filtered_layer.shp"

# Open layer with GDAL
ds = ogr.Open(layer.dataProvider().dataSourceUri())
layer_gdal = ds.GetLayer()

# Create new layer for filtered results
driver = ogr.GetDriverByName("ESRI Shapefile")
filtered_ds = driver.CreateDataSource(output_file)
filtered_layer = filtered_ds.CreateLayer("Filtered Layer", geom_type=layer_gdal.GetGeomType())

# Filter and copy features
for feature in layer_gdal:
    if feature.GetField('status') == 'active':  # Example attribute filter
        filtered_layer.CreateFeature(feature)

print("Filtered features saved to output file.")
