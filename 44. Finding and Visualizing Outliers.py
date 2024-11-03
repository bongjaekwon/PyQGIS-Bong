from qgis.core import QgsProject
import numpy as np

layer = QgsProject.instance().mapLayersByName("My Layer")[0]
values = []

for feature in layer.getFeatures():
    values.append(feature['value'])  # Assuming 'value' is the attribute of interest

# Calculate mean and standard deviation
mean = np.mean(values)
std_dev = np.std(values)
threshold = 2  # Standard deviations

outliers = [feature.id() for feature in layer.getFeatures() if abs(feature['value'] - mean) > threshold * std_dev]

layer.select(outliers)
print(f"Identified {len(outliers)} outliers in the dataset.")
