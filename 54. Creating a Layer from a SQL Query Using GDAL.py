from osgeo import ogr

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
query = "SELECT * FROM \"My Layer\" WHERE \"population\" > 10000"

# Open the layer with GDAL
datasource = ogr.Open(layer.dataProvider().dataSourceUri())
layer_gdal = datasource.GetLayer()

# Execute SQL query
result_layer = datasource.ExecuteSQL(query)

# Create new shapefile for results
output_file = "/path/to/query_results.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")
output_ds = driver.CreateDataSource(output_file)

# Copy features to new layer
output_layer = output_ds.CreateLayer("Query Results", geom_type=layer_gdal.GetGeomType())
for feature in result_layer:
    output_layer.CreateFeature(feature)

print("SQL query results saved to output file.")
