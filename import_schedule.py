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
            try:
                urlretrieve(testurl, 'temp.json')
            except:
                continue
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
                # Manually add building's hours that aren't imported
                if (temp_list[0] == "Mueller Center"):
                    opentime = datetime.time(9, 0, 0)
                    closetime = datetime.time(23, 0, 0)
                    for i in range(0, 7):
                      building_hours.append((dotw[i], opentime, closetime)) 
                if (temp_list[0] == "West Hall"):
                    opentime = datetime.time(8, 0, 0)
                    closetime = datetime.time(17, 0, 0)
                    for i in range(0, 7):
                      building_hours.append((dotw[i], opentime, closetime)) 
                if (temp_list[0] == "Folsom Library"):
                    opentime = datetime.time(8, 0, 0)
                    closetime = datetime.time(22, 0, 0)
                    for i in range(0, 7):
                      building_hours.append((dotw[i], opentime, closetime)) 
                if (temp_list[0] == "Sage Dining Hall"):
                    opentime = datetime.time(13, 30, 0)
                    closetime = datetime.time(20, 0, 0)
                    for i in range(0, 7):
                      building_hours.append((dotw[i], opentime, closetime))
                if (temp_list[0] == "Cogswell"):
                    opentime = datetime.time(12, 0, 0)
                    closetime = datetime.time(18, 0, 0)
                    for i in range(0, 7):
                      building_hours.append((dotw[i], opentime, closetime))
                if (temp_list[0] == "Commons Dining Hall"):
                    opentime = datetime.time(9, 0, 0)
                    closetime = datetime.time(23, 0, 0)
                    for i in range(0, 7):
                      building_hours.append((dotw[i], opentime, closetime))                
                building_list.append(building.Building(temp_list[0], 0, '', '', float(cordinfo['lon']), float(cordinfo['lat']), 0, '', building_hours, buildaccess))
    building_list.append(building.Building("'87 Gymnasium", 0, '', '', -73.67881, 42.7308, 0, '', building_hours, ''))
    building_list.append(building.Building("Blitman Dining Hall", 0, '', '', -73.68581, 42.73151, 0, '', building_hours, ''))
    building_list.append(building.Building("EMPAC Theater", 0, '', '', -73.68364, 42.72888, 0, '', building_hours, ''))
    building_list.append(building.Building("J Erik Jonsson Engineering Center", 0, '', '', -73.68016, 42.72968, 0, '', building_hours, ''))
    building_list.append(building.Building("Center for Biotechnology and Iterdisciplinary Studies", 0, '', '', -73.67863, 42.72832, 0, '', building_hours, ''))
    building_list.append(building.Building("Walker Laboratory", 0, '', '', -73.68259, 42.73082, 0, '', building_hours, ''))
    building_list.append(building.Building("Russel Sage Laboratory", 0, '', '', -73.68164, 42.73086, 0, '', building_hours, ''))
    building_list.append(building.Building("Hirsch Observatory", 0, '', '', -73.68051, 42.72842, 0, '', building_hours, ''))
    building_list.append(building.Building("Jonsson-Rowland Science Center (J-ROWL)", 0, '', '', -73.68057, 42.72889, 0, '', building_hours, ''))
    building_list.append(building.Building("Voorhees Computing Center", 0, '', '', -73.68179, 42.72923, 0, '', building_hours, ''))
    building_list.append(building.Building("Chapel + Cultural Center", 0, '', '', -73.67226, 42.73177, 0, '', building_hours, ''))
    building_list.append(building.Building("Carnegie Building", 0, '', '', -73.68322, 42.73043, 0, '', building_hours, ''))
    building_list.append(building.Building("East Campus Athlietic Village", 0, '', '', -73.66761, 42.73231, 0, '', building_hours, ''))
    building_list.append(building.Building("Houston Field House", 0, '', '', -73.66959, 42.73213, 0, '', building_hours, ''))
    building_list.append(building.Building("Admissions", 0, '', '', -73.67547, 42.73067, 0, '', building_hours, ''))
    building_list.append(building.Building("RPI Public Safety", 0, '', '', -73.67714, 42.72926, 0, '', building_hours, ''))
    return building_list