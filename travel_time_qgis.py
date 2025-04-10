import openrouteservice
import json
from qgis.core import QgsVectorLayer, QgsProject

# Replace with your actual API key
client = openrouteservice.Client(key="5b3ce3597851110001cf6248639b38838b734dabaccb60bbc0c261aa")

start = (-10.8761395846085, 9.120508816411458)  # (lon, lat)
end = (-10.9490956705478, 9.196093811704191)

route = client.directions(
    coordinates=[start, end],
    profile='driving-car',
    format='geojson'
)

# Extract travel info
summary = route['features'][0]['properties']['summary']
distance_km = summary['distance'] / 1000
duration_min = summary['duration'] / 60

print(f"Distance: {distance_km:.2f} km")
print(f"Estimated travel time: {duration_min:.2f} minutes")

# Optional: Add route as a layer to QGIS
geojson = json.dumps(route)
layer = QgsVectorLayer(f"GeoJSON:{geojson}", "ORS Route", "ogr")
QgsProject.instance().addMapLayer(layer)
