from qgis.core import QgsProject

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
query = "SELECT * FROM \"My Layer\" WHERE \"population\" > 10000"

# Create a new layer based on the SQL query
result_layer = QgsVectorLayer(query, "Filtered Layer", "virtual")
if result_layer.isValid():
    QgsProject.instance().addMapLayer(result_layer)
    print("SQL query applied, and filtered layer added to the project.")
else:
    print("Failed to create filtered layer.")
