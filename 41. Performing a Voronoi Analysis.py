from qgis.core import QgsProject
import processing

layer = QgsProject.instance().mapLayersByName("Point Layer")[0]

params = {
    'INPUT': layer,
    'OUTPUT': 'memory:voronoi'
}

voronoi_layer = processing.run("native:voronoipolygons", params)['OUTPUT']
QgsProject.instance().addMapLayer(voronoi_layer)

print("Voronoi diagram created and added to the project.")
