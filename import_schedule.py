from urllib.request import urlretrieve
from urllib.request import urlopen
import ssl
from bs4 import BeautifulSoup
import datetime
import json
import building

dotw = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
building_type_list = ["Community Access", "Unlocked", "Locked/Closed"]
# Ignore for building hours
badformat = ["Cogswell", "Folsom Library", "Mueller Center"]

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
            buildaccess = ''
            if ('/' in temp_list[0]):
                t = temp_list[0].split('/')
                temp_list[0] = t[1]
            if ('\xa0' in temp_list[0]):
                temp_list[0] = temp_list[0].replace('\xa0', '')
            urlstring = temp_list[0].replace(" ", "+")
            testurl = 'https://nominatim.openstreetmap.org/search?q='+urlstring+',+troy,+new+york&format=json&polygon=1&addressdetails=1'
            urlretrieve(testurl, 'temp.json')
            with open("temp.json", 'r') as f:
                data = f.read()
            if (data != '[]'):
                if ('},' in data):
                    newdata = data[1:data.index('},')] + '}'
                else:
                    newdata = data[1:len(data)-1]
                with open("temp.json", 'w') as f:
                    f.write(newdata)
                cordinfo = json.loads(open("temp.json", encoding="utf8").read())

                for b in building_type_list:
                    if (b in temp_list[1]):
                        buildaccess = b
                
                building_hours = []
                # Parse hours (edge case)
                if (temp_list[2] == '24/7'):
                    for day in dotw:
                        building_hours.append((day, datetime.time(0,0), datetime.time(23,59)))
                # Regular Parsing for hours is not implemented yet
                elif (temp_list[0] not in badformat):
                    words = temp_list[2].split()
                    if (words[0] != 'Please'):
                        segments = temp_list[2].split(';')
                        for seg in segments:
                            small_segments = seg.split()
                            if (small_segments[0][0].isnumeric() and small_segments[2][0].isnumeric()):
                                index1 = small_segments[0].index('AM')
                                index2 = small_segments[2].index('PM')
                                opentime = datetime.time(int(small_segments[0][0:index1]),0,0)
                                closetime = datetime.time(int(small_segments[2][0:index2])+12,0,0)
                                if (len(small_segments) == 4):
                                    building_hours.append((small_segments[3], opentime, closetime))
                                elif (len(small_segments) == 6):
                                    startday = small_segments[3]
                                    endday = small_segments[5]
                                    startindex = dotw.index(startday)
                                    endindex = dotw.index(endday)
                                    for i in range(startindex, endindex+1):
                                        building_hours.append((dotw[i], opentime, closetime))
                building_list.append(building.Building(temp_list[0], 0, '', '', float(cordinfo['lon']), float(cordinfo['lat']), 0, '', building_hours, buildaccess))
    return building_list