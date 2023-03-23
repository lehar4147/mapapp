import plotly.graph_objects as go
from dash import Dash
from dash import html
import folium

RPI_coor = [42.73, -73.6775]
my_map = folium.Map(location=RPI_coor, zoom_start=24)
my_map.save('my_map.html')

import geocoder
g = geocoder.ip('me')

app = Dash(__name__)

app.layout = html.Div([
    html.Iframe(id='map', srcDoc=open('my_map.html','r').read(), width='100%', height='600'),
])

if __name__ == '__main__':
    app.run_server(debug=True)