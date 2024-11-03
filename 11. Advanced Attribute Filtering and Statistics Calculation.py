from qgis.core import QgsProject, QgsFeatureRequest

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
expression = '"population" > 10000'
request = QgsFeatureRequest().setFilterExpression(expression)

total_population = 0
count = 0

print("Features with population > 10000:")
for feature in layer.getFeatures(request):
    print(f"ID: {feature.id()}, Name: {feature['name']}, Population: {feature['population']}")
    total_population += feature['population']
    count += 1

if count > 0:
    average_population = total_population / count
    print(f"Average Population of filtered features: {average_population}")
else:
    print("No features found.")
