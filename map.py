from dash import html
import folium

import building

# Main map
RPI_coor = [42.73, -73.6775]
my_map = folium.Map(location=RPI_coor, zoom_start=24)

# Marker
tooltip = "Click Here For More Info"
for build in building.buildings:
    color = "red"
    icon = "info-sign"

    # icon indicates the type of building
    if (build.getBuildingType() == "Dining"):
        icon = "cutlery"
    elif (build.getBuildingType() == "Academic"):
        icon = "education"
    elif (build.getBuildingType() == "Residential"):
        icon = "home"
    elif (build.getBuildingType() == "Athletic"):
        icon = "apple"
    elif (build.getBuildingType() == "Parking"):
        icon = "road"
    elif (build.getBuildingType() == "Other"):
        icon = "question-sign"

    # color indicates if the building is open or not
    if (build.isOpen()):
        color = "green"
    
    marker = folium.Marker(
        location=[build.getLatitude(), build.getLongitude()],
        icon=folium.Icon(color = color, icon = icon),
        popup=build.getName(),
        tooltip=tooltip)
    marker.add_to(my_map)

my_map.save('my_map.html')

# Layout
layout = html.Iframe(id='map', srcDoc=open('my_map.html','r').read(), width='100%', height='600')