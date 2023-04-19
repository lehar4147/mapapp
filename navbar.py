from dash import Dash
from dash import dcc
from dash import html
from datetime import datetime, date
import dash_bootstrap_components as dbc
from dash import dcc


# Functions


#def get_view():
    # not sure how to check which view has been selected
    #return current_view

"""
def table():
    table_header = [
        # Need to make dynamic
        html.Thead(html.Tr([html.Th("Current View: ")]))
    ]
    row1 = html.Tr([html.Td( dcc.Markdown(id = 'time'),
                             dcc.Interval(
                                id = 'interval-component',
                                interval = 1000,
                                n_intervals = 0
                             )
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
"""

layout = dbc.Navbar(
            dbc.Container(
                [
                    dbc.Row(
                        [
                            #dbc.Col(html.Img(src=RPI_MAP_APP_LOGO, height=""))
                            #Put in title for now
                            dbc.Col(
                                html.Div([html.H2("RPI Map App")]),
                                width={"size": 3, "order": 1}
                            ),
                            dbc.Col(
                                html.Div([
                                    html.H3("Current time: "),
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
                                     label="Change View"
                                ),
                                width={"size": 2, "order": 3}
                            ),
                            html.P(id="view", className="mt-3"),
                            dbc.Col(
                                dbc.DropdownMenu(
                                    [
                                    #  dcc.DatePickerSingle(
                                    #    id = 'date-picker',
                                    #    min_date_allowed=date(2023,3,28),
                                    #    max_date_allowed=date(2023,12,31),
                                    #    date=date.today()
                                    #),
                                    dcc.Input(id="hour_input", placeholder="Hour", value=datetime.now().hour, type="number", min=0,max=23),
                                    dcc.Input(id="minute_input", placeholder="Minute", value=datetime.now().minute, type="number", min=0, max=59),
                                    dbc.Button('Set to inputted time', id = 'update_button', n_clicks = 0),
                                    dbc.Button('Set to local time', id = 'reset_button', n_clicks = 0)
                                    #dbc.Button('Reset to original', id = 'reset_button', n_clicks = 0)
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
