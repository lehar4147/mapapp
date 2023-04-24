from dash import Dash
from dash import dcc
from dash import html
from datetime import datetime, date
import dash_bootstrap_components as dbc
from dash import dcc

layout = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row(
                        [
                            #dbc.Col(html.Img(src=RPI_MAP_APP_LOGO, height=""))
                            #Put in title for now
                            dbc.Col(
                                html.Div([html.H1("RPI MapApp")]),
                                width={"size": 3, "order": 1}
                            ),
                            dbc.Col(
                                html.Div([
                                    html.H6("Current Time: "),
                                    html.P(id = 'time')
                                ]),
                                width={"size": 3, "order": 2}
                            ),
                            dbc.Col(
                                dbc.DropdownMenu(
                                    [dbc.DropdownMenuItem("Student", id="Student"),
                                     dbc.DropdownMenuItem("Faculty", id="Faculty"),
                                     dbc.DropdownMenuItem("Staff", id="Staff"),
                                     dbc.DropdownMenuItem("Guest", id="Guest")],
                                     label="Change View", color = "#54585a"
                                ),
                                width={"size": 2, "order": 3}
                            ),
                            html.P(id="view", className="mt-3"),
                            dbc.Col(
                                dbc.DropdownMenu(
                                    [
                                    dcc.Input(id="hour_input", placeholder="Hour", value=datetime.now().hour, type="number", min=0,max=23),
                                    dcc.Input(id="minute_input", placeholder="Minute", value=datetime.now().minute, type="number", min=0, max=59),
                                    dbc.Button('Set to inputted time', id = 'update_button', n_clicks = 0),
                                    dbc.Button('Set to local time', id = 'reset_button', n_clicks = 0)
                                   ],
                                    label = "Change Time", color = "#54585a"
                                ),
                                width={"size": 2, "order": 4}
                            ),
                            #dbc.Col(
                                #dbc.Button(
                                    #"Report Building Error", color = "primary"
                               # ),
                               # width={"size": 2, "order": 5}
                           # ),
                        ],
                        align = "center"
                    )
                ]
            ),
            color = "#d6001c"
        )
