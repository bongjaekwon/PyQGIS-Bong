from qgis.core import QgsProject, QgsProcessingFeatureSourceDefinition
from qgis import processing

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
buffer_distance = 100  # Buffer distance

params = {
    'INPUT': QgsProcessingFeatureSourceDefinition(layer.id(), selectedFeatures=True),
    'DISTANCE': buffer_distance,
    'OUTPUT': 'memory:'
}

buffer_layer = processing.run("native:buffer", params)['OUTPUT']
QgsProject.instance().addMapLayer(buffer_layer)
print("Buffer created!")
