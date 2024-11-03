from qgis.core import QgsProject
import processing

source_layer = QgsProject.instance().mapLayersByName("Source Layer")[0]
target_layer = QgsProject.instance().mapLayersByName("Target Layer")[0]

# Finding nearest features
params = {
    'INPUT': source_layer,
    'NEIGHBOUR_COUNT': 1,  # Find the nearest feature
    'OUTPUT': 'memory:nearest_features'
}

nearest_layer = processing.run("native:nearestneighbour", params)['OUTPUT']
QgsProject.instance().addMapLayer(nearest_layer)

print("Nearest features calculated and added to the project.")
