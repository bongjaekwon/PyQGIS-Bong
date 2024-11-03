from qgis.core import QgsProject, QgsFeatureRequest

layer_a = QgsProject.instance().mapLayersByName("Polygon Layer A")[0]
layer_b = QgsProject.instance().mapLayersByName("Polygon Layer B")[0]

overlapping_features = []

for feature_a in layer_a.getFeatures():
    for feature_b in layer_b.getFeatures():
        if feature_a.geometry().overlaps(feature_b.geometry()):
            overlapping_features.append(feature_a.id())

layer_a.select(overlapping_features)
print(f"Found {len(overlapping_features)} overlapping features in Layer A.")
