from dash import html
import folium

# Variables

RPI_coor = [42.73, -73.6775]
my_map = folium.Map(location=RPI_coor, zoom_start=18,
                    min_lat= 42.72558,
                    min_lon= -73.68990,
                    min_zoom= 15,
                    max_lat= 42.73984,
                    max_lon= -73.66338,
                    max_zoom= 18,
                    max_bounds= True)
my_map.save('my_map.html')

# Layout

layout = html.Iframe(id='map', srcDoc=open('my_map.html','r').read(), width='100%', height='600')