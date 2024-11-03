from qgis.core import QgsProject, QgsProcessing
import processing

layer = QgsProject.instance().mapLayersByName("Point Layer")[0]

# Create heatmap parameters
params = {
    'INPUT': layer,
    'RADIUS': 100,  # Radius for heatmap calculation
    'OUTPUT': 'memory:heatmap'
}

heatmap_layer = processing.run("native:heatmap", params)['OUTPUT']
QgsProject.instance().addMapLayer(heatmap_layer)

print("Heatmap created from point data and added to the project.")
