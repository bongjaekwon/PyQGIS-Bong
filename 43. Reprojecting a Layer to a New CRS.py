from qgis.core import QgsProject, QgsCoordinateReferenceSystem
import processing

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
new_crs = QgsCoordinateReferenceSystem("EPSG:4326")  # Example: WGS 84

params = {
    'INPUT': layer,
    'TARGET_CRS': new_crs,
    'OUTPUT': 'memory:reprojected_layer'
}

reprojected_layer = processing.run("gdal:warpreproject", params)['OUTPUT']
QgsProject.instance().addMapLayer(reprojected_layer)

print("Layer reprojected to new CRS and added to the project.")
