from dash import html
import folium

# Variables

RPI_coor = [42.73, -73.6775]
my_map = folium.Map(location=RPI_coor, zoom_start=24)
my_map.save('my_map.html')

# Layout

layout = html.Iframe(id='map', srcDoc=open('my_map.html','r').read(), width='100%', height='600')