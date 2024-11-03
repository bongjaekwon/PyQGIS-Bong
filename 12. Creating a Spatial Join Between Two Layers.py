from qgis.core import QgsProject, QgsProcessingFeatureSourceDefinition
from qgis import processing

# Input layers
layer_a = QgsProject.instance().mapLayersByName("Layer A")[0]
layer_b = QgsProject.instance().mapLayersByName("Layer B")[0]

# Spatial join parameters
params = {
    'INPUT': QgsProcessingFeatureSourceDefinition(layer_a.id(), selectedFeatures=False),
    'JOIN': QgsProcessingFeatureSourceDefinition(layer_b.id(), selectedFeatures=False),
    'PREDICATE': [0],  # Intersects
    'OUTPUT': 'memory:'
}

joined_layer = processing.run("native:joinattributesbylocation", params)['OUTPUT']
QgsProject.instance().addMapLayer(joined_layer)
print("Spatial join completed. New layer added.")
