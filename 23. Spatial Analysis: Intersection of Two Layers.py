from qgis.core import QgsProject
import processing

layer_a = QgsProject.instance().mapLayersByName("Layer A")[0]
layer_b = QgsProject.instance().mapLayersByName("Layer B")[0]

# Intersection parameters
params = {
    'INPUT': layer_a,
    'OVERLAY': layer_b,
    'OUTPUT': 'memory:intersected_layer'
}

intersected_layer = processing.run("native:intersection", params)['OUTPUT']
QgsProject.instance().addMapLayer(intersected_layer)

print("Intersection calculated and added to the project.")
