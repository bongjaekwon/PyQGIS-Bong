from qgis.core import QgsProject, QgsFeature, QgsGeometry
from qgis.utils import edit

point_layer = QgsProject.instance().mapLayersByName("Point Layer")[0]

# Create a line from selected points
points = []
for feature in point_layer.selectedFeatures():
    points.append(feature.geometry().asPoint())

line_geom = QgsGeometry.fromPolylineXY(points)

# Create a new line feature
line_feature = QgsFeature()
line_feature.setGeometry(line_geom)
line_layer = QgsProject.instance().mapLayersByName("Line Layer")[0]

with edit(line_layer):
    line_layer.addFeature(line_feature)

print("Line created from selected points and added to the line layer.")
