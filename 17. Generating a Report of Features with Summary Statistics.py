from qgis.core import QgsProject

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
total_features = layer.featureCount()
total_population = 0

for feature in layer.getFeatures():
    total_population += feature['population']

average_population = total_population / total_features if total_features > 0 else 0

# Generate report
report = f"Total Features: {total_features}\nTotal Population: {total_population}\nAverage Population: {average_population}\n"
print(report)
