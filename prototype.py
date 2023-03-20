#import pandas as pd
#import plotly.express as px
import plotly.graph_objects as go

#import dash
from dash import Dash
from dash import dcc
from dash import html
#from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc

from datetime import datetime

import geocoder
g = geocoder.ip('me')

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

fig = go.Figure(go.Scattergeo())
fig.update_geos(
    visible=False, resolution=50, scope='north america',
    showcountries=True, countrycolor="Black",
    showsubunits=True, subunitcolor="Blue",
    center=dict(lon=g.latlng[1],lat=g.latlng[0]),
    lataxis_range=[g.latlng[0]-1,g.latlng[0]+1], lonaxis_range=[g.latlng[1]-1,g.latlng[1]+1]
)
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

#RPI_MAP_APP_LOGO = "....png"
def get_time():
    current_time = datetime.now().strftime("%H:%M")
    return current_time
    

def table():
    table_header = [
        # Need to make dynamic
        html.Thead(html.Tr([html.Th("Current View: Student")]))
    ]
    row1 = html.Tr([html.Td("Current Time: " + get_time())])
    table_body = [html.Tbody([row1])]

    table = dbc.Table(table_header + table_body, bordered=True)
    return table


app.layout = html.Div([
    html.Div(    
        dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row(
                        [
                            #dbc.Col(html.Img(src=RPI_MAP_APP_LOGO, height=""))
                            #Put in title for now
                            dbc.Col(
                                html.Div("RPI Map App"),
                                width={"size": 3, "order": 1}
                            ),
                            dbc.Col(
                                html.Div(table()),
                                width={"size": 3, "order": 2}
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "Change View", color = "primary"
                                ),
                                width={"size": 2, "order": 3}
                            ),
                            dbc.Col(
                                dbc.DropdownMenu(
                                    [dbc.DropdownMenuItem("Student"),dbc.DropdownMenuItem("Faculty"),
                                     dbc.DropdownMenuItem("Staff"),dbc.DropdownMenuItem("Guest")],
                                     label="Change View"
                                ),
                                width={"size": 2, "order": 4}
                            ),
                            dbc.Col(
                                dbc.Button(
                                    "Report Building Error", color = "primary"
                                ),
                                width={"size": 2, "order": 5}
                            ),
                        ],
                        align = "center"
                    )
                ]
            ),
            color = "primary"
        )
    ),
    html.Div(
        className = "map-view",
        children = [
            dcc.Graph(figure=fig)
        ]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)