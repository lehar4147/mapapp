from urllib.request import urlretrieve
import ssl
from bs4 import BeautifulSoup
import datetime
import building

dotw = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Returns a list of Building objects
def run_import():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://publicsafety.rpi.edu/campus-security/card-access-schedule'
    urlretrieve(url, 'rawdata.html')
    soup = BeautifulSoup(open("rawdata.html", encoding="utf8").read(), 'html.parser')

    building_list = []

    for row in soup.find_all('tr'):
        temp_list = []
        for element in row.find_all('td'):
            temp_list.append(element.next)
        if (len(temp_list) > 0):
            building_hours = []
            # Parse hours
            if (temp_list[2] == '24/7'):
                for day in dotw:
                    building_hours.append((day, datetime.time(12,0,0), datetime.time(23,59,59)))
            segments = temp_list[2].split(';')
            building_list.append(building.Building(temp_list[0], 0, '', '', 0, 0, 0, temp_list[0], [], []))

    return building_list

# For Testing Purposes
bl = run_import()