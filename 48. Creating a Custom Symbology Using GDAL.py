from osgeo import gdal

raster_layer = QgsProject.instance().mapLayersByName("Raster Layer")[0]
raster_file = raster_layer.dataProvider().dataSourceUri()

# Open the raster dataset
dataset = gdal.Open(raster_file, gdal.GA_Update)

# Create a color table for custom symbology
color_table = gdal.ColorTable()
color_table.SetColorEntry(0, (255, 0, 0))  # Red for low values
color_table.SetColorEntry(1, (0, 255, 0))  # Green for mid values
color_table.SetColorEntry(2, (0, 0, 255))  # Blue for high values

# Assign the color table to the raster band
band = dataset.GetRasterBand(1)
band.SetColorTable(color_table)

print("Custom symbology applied to raster layer.")
