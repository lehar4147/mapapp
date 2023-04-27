'''This module defines the start page for the application.'''
import datetime
from dash.dependencies import Output, Input, State
from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import dash
import rpi_map
import navbar

# global vars
VIEW = 0
TIME = datetime.datetime.now().strftime('%A %I:%M %p')

# App Initialization

rpi_map.reload_map(VIEW,TIME)

app = Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout

app.layout = html.Div([
    html.Div(
        navbar.layout
    ),
    html.Div(
        rpi_map.layout
    )
])

@app.callback(
    Output('time', 'children'),
    Input('update_button', 'n_clicks'),
    Input('reset_button', 'n_clicks'),
    State('hour_input', 'value'),
    State('minute_input', 'value')
)
def update_time(update_clicks, reset_clicks, hour, minute):
    """
    Update the time based on user inputs

    Args:
    update_clicks (int): The number of times the update button has been clicked.
    reset_clicks (int): The number of times the reset button has been clicked.
    hour (int): The hour selected by the user, in 24-hour format (0-23).
    minute (int): The minute selected by the user (0-59).

    Returns:
    str: A string representation of the current time, in the format "weekday hour:minute AM/PM".
    """
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
                current_time = datetime.datetime.strptime(
                    f'{current_day} {hour}:{minute} {ampm}', '%A %I:%M %p'
                )
            elif hour is None and minute is not None:
                current_time = datetime.datetime.strptime(
                    f'{current_day} 00:{minute} PM', '%A %I:%M %p'
                )
            elif hour is not None and minute is None:
                if hour >= 12:
                    ampm = 'PM'
                else:
                    ampm = 'AM'
                current_time = datetime.datetime.strptime(
                    f'{current_day} {hour}:00 {ampm}', '%A %I:%M %p'
                )
    # Format the time string and return it as the output
    current_time_str = current_time.strftime('%A %I:%M %p')
    global TIME
    TIME = current_time_str
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
    """
    Update the VIEW global variable based on the user's button click.

    Args:
        student (int): The number of clicks on the "Student" button.
        faculty (int): The number of clicks on the "Faculty" button.
        staff (int): The number of clicks on the "Staff" button.
        guest (int): The number of clicks on the "Guest" button.

    Returns:
        int: The value of the VIEW global variable after the button click. The possible
        values are:
        1. If "Student" button is clicked, VIEW = 1.
        2. If "Faculty" button is clicked, VIEW = 2.
        3. If "Staff" button is clicked, VIEW = 3.
        4. If "Guest" button is clicked, VIEW = 4.
        If no button is clicked, returns the empty string.

    """
    # Check which input triggered the callback
    ctx = dash.callback_context
    if not (student or faculty or staff or guest) or not ctx.triggered:
        return ""

    # Retrieve what viewpoint the user has clicked
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    global VIEW
    if button_id == "Student":
        VIEW = 1
    if button_id == "Faculty":
        VIEW = 2
    if button_id == "Staff":
        VIEW = 3
    if button_id == "Guest":
        VIEW = 4
    return VIEW

# Update the map after the view or time is changed
@app.callback(
    dash.dependencies.Output('map', 'srcDoc'),
    [dash.dependencies.Input('view', 'children'),
     dash.dependencies.Input('time','children')])
def update_map(view, time):
    """
    Updates the map in the Dash application based on the selected view and time.

    Args:
    view (str): The current view selected by the user.
    time (str): The current time in the format '%A %I:%M %p'.

    Returns:
    str: The HTML source code of the updated map.
    """
    # Reload map when user has changed view or time
    rpi_map.reload_map(view,time)
    with open('my_map.html', 'r', encoding='utf-8') as map_file:
        return map_file.read()

# Server
if __name__ == '__main__':
    app.run_server(debug=False)
