# wards-plotter-ng
A Python-based tool for plotting Nigeria's LGA wards on static maps. 

This Python script allows users to visualize ward boundaries for any Local Government Area (LGA) in Nigeria using geospatial data. It loads a GeoJSON file containing ward polygons, prompts the user to select an LGA, and generates a map with ward labels and an OpenStreetMap basemap.

---
### How to Use
- Create Virtual environment called spatial (optional)
```bash
python -m venv spatial
```
- Open your terminal and activate your Python environment:
```bash
.\spatial\Scripts\Activate.ps1  # For PowerShell
spatial\Scripts\activate  # For CMD
source spatial/bin/activate #macOS/Linux
```
## Requirements

Make sure you have the following Python packages installed:

- `geopandas`
- `matplotlib`
- `contextily`
- `shapely`

### Install them using pip:

```bash
pip install geopandas matplotlib contextily shapely
```
### Run the script
```bash
python plotting_script.py
```
- Select an LGA from the printed list by entering its corresponding number.
- The script will generate a map showing ward boundaries and labels, and save it as a PNG file in the map2/ directory.

### Output
- A high-resolution PNG map of the selected LGA's wards.
- File is saved as:
`map2/<LGA_NAME>_wards_map.png`

## Features
- Interactive LGA selection via terminal
- Ward-level visualization with labels
- OpenStreetMap basemap integration
- Automatic CRS transformation for web mapping
- Clean and high-resolution map output

### Authord By: 
Ugwuozor Collins

## Project Structure
```pgsql
/plotting_scripts
│
├── app.py
├── requirements.txt
├── templates/
│   └── index.html
├── static/
│   └── maps/
└── .render.yaml (optional)

```

## Troubleshooting
- GeoJSON not found: Ensure ward_polygon.geojson is in the same directory as the script.
- Missing packages: Run pip install for any missing dependencies.
- Permission error in PowerShell: Run:
```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```




