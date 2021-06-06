#!/usr/bin/env python

import sys
print(sys.path)
#sys.path.append('/users/webhome/bowley/volunteering/veterans_memorial/VeteransMemorialHospital/mapping/venv/Lib/site-packages')
sys.path.append('./venv/Lib/site-packages')
print(sys.path)
#import venv/Lib/site-packages/folium/__init__.py

import folium
from folium.plugins import MarkerCluster

print(sys.path)

coords_ns = [45.24664938443739, -63.24613206184815]
map = folium.Map(location=coords_ns, zoom_start=8)
map.save('ns_map.html')
