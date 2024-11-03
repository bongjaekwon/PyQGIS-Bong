from qgis.core import QgsProject
import processing

layer = QgsProject.instance().mapLayersByName("Point Layer")[0]

# Create heatmap with variable radius
params = {
    'INPUT': layer,
    'RADIUS': '"radius_attribute"',  # Assuming there's an attribute defining radius
    'OUTPUT': 'memory:heatmap'
}

heatmap_layer = processing.run("native:heatmap", params)['OUTPUT']
QgsProject.instance().addMapLayer(heatmap_layer)

print("Heatmap with variable radius created and added to the project.")
