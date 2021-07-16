#!/usr/bin/env python

import sys
sys.path.append('./venv/Lib/site-packages')

#mapping imports
import folium
from folium.plugins import MarkerCluster

#source code is public but the database password must be kept secret sorry.
sys.path.append('../../databaseSecret')
from database import config

#reading from mysql server thats hosted on the dal servers
import mysql.connector
connection = mysql.connector.connect(**config)

cursor = connection.cursor()
query = ("SELECT * FROM VetMSingleTable")
cursor.execute(query)
result = cursor.fetchall()
for row in result:
    print(row)

#connection = pyodbc.connect('Driver={};'

coords_ns = [45.24664938443739, -63.24613206184815]
map = folium.Map(location=coords_ns, zoom_start=8)

latitude = 45.24
longitude = -63.246

tuple = (latitude, longitude)
tuple2 = (45.30, -63.25)

points = [tuple, tuple2]

folium.PolyLine(points).add_to(map)



map.save('ns_map.html')


