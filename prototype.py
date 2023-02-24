#import pandas as pd
#import plotly.express as px
import plotly.graph_objects as go

#import dash
from dash import Dash
from dash import dcc
from dash import html
#from dash.dependencies import Input, Output

import geocoder
g = geocoder.ip('me')

app = Dash(__name__)

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=50, scope='north america',
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue",
    center=dict(lon=g.latlng[1],lat=g.latlng[0]),
    lataxis_range=[g.latlng[0]-1,g.latlng[0]+1], lonaxis_range=[g.latlng[1]-1,g.latlng[1]+1]
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

app.layout = html.Div([
    html.H1("Figure 1"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)