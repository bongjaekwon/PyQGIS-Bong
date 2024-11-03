from qgis.core import QgsProject

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
layer.selectByExpression('"population" < 1000')
selected_features = layer.selectedFeatures()

print("Selected Features:")
for feature in selected_features:
    print(f"ID: {feature.id()}, Name: {feature['name']}")
