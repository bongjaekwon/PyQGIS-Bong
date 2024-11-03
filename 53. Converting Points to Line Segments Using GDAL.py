from osgeo import ogr

point_layer = QgsProject.instance().mapLayersByName("Point Layer")[0]
output_file = "/path/to/lines_from_points.shp"

# Open point layer with GDAL
ds = ogr.Open(point_layer.dataProvider().dataSourceUri())
layer_gdal = ds.GetLayer()

# Create new line layer
driver = ogr.GetDriverByName("ESRI Shapefile")
line_ds = driver.CreateDataSource(output_file)
line_layer = line_ds.CreateLayer("Line Layer", geom_type=ogr.wkbLineString)

points = []

for feature in layer_gdal:
    points.append(feature.GetGeometryRef().GetPoint(0))

# Create line geometry from points
line = ogr.Geometry(ogr.wkbLineString)
for point in points:
    line.AddPoint(point[0], point[1])

# Create new feature and add to line layer
line_feature = ogr.Feature(line_layer.GetLayerDefn())
line_feature.SetGeometry(line)
line_layer.CreateFeature(line_feature)

print("Points converted to line segments and saved to output file.")
