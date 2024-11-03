from qgis.core import QgsProject
from qgis import processing

# Define layers
input_layer = QgsProject.instance().mapLayersByName("Input Layer")[0]
clip_layer = QgsProject.instance().mapLayersByName("Clip Layer")[0]

# Create buffer
buffer_params = {
    'INPUT': input_layer,
    'DISTANCE': 500,  # Buffer distance in the same units as the layer
    'OUTPUT': 'memory:buffer'
}
buffer_layer = processing.run("native:buffer", buffer_params)['OUTPUT']

# Clip the layer using the buffer
clip_params = {
    'INPUT': clip_layer,
    'OVERLAY': buffer_layer,
    'OUTPUT': 'memory:clipped'
}
clipped_layer = processing.run("native:clip", clip_params)['OUTPUT']

# Add layers to the project
QgsProject.instance().addMapLayer(buffer_layer)
QgsProject.instance().addMapLayer(clipped_layer)

print("Buffer created and Clip operation performed. Layers added to the project.")
