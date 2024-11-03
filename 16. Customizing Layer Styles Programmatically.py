from qgis.core import QgsProject, QgsRendererCategory, QgsCategorizedSymbolRenderer
from PyQt5.QtGui import QColor

layer = QgsProject.instance().mapLayersByName("My Layer")[0]

# Define categories based on a specific attribute
categories = []
values = layer.uniqueValues("status")  # Assuming 'status' is an attribute

for value in values:
    color = QColor(0, 255, 0) if value == 'Well Populated' else QColor(255, 255, 0) if value == 'Moderately Populated' else QColor(255, 0, 0)
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(color)
    symbol.setWidth(2)
    categories.append(QgsRendererCategory(value, symbol, str(value)))

# Create renderer and set it to the layer
renderer = QgsCategorizedSymbolRenderer("status", categories)
layer.setRenderer(renderer)
layer.triggerRepaint()

print("Layer style customized based on status attribute.")
