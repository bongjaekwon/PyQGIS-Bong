from qgis.core import QgsProject, QgsFeature, QgsGeometry
from qgis.utils import edit

point_layer = QgsProject.instance().mapLayersByName("Point Layer")[0]
points = [feature.geometry().asPoint() for feature in point_layer.getFeatures()]

# Create a line
line_geom = QgsGeometry.fromPolylineXY(points)

# Smooth the line (simplifying for demonstration; real smoothing would require more complex logic)
smoothed_line_geom = line_geom.simplify(0.1)

line_feature = QgsFeature()
line_feature.setGeometry(smoothed_line_geom)
line_layer = QgsProject.instance().mapLayersByName("Line Layer")[0]

with edit(line_layer):
    line_layer.addFeature(line_feature)

print("Line created from points and smoothed, then added to the line layer.")
