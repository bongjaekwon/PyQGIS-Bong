from osgeo import ogr
from qgis.core import QgsProject

layer = QgsProject.instance().mapLayersByName("Polygon Layer")[0]
vector_file = layer.dataProvider().dataSourceUri()

# Open the layer with GDAL
datasource = ogr.Open(vector_file)
layer_gdal = datasource.GetLayer()

# Adding fields for area and perimeter
layer_gdal.CreateField(ogr.FieldDefn('area', ogr.OFTReal))
layer_gdal.CreateField(ogr.FieldDefn('perimeter', ogr.OFTReal))

for feature in layer_gdal:
    geom = feature.GetGeometryRef()
    area = geom.GetArea()
    perimeter = geom.Length()
    feature.SetField('area', area)
    feature.SetField('perimeter', perimeter)
    layer_gdal.SetFeature(feature)

print("Area and perimeter calculated and added as new attributes.")
