from qgis.core import QgsProject, QgsVectorFileWriter

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
output_path = "selected_features.csv"

# Export selected features to CSV
error = QgsVectorFileWriter.writeAsVectorFormat(layer, output_path, "UTF-8", layer.crs(), "CSV",
                                                layer.selectedFeatures())
if error[0] == QgsVectorFileWriter.NoError:
    print("Selected features exported successfully to CSV!")
else:
    print("Error:", error[1])
