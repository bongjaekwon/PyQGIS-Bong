from qgis.core import QgsProject
from qgis.utils import edit

layer = QgsProject.instance().mapLayersByName("My Layer")[0]

with edit(layer):
    for feature in layer.getFeatures():
        new_value = feature['population'] * 2  # Example calculation
        feature['new_field'] = new_value
        layer.updateFeature(feature)

print("Field updated based on calculations.")
