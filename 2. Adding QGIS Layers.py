from qgis.core import QgsProject, QgsVectorLayer

layer_path = "path/to/your/shapefile.shp"
layer_name = "My Layer"
layer = QgsVectorLayer(layer_path, layer_name, "ogr")

if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
    print(f"Layer '{layer_name}' added successfully!")
else:
    print("Failed to load layer!")
