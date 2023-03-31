from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import map
import navbar

from dash.dependencies import Output, Input
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
    [
        Input('date-picker','date'),
        Input('hour_input','value'),
        Input('minute_input','value'),
        #Input('update_button','n_clicks')
    ]
)
def new_custom_time(date,hour,minute):  
    if (hour is not None) and (minute is not None):
        if (0 <= minute < 10):
            return f'{date}, {hour}:0{minute}'
        else:
            return f'{date}, {hour}:{minute}'
    else:
        if (hour is None) and (minute is not None):
            return f'{date}, 00:{minute}'
        elif (hour is not None) and (minute is None):
            return f'{date}, {hour}:00'
        else:
            return f'{date}, 00:00'



# Server
map.reloadMap()
if __name__ == '__main__':
    app.run_server(debug=True)
