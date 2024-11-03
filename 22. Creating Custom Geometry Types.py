from qgis.core import QgsProject, QgsFeature, QgsGeometry, QgsPointXY
from qgis.utils import edit

layer = QgsProject.instance().mapLayersByName("My Layer")[0]

with edit(layer):
    # Create a custom polygon
    points = [QgsPointXY(1, 1), QgsPointXY(2, 1), QgsPointXY(2, 2), QgsPointXY(1, 2), QgsPointXY(1, 1)]
    polygon = QgsGeometry.fromPolygonXY([points])
    
    feature = QgsFeature()
    feature.setGeometry(polygon)
    feature.setAttributes(["Custom Polygon"])
    layer.addFeature(feature)

print("Custom geometry added to the layer.")
