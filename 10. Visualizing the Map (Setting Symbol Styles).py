from qgis.core import QgsProject
from PyQt5.QtGui import QColor

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
symbol = layer.renderer().symbol()
symbol.setColor(QColor("blue"))
symbol.setSize(3)
layer.triggerRepaint()
print("Symbol style updated!")
