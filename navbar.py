'''This module defines the navigation bar component'''
from datetime import datetime
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc

layout = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row(
                        [
                            # Title
                            dbc.Col(
                                html.Div([html.H1("RPI MapApp", style= {"color": "white"})]),
                                width={"size": 3, "order": 1}
                            ),
                            # Display current time or the time set by user
                            dbc.Col(
                                html.Div([
                                    html.H6("Current Time: ", style = {"color": "white"}),
                                    html.P(id = 'time', style = {"color": "white"})
                                ]),
                                width={"size": 3, "order": 2}
                            ),
                            # Drop down menu to change view
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
                            html.P(id="view", className="mt-3", style={"display":"none"}),
                            # Change time functionality
                            dbc.Col(
                                dbc.DropdownMenu(
                                    [
                                    dcc.Input(
                                        id="hour_input",
                                        placeholder="Hour",
                                        value=datetime.now().hour,
                                        type="number",
                                        min=0,
                                        max=23
                                    ),
                                    dcc.Input(
                                        id="minute_input",
                                        placeholder="Minute",
                                        value=datetime.now().minute,
                                        type="number",
                                        min=0,
                                        max=59
                                    ),
                                    dbc.Button(
                                        'Set to inputted time', 
                                        id = 'update_button', n_clicks = 0
                                    ),
                                    dbc.Button(
                                        'Set to local time', 
                                        id = 'reset_button', n_clicks = 0
                                    )
                                   ],
                                    label = "Change Time", color = "#54585a"
                                ),
                                width={"size": 2, "order": 4}
                            ),
                        ],
                        # Align every text in each column in the center
                        align = "center"
                    )
                ]
            ),
            # Color of navigation bar is set to RPI color
            color = "#d6001c"
        )
