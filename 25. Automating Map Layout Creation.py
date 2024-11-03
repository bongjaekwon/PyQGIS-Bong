from qgis.core import QgsProject
from qgis.core import QgsPrintLayout, QgsLayoutItemMap, QgsLayoutItemLabel
from qgis.PyQt.QtCore import QRectF

# Create a new layout
project = QgsProject.instance()
layout = QgsPrintLayout(project)
layout.initializeDefaults()
layout.setName("My Map Layout")
project.layoutManager().addLayout(layout)

# Add a map item
map_item = QgsLayoutItemMap(layout)
map_item.setRect(20, 20, 200, 150)
map_item.setLayers([QgsProject.instance().mapLayersByName("My Layer")[0]])
layout.addLayoutItem(map_item)

# Add a label
label = QgsLayoutItemLabel(layout)
label.setText("My Map Title")
label.setFont(QFont("Arial", 16))
label.adjustSizeToText()
layout.addLayoutItem(label)

print("Map layout created and items added.")
