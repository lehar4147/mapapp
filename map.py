import plotly.graph_objects as go
from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
from datetime import datetime
import folium

# Functions

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

# Variables

RPI_coor = [42.73, -73.6775]
my_map = folium.Map(location=RPI_coor, zoom_start=24)
my_map.save('my_map.html')

# App Initialization

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout

navbar = dbc.Navbar(
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
                                dbc.DropdownMenu(
                                    [dbc.DropdownMenuItem("Student"),dbc.DropdownMenuItem("Faculty"),
                                     dbc.DropdownMenuItem("Staff"),dbc.DropdownMenuItem("Guest")],
                                     label="Change View"
                                ),
                                width={"size": 2, "order": 3}
                            ),
                            dbc.Col(
                                dbc.DropdownMenu(
                                    [
                                      dbc.DropdownMenu(
                                        [
                                            dbc.DropdownMenuItem("Monday"),
                                            dbc.DropdownMenuItem("Tuesday"),
                                            dbc.DropdownMenuItem("Wednesday"),
                                            dbc.DropdownMenuItem("Thursday"),
                                            dbc.DropdownMenuItem("Friday"),
                                            dbc.DropdownMenuItem("Saturday"),
                                            dbc.DropdownMenuItem("Sunday"),
                                        ],
                                        label = "Day"
                                      ),
                                      dbc.Input(id="hour_input", placeholder="Hour", type="number",min=0,max=23),
                                      dbc.Input(id="minute_input", placeholder="Minute", type="number", min=0, max=59),
                                      dbc.DropdownMenu(
                                        [
                                            dbc.DropdownMenuItem("AM", id = "trigger_am"),
                                            dbc.DropdownMenuItem("PM", id = "trigger_pm")
                                        ],
                                        label = "AM/PM",
                                        direction = "up"
                                      ),
                                      html.P('Current time: ')
                                      # Need to make function to update time while input is given
                                    ],
                                    label = "Change Time"
                                ),
                                width={"size": 2, "order": 4},
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

app.layout = html.Div([
    html.Div(    
        navbar
    ),
    html.Div(
        className = "map-view",
        children = [
            html.Iframe(id='map', srcDoc=open('my_map.html','r').read(), width='100%', height='600')
        ]
    )
])

# Callbacks

# @app.callback(
#     Output("current_AM_PM","children"), [Input("trigger_am", "PM")]
# )

# def update_am_pm(clicked):
#     if (clicked == 'PM'){
#         return f'Output: {PM}'
#     }
#     return f'Output: {AM}'

# Server

if __name__ == '__main__':
    app.run_server(debug=True)