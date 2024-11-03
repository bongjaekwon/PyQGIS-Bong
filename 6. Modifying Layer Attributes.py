from qgis.core import QgsProject
from qgis.utils import edit

layer = QgsProject.instance().mapLayersByName("My Layer")[0]

with edit(layer):
    for feature in layer.getFeatures():
        feature['population'] += 1000  # Increase population
        layer.updateFeature(feature)
    print("Population updated!")
