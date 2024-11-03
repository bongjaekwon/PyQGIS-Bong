from qgis.core import QgsProject
from qgis.utils import edit

layer = QgsProject.instance().mapLayersByName("My Layer")[0]

with edit(layer):
    for feature in layer.getFeatures():
        if feature['population'] < 5000:
            feature['status'] = 'Underpopulated'
        elif feature['population'] < 20000:
            feature['status'] = 'Moderately Populated'
        else:
            feature['status'] = 'Well Populated'
        layer.updateFeature(feature)

print("Population status updated based on conditions.")
