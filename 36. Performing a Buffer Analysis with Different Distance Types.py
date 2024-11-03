from qgis.core import QgsProject
import processing

layer = QgsProject.instance().mapLayersByName("Point Layer")[0]

# Create fixed distance buffer
fixed_buffer_params = {
    'INPUT': layer,
    'DISTANCE': 100,  # Fixed buffer distance
    'OUTPUT': 'memory:fixed_buffer'
}
fixed_buffer_layer = processing.run("native:buffer", fixed_buffer_params)['OUTPUT']

# Create variable distance buffer based on an attribute
variable_buffer_params = {
    'INPUT': layer,
    'DISTANCE': '"buffer_distance"',  # Assuming there's a field named 'buffer_distance'
    'OUTPUT': 'memory:variable_buffer'
}
variable_buffer_layer = processing.run("native:buffer", variable_buffer_params)['OUTPUT']

# Add both layers to the project
QgsProject.instance().addMapLayer(fixed_buffer_layer)
QgsProject.instance().addMapLayer(variable_buffer_layer)

print("Fixed and variable distance buffers created and added to the project.")
