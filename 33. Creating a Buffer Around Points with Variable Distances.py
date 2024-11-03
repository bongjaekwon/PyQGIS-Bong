from qgis.core import QgsProject
import processing

point_layer = QgsProject.instance().mapLayersByName("Point Layer")[0]

# Create buffer with variable distance
params = {
    'INPUT': point_layer,
    'DISTANCE': '"buffer_distance"',  # Assuming there's a field named 'buffer_distance'
    'OUTPUT': 'memory:variable_buffer'
}

variable_buffer = processing.run("native:buffer", params)['OUTPUT']
QgsProject.instance().addMapLayer(variable_buffer)

print("Variable distance buffers created and added to the project.")
