import json
import folium
import overpy
from source_code.constants import *
import os


api = overpy.Overpass()

base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, 'data', 'route.geojson')

with open(file_path, encoding='utf-8') as geojson:
    data = json.load(geojson)
    geometry = data.get('geometry')

# coordinates in route file are stored in (latitude, longitude) order
# it must be swapped
coordinates = []
for lat, lon in geometry.get('coordinates'):
    coordinates.append((lon, lat))

# calculate the middle point when the map loads
middle_idx = len(coordinates) // 2
center = coordinates[middle_idx]

# create a map pointing at middle route with initial zoom of 6
my_map = folium.Map(location=center, zoom_start=6)
folium.PolyLine(coordinates).add_to(my_map)

# query every 500th point (from 4464) which is about 75 km for this route
for latitude, longitude in coordinates[::NTH_POINT]:
    result = api.query(
        QUERY_TEMPLATE.format(
            tag=TAG, radius=RADIUS, lat=latitude, lon=longitude
        )
    )

    # place found fuel stations as markers on the map
    for node in result.nodes:
        folium.map.Marker([node.lat, node.lon],
                          popup=node.tags.get('brand', TAG)).add_to(my_map)

my_map.save('map.html')
