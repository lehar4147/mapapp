from urllib.request import urlretrieve
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup
import datetime
import json
import building

dotw = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Returns a list of Building objects
def run_import():
    ssl._create_default_https_context = ssl._create_unverified_context
    url = 'https://publicsafety.rpi.edu/campus-security/card-access-schedule'
    url2 = 'https://nominatim.openstreetmap.org/search?q=134+pilkington+avenue,+birmingham&format=json&polygon=1&addressdetails=1'
    urlretrieve(url, 'rawdata.html')
    urlretrieve(url2, 'temp.json')
    with open("temp.json", 'r') as f:
        data = f.read()
    newdata = data[1:data.index('},')] + '}'
    with open("temp.json", 'w') as f:
        f.write(newdata)
    soup = BeautifulSoup(open("rawdata.html", encoding="utf8").read(), 'html.parser')
    cordinfo = json.loads(open("temp.json", encoding="utf8").read())

    building_list = []

    for row in soup.find_all('tr'):
        temp_list = []
        for element in row.find_all('td'):
            temp_list.append(element.next)
        if (len(temp_list) > 0):
            building_hours = []
            # Parse hours (edge case)
            if (temp_list[2] == '24/7'):
                for day in dotw:
                    building_hours.append((day, datetime.time(12,0,0), datetime.time(23,59,59)))
            # Regular Parsing for hours is not implemented yet
            #else:
                #words = temp_list[2].split()
                #if (words[0] != 'Please'):
                    #segments = temp_list[2].split(';')
                    #for seg in segments:
                        #small_segments = seg.split()
                        #if (small_segments[0][0].isnumeric()):
                            #index1 = small_segments[0].index('AM')
                            #index2 = small_segments[2].index('PM')
                            #opentime = datetime.time(int(small_segments[0][0:index1]),0,0)
                            #closetime = datetime.time(int(small_segments[2][0:index2])+12,0,0)
            building_list.append(building.Building(temp_list[0], 0, '', '', 0, 0, 0, temp_list[0], building_hours, []))

    return building_list

# For Testing Purposes
#bl = run_import()