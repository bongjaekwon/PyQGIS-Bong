from qgis.core import QgsProject
from qgis.utils import edit

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
unique_ids = set()
features_to_delete = []

# Identify duplicates
for feature in layer.getFeatures():
    if feature['unique_attribute'] in unique_ids:  # Assuming 'unique_attribute' is the key for duplicates
        features_to_delete.append(feature.id())
    else:
        unique_ids.add(feature['unique_attribute'])

# Remove duplicates
with edit(layer):
    layer.deleteFeatures(features_to_delete)

print(f"Removed {len(features_to_delete)} duplicate features.")
