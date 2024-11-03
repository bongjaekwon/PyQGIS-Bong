from osgeo import gdal, ogr

# Set input point layer
point_layer = QgsProject.instance().mapLayersByName("Point Layer")[0]
point_file = point_layer.dataProvider().dataSourceUri()

# Create output polygon layer
output_file = "/path/to/thiessen_polygons.shp"
driver = ogr.GetDriverByName("ESRI Shapefile")

# Use GDAL to create Voronoi polygons
gdal.UseExceptions()
gdal.VoronoiPolygons(point_file, output_file)

print("Thiessen polygons generated and saved to output file.")
