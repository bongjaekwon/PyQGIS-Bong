from qgis.core import QgsProject, QgsFeatureRequest
from collections import Counter

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
attribute_counts = Counter()

for feature in layer.getFeatures():
    attribute_counts[feature['category']] += 1  # Assuming 'category' is the attribute of interest

# Print counts
print("Counts by category:")
for category, count in attribute_counts.items():
    print(f"{category}: {count}")
