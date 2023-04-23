import import_schedule

class Building:
    def __init__(self, name, code, building_type, address, longitude, latitude, image, description, building_hours, building_access, shops):
        self.name = name
        self.code = code
        self.building_type = building_type
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.image = image
        self.description = description
        self.building_hours = building_hours # list of tuples (day, open, close)
        self.building_access = building_access
        self.shops = shops

    def getName(self):
        return self.name
    
    def getBuildingType(self):
        return self.building_type

    def getLongitude(self):
        return self.longitude
    
    def getLatitude(self):
        return self.latitude

    def getSchedule(self):
        return self.building_hours
    
    def isOpen(self, view, time): # view argument represent the point of view of the viewer, specifically:
                      # 0 = not specified
                      # 1 = Student View
                      # 2 = Faculty View
                      # 3 = Staff View
                      # 4 = Guest View
        
        # Split the input date string into day, time, and AM/PM components
        time_str = time.split(' ')
        day = time_str[0]
        # Split the time string into hour and minute components
        hour_str, minute_str = time_str[1].split(':')
        am_pm = time_str[2]
        
        # Convert the hour into 24-hour format
        hour = int(hour_str)
        if am_pm == 'PM' and hour != 12:
            hour += 12
        elif am_pm == 'AM' and hour == 12:
            hour = 0
        minute = int(minute_str)
        result = False

        #Check current view
        if (view is not None):
            if self.building_access == 'Locked/Closed':
                result = False
            elif self.building_access == 'Unlocked':
                result = True
            else:
                # Depends on view
                if view == 4:
                    result = False
                else:
                    result = False
                    #Check if time is within shedule open hours
                    for hours in self.building_hours:
                        if hours[0] == day:
                            if int(hours[1].hour) <= hour and hour < int(hours[2].hour):
                                result = True
                                break
                            elif int(hours[2].hour) == hour and int(hours[2].minute) <= minute:
                                result = True
                                break
        return result

# List of buildings to be read into the map
buildings = import_schedule.run_import()