from osgeo import ogr
from collections import Counter

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
datasource = ogr.Open(layer.dataProvider().dataSourceUri())
layer_gdal = datasource.GetLayer()

attribute_counts = Counter()

for feature in layer_gdal:
    attribute_counts[feature.GetField('category')] += 1  # Assuming 'category' is the attribute of interest

# Print summary report
print("Summary Report:")
for category, count in attribute_counts.items():
    print(f"{category}: {count} features")
