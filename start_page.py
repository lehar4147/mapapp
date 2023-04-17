from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import map
import navbar

from dash.dependencies import Output, Input, State
import datetime
# App Initialization

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

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

@app.callback(
    Output('time','children'),
    Output('updated-time','value'),
    [
        Input('interval-component', 'n_intervals'),
        Input('date-picker','date'),
        Input('hour_input','value'),
        Input('minute_input','value'),
        #Input('update_button','n_clicks')
    ],
    State('updated-time','value')
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
    return f'{current_time_str}', current_time_str

@app.callback(
    #'updated-map-status, some_other_callback will be used to update the map
    Output('updated-map-status','children'),
    Input('updated-time','value')
)
def some_other_callback(updated_time_value):
    # do something with updated_time_value
    return


# Server
if __name__ == '__main__':
    app.run_server(debug=True)
