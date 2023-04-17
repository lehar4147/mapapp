from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import map
import navbar
import dash

from dash.dependencies import Output, Input, State
import datetime
# App Initialization

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

#setted_time = None
# Layout

app.layout = html.Div([
    html.Div(
        navbar.layout
    ),
    html.Div(
        map.layout
    )
])

# @app.callback(
#     Output('time', 'children'),
#     [Input('interval-component', 'n_intervals')]
# )
# def update_time(n):
#     return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#def map_function(current_time_str)

@app.callback(
    Output('time','children'),
    #Output('updated-time','value'),
    [
        Input('interval-component', 'n_intervals'),
        Input('date-picker','date'),
        Input('hour_input','value'),
        Input('minute_input','value'),
        #Input('update_button','n_clicks')
    ],
    #State('updated-time','value')
)
def new_custom_time(n,date,hour,minute):  
    if hour is not None and minute is not None:
        current_time = datetime.datetime.strptime(f'{date} {hour}:{minute}', '%Y-%m-%d %H:%M')
    elif hour is None and minute is not None:
        current_time = datetime.datetime.strptime(f'{date} 00:{minute}', '%Y-%m-%d %H:%M')
    elif hour is not None and minute is None:
        current_time = datetime.datetime.strptime(f'{date} {hour}:00', '%Y-%m-%d %H:%M')
    else:
        current_time = datetime.datetime.now()
    current_time_str = current_time.strftime('%I:%M:%S %p')
    #global setted_time
    #setted_time = current_time_str

    #map_function(current_time_str)
    return f'{current_time_str}'#, current_time_str

'''
@app.callback(
    #'updated-map-status, some_other_callback will be used to update the map
    Output('updated-map-status','children'),
    Input('updated-time','value')
)
def some_other_callback(updated_time_value):
    # do something with updated_time_value
    print(updated_time_value)
    return
'''

@app.callback(
    Output("view", "children"),
    [
        Input("Student", "n_clicks"),
        Input("Faculty", "n_clicks"),
        Input("Staff", "n_clicks"),
        Input("Guest", "n_clicks"),
    ],
)

def change_view(student,faculty,staff,guest):
    ctx = dash.callback_context

    if (student is None and faculty is None and staff is None and guest is None) or not ctx.triggered:
        return ""

    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if button_id == "Student":
        map.reloadMap(1)
    if button_id == "Faculty":
        map.reloadMap(2)
    if button_id == "Staff":
        map.reloadMap(3)
    if button_id == "Guest":
        map.reloadMap(4)

    return button_id

# Server
if __name__ == '__main__':
    app.run_server(debug=True)
