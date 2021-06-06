#!/usr/bin/env python

import folium
from folium.plugins import MarkerCluster


coords_ns = [45.24664938443739, -63.24613206184815]
map = folium.Map(location=coords_ns, zoom_start=8)
map.save('ns_map.html')
