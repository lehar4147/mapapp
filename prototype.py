#import plotly.express as px
import plotly.graph_objects as go

#import dash
from dash import Dash
from dash import dcc
from dash import html
#from dash.dependencies import Input, Output

import folium
import pandas as pd

RPI_coor = [42.73, -73.6775]
my_map = folium.Map(location=RPI_coor, zoom_start=24)
my_map.save('my_map.html')

import geocoder
g = geocoder.ip('me')

app = Dash(__name__)

# fig = go.Figure(go.Scattergeo())
# fig.update_geos(
#     visible=False, resolution=50, scope='north america',
#     showcountries=True, countrycolor="Black",
#     showsubunits=True, subunitcolor="Blue",
#     center=dict(lon=g.latlng[1],lat=g.latlng[0]),
#     lataxis_range=[g.latlng[0]-1,g.latlng[0]+1], lonaxis_range=[g.latlng[1]-1,g.latlng[1]+1]
# )
# fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

app.layout = html.Div([
    html.H1("Figure 1"),
    html.Iframe(id='map', srcDoc=open('my_map.html','r').read(), width='100%', height='600'),
])

if __name__ == '__main__':
    app.run_server(debug=True)