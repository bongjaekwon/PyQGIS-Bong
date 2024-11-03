from qgis.core import QgsProject, QgsFeature, QgsGeometry
from qgis.utils import edit

input_layer = QgsProject.instance().mapLayersByName("My Layer")[0]
centroid_layer = QgsVectorLayer("Point?crs=EPSG:4326", "Centroids", "memory")
centroid_layer_data = centroid_layer.dataProvider()
centroid_layer.startEditing()

for feature in input_layer.getFeatures():
    centroid_geom = feature.geometry().centroid()
    centroid_feature = QgsFeature()
    centroid_feature.setGeometry(centroid_geom)
    centroid_layer_data.addFeatures([centroid_feature])

centroid_layer.commitChanges()
QgsProject.instance().addMapLayer(centroid_layer)

print("Centroids calculated and added to a new layer.")
