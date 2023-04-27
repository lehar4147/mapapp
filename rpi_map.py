'''This module defines the making of map'''
import datetime
from dash import html
import folium

import building

# Main map
RPI_coor = [42.73, -73.6775]

def reload_map(view,time):
    """
    Creates a Folium map showing RPI buildings and their status based on the given view and time.

    Args:
        view (str): The view to show, either "day" or "night".
        time (datetime.time): The time to show, in 24-hour format.

    Returns:
        None
    """
    my_map = folium.Map(location=RPI_coor,
                        min_zoom= 16,
                        max_zoom= 18,
                        zoom_start=18,
                        min_lat= 42.72558,
                        max_lat= 42.73984,
                        min_lon= -73.68990,
                        max_lon= -73.66338,
                        max_bounds= True)

    # Marker
    tooltip = "Click Here For More Info"
    for build in building.buildings:
        html_template = f"""
            <h1>{build.get_name()}</h1>
            <p>{build.get_description}</p>
            """
        # Find schedule for each building
        for sched in build.get_schedule():
            html_template += f"""
                <p>{sched[0]}: {sched[1]} - {sched[2]}</p>
                """
        iframe = folium.IFrame(html=html_template, width=300, height=200)
        popup = folium.Popup(iframe, max_width=300)
        color = "red"
        icon = "info-sign"

        # icon indicates the type of building
        if build.get_building_type() == "Dining":
            icon = "cutlery"
        elif build.get_building_type() == "Academic":
            icon = "education"
        elif build.get_building_type() == "Residential":
            icon = "home"
        elif build.get_building_type() == "Athletic":
            icon = "apple"
        elif build.get_building_type() == "Parking":
            icon = "road"
        elif build.get_building_type() == "Other":
            icon = "question-sign"
        # Set open status color for each building
        if build.is_open(view,time):
            color = "green"
        # Mark every RPI building with appropriate color icon
        marker = folium.Marker(
            location=[build.get_latitude(), build.get_longitude()],
            icon=folium.Icon(color = color, icon = icon),
            popup=popup,
            tooltip=tooltip)
        marker.add_to(my_map)

    my_map.save('my_map.html')

# Layout
reload_map(0, datetime.datetime.now().strftime('%A %I:%M %p'))
with open('my_map.html', 'r', encoding='utf-8') as map_file:
    layout = html.Iframe(id='map', srcDoc=map_file.read(), width='100%', height='600')
