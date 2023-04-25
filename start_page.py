from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import map
import navbar
import dash

from dash.dependencies import Output, Input, State
import datetime

# global vars
view = 0
time = datetime.datetime.now().strftime('%A %I:%M %p')

map.reloadMap(view,time)

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

# Update the time using a button
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
        
        current_time = datetime.datetime.now()
        current_day = current_time.strftime('%A')
        if input_id == 'update_button':
            # Update the time with the inputted date and time
            if hour is not None and minute is not None:
                if hour >= 12:
                    ampm = 'PM'
                    if hour > 12:
                        hour -= 12
                else:
                    ampm = 'AM'
                    if hour == 0:
                        hour = 12
                current_time = datetime.datetime.strptime(f'{current_day} {hour}:{minute} {ampm}', '%A %I:%M %p')
            elif hour is None and minute is not None:
                current_time = datetime.datetime.strptime(f'{current_day} 00:{minute} PM', '%A %I:%M %p')
            elif hour is not None and minute is None:
                if hour >= 12:
                    ampm = 'PM'
                else:
                    ampm = 'AM'
                current_time = datetime.datetime.strptime(f'{current_day} {hour}:00 {ampm}', '%A %I:%M %p')
    # Format the time string and return it as the output

    current_time_str = current_time.strftime('%A %I:%M %p')
    global time
    time = current_time_str
    return current_time_str

# Change the view using a button
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

    global view
    if button_id == "Student":
        view = 1
    if button_id == "Faculty":
        view = 2
    if button_id == "Staff":
        view = 3
    if button_id == "Guest":
        view = 4
    return view

# Update the map after the view or time is changed
@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    [dash.dependencies.Input('view', 'children'),
     dash.dependencies.Input('time','children')])
def update_map(view, time):
    map.reloadMap(view,time)
    return open('my_map.html', 'r').read()

# Server
if __name__ == '__main__':
    app.run_server(debug=False)
