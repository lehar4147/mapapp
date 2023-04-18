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
    Output('time', 'children'),
    Input('update_button', 'n_clicks'),
    Input('reset_button', 'n_clicks'),
    State('hour_input', 'value'),
    State('minute_input', 'value'),
)
def update_time(update_clicks, reset_clicks, hour, minute):
    # Check which input triggered the callback
    ctx = dash.callback_context
    if not ctx.triggered:
        # Callback was triggered by the interval component
        current_time = datetime.datetime.now()
    else:
        # Get the ID of the input that triggered the callback
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]
        
        if input_id == 'update_button':
            # Update the time with the inputted date and time
            if hour is not None and minute is not None:
                current_time = datetime.datetime.strptime(f'{hour}:{minute}', '%H:%M')
            elif hour is None and minute is not None:
                current_time = datetime.datetime.strptime(f'00:{minute}', '%H:%M')
            elif hour is not None and minute is None:
                current_time = datetime.datetime.strptime(f'{hour}:00', '%H:%M')
            else:
                current_time = datetime.datetime.now()
        elif input_id == 'reset_button':
            # Reset the time to the current time
            current_time = datetime.datetime.now()
        else:
            # Callback was triggered by the interval component
            current_time = datetime.datetime.now()
    
    # Format the time string and return it as the output
    current_time_str = current_time.strftime('%I:%M %p')
    return current_time_str

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

@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    [dash.dependencies.Input('view', 'children'),
     dash.dependencies.Input('time','children')])
def update_map(view, time):
    if view == 0 and time == 0:
        return dash.no_update
    else:
        return open('my_map.html', 'r').read()

# Server
if __name__ == '__main__':
    app.run_server(debug=True)
