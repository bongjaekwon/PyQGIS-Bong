from qgis.core import QgsProject, QgsVectorFileWriter

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
output_path = "selected_features.shp"

# Create a new shapefile from selected features
error = QgsVectorFileWriter.writeAsVectorFormat(layer, output_path, "UTF-8", layer.crs(), "ESRI Shapefile",
                                                layer.selectedFeatures())
if error[0] == QgsVectorFileWriter.NoError:
    print("Selected features exported successfully!")
else:
    print("Error:", error[1])
