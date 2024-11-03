from qgis.core import QgsProject

layer = QgsProject.instance().mapLayersByName("My Layer")[0]

for feature in layer.getFeatures():
    area = feature.geometry().area()
    length = feature.geometry().length()
    print(f"Feature ID: {feature.id()}, Area: {area}, Length: {length}")
