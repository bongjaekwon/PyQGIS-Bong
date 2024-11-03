# QGIS Python Scripts

This repository contains a comprehensive collection of advanced Python scripts tailored for use with QGIS, one of the leading open-source Geographic Information System (GIS) applications. These scripts leverage both native QGIS functions and GDAL (Geospatial Data Abstraction Library) capabilities to facilitate a wide array of geospatial analyses and operations.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Scripts Overview](#scripts-overview)
3. [Usage Instructions](#usage-instructions)
4. [Author Information](#author-information)
5. [License](#license)

## Getting Started

To utilize these scripts, you need to have QGIS installed on your machine, preferably version 3.34.11 or later. Additionally, ensure that GDAL is set up correctly, as some scripts depend on it for advanced data processing capabilities.

### Prerequisites

- **QGIS**: Download and install from the [QGIS website](https://qgis.org).
- **GDAL**: Often included with QGIS installations, but can also be installed separately if needed.

Once you have QGIS installed, you can access the Python console from the main interface to run these scripts directly.

## Scripts Overview

This repository includes a variety of scripts organized into categories based on their functionality:

### 1. Environment Setup and Layer Management
- **1. Setting Up QGIS Environment.py**: Initializes the QGIS environment for scripting.
- **2. Adding QGIS Layers.py**: Adds layers to the current QGIS project.
- **21. Merging Multiple Shapefiles into One.py**: Combines multiple shapefiles into a single layer.
- **47. Clipping Vector Features Using GDAL.py**: Clips features from one vector layer using another's geometry.

### 2. Data Manipulation and Attribute Management
- **3. Filtering Attributes and Outputting Results.py**: Filters features based on attribute values and outputs results.
- **4. Adding Features.py**: Adds new features to a layer.
- **5. Calculating Geometric Properties (Area and Length).py**: Computes geometric properties for features.
- **6. Modifying Layer Attributes.py**: Changes attribute values of features in a layer.
- **11. Advanced Attribute Filtering and Statistics Calculation.py**: Performs advanced filtering and calculates statistics.
- **12. Creating a Spatial Join Between Two Layers.py**: Merges attributes based on spatial relationships.
- **30. Updating a Field Based on Calculated Values.py**: Updates a specific field based on calculations from other attributes.
- **38. Identifying and Removing Duplicates in a Layer.py**: Finds and removes duplicate features in a layer.

### 3. Geospatial Analysis
- **9. Spatial Analysis (Creating Buffers).py**: Creates buffer zones around features.
- **10. Visualizing the Map (Setting Symbol Styles).py**: Sets visual styles for map layers.
- **13. Batch Update of Attributes Based on Conditions.py**: Updates multiple attributes in a batch process based on defined conditions.
- **14. Geoprocessing: Buffer and Clip Operations.py**: Performs both buffer and clip operations on spatial data.
- **20. Finding Nearest Features.py**: Identifies the nearest features to a given feature.
- **23. Spatial Analysis: Intersection of Two Layers.py**: Analyzes the intersection of two spatial layers.
- **29. Performing Zonal Statistics.py**: Calculates statistics based on zonal data.
- **41. Performing a Voronoi Analysis.py**: Creates Voronoi polygons from point features.
- **42. Checking for Spatial Overlaps Between Two Layers.py**: Determines if features in two layers overlap spatially.

### 4. Raster Operations and Analysis
- **19. Performing a Raster Calculation.py**: Executes calculations on raster data.
- **31. Clipping a Raster by a Polygon.py**: Clips a raster layer using the geometry of a polygon.
- **32. Merging Multiple Raster Layers.py**: Combines several raster layers into one.
- **34. Extracting Elevation Values from a Raster.py**: Extracts elevation data from a raster file.
- **45. Generating Contours from a Raster Layer.py**: Creates contour lines from elevation data in a raster.

### 5. Visualization and Reporting
- **17. Generating a Report of Features with Summary Statistics.py**: Produces a report summarizing statistics of features.
- **18. Creating Heatmaps from Point Data.py**: Generates heatmaps based on point data distribution.
- **39. Creating a Heatmap with Variable Radius.py**: Produces heatmaps that adjust based on varying radius values.
- **40. Creating a Line from Multiple Points with Smoothing.py**: Generates smooth lines from a series of points.
- **44. Finding and Visualizing Outliers.py**: Identifies and visualizes outliers in the data.

### 6. Exporting Data
- **8. Exporting Layers (GeoJSON).py**: Exports selected layers to GeoJSON format.
- **15. Exporting Selected Features to a New Shapefile.py**: Exports specific features to a new shapefile.
- **37. Exporting Selected Features to CSV.py**: Saves selected features to a CSV file.
- **54. Creating a Layer from a SQL Query Using GDAL.py**: Executes a SQL query on a layer and creates a new layer from the results.

### 7. Random Data Generation and Custom Geometry
- **26. Generating Random Points Within a Polygon.py**: Creates random points inside a specified polygon.
- **27. Creating a Line from Points.py**: Generates a line from a given set of points.
- **28. Calculating Centroids of Features.py**: Computes centroids for features in a layer.
- **33. Creating a Buffer Around Points with Variable Distances.py**: Creates variable distance buffers around point features.
- **46. Calculating Area and Perimeter for Each Feature Using GDAL.py**: Computes area and perimeter for polygon features.

### 8. Advanced GDAL Operations
- **48. Creating a Custom Symbology Using GDAL.py**: Applies custom styling to raster layers.
- **49. Generating Thiessen Polygons Using GDAL.py**: Creates Thiessen polygons from a set of points.
- **50. Interpolating Values Across a Raster Using GDAL.py**: Interpolates values from point data to create a continuous raster.
- **52. Filtering Features Based on Attribute Values Using GDAL.py**: Filters features in a layer based on attribute criteria using GDAL.
- **53. Converting Points to Line Segments Using GDAL.py**: Converts point features into line segments.

### 9. Miscellaneous
- **24. Applying a Custom SQL Query to a Layer.py**: Executes a custom SQL query on a layer.
- **25. Automating Map Layout Creation.py**: Automates the process of creating a map layout in QGIS.

## Usage Instructions

To run a script, open QGIS and navigate to the Python console. Copy and paste the desired script into the console and execute it. Make sure to adjust any file paths or parameters as necessary to fit your specific datasets and requirements.

For example, if a script requires you to specify an input layer name or an output file path, ensure that these values correspond to the layers and paths relevant to your project.

## Author Information

Bongjae Kwon  
Civil and Environmental Engineering GIS/LBS Lab  
Seoul National University  
Email: [bongjae.kwon@snu.ac.kr](mailto:bongjae.kwon@snu.ac.kr)

Bongjae Kwon specializes in geospatial technologies and their applications in civil and environmental engineering. This repository reflects a commitment to providing practical tools for enhancing geospatial analysis and decision-making processes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details about usage and redistribution.
