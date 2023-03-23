from dash import Dash
from dash import html
import dash_bootstrap_components as dbc
import map
import navbar

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

# Server

if __name__ == '__main__':
    app.run_server(debug=True)