from qgis.core import QgsProject, QgsFeature, QgsGeometry, QgsPointXY
from qgis.utils import edit

layer = QgsProject.instance().mapLayersByName("My Layer")[0]

with edit(layer):
    feature = QgsFeature()
    feature.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(1, 1)))
    feature.setAttributes(["New Feature", 5000])
    layer.addFeature(feature)
    print("New feature added!")
