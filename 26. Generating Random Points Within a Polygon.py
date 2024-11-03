from qgis.core import QgsProject, QgsVectorLayer
import processing

polygon_layer = QgsProject.instance().mapLayersByName("Polygon Layer")[0]

# Define parameters for random point generation
params = {
    'INPUT': polygon_layer,
    'POINTS': 100,  # Number of random points
    'OUTPUT': 'memory:random_points'
}

random_points_layer = processing.run("native:randompointsinpolygon", params)['OUTPUT']
QgsProject.instance().addMapLayer(random_points_layer)

print("Random points generated within the polygon and added to the project.")
