from dash import Dash
from dash import dcc
from dash import html
from datetime import datetime, date
import dash_bootstrap_components as dbc
from dash import dcc

from datetime import datetime

# Functions

def get_time():
    current_time = datetime.now().strftime("%H:%M")
    return current_time

#def get_view():
    # not sure how to check which view has been selected
    return current_view

def table():
    table_header = [
        # Need to make dynamic
        html.Thead(html.Tr([html.Th("Current View: ")]))
    ]
    row1 = html.Tr([html.Td(datetime.now().strftime("%Y-%m-%d %H:%M"), id = "time"
                    # "Current Time: ", id = "time"),
                    # dcc.Interval(
                    #     id = 'interval-component',
                    #     interval = 1000,
                    #     n_intervals = 0                       
                    )
                    ])
    table_body = [html.Tbody([row1])]

    table = dbc.Table(table_header + table_body, bordered=True)
    return table


layout = dbc.Navbar(
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
                                      dcc.DatePickerSingle(
                                        id = 'date-picker',
                                        min_date_allowed=date(2023,3,28),
                                        max_date_allowed=date(2023,12,31),
                                        date=date.today()
                                      ),
                                    #   dbc.DropdownMenu(
                                    #     [
                                    #         dbc.DropdownMenuItem("AM", id = "trigger_am"),
                                    #         dbc.DropdownMenuItem("PM", id = "trigger_pm")
                                    #     ],
                                    #     label = "AM/PM",
                                    #     direction = "right"
                                    #   ),
                                   dcc.Input(id="hour_input", placeholder="Hour", type="number", value = datetime.now().hour, min=0,max=23),
                                   dcc.Input(id="minute_input", placeholder="Minute", type="number", value = datetime.now().minute, min=0, max=59),
                                   #html.P(id = 'time'),

                                   #Button doesn't function for now
                                   #html.Button('Update time using custom time: ', id = 'update_button', n_clicks = 0)
                                   ],
                                    label = "Change time"
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
