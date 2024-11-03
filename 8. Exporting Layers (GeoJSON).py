from qgis.core import QgsProject, QgsVectorFileWriter

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
output_path = "output.geojson"

error = QgsVectorFileWriter.writeAsVectorFormat(layer, output_path, "UTF-8", layer.crs(), "GeoJSON")
if error[0] == QgsVectorFileWriter.NoError:
    print("Layer exported successfully!")
else:
    print("Error:", error[1])
