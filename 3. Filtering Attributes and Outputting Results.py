from qgis.core import QgsProject, QgsFeatureRequest

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
expression = '"population" > 10000'
request = QgsFeatureRequest().setFilterExpression(expression)

print("Features with population > 10000:")
for feature in layer.getFeatures(request):
    print(f"ID: {feature.id()}, Name: {feature['name']}")
