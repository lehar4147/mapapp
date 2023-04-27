import import_schedule

# building class
class Building:
    # Attributes
    def __init__(self, name, building_type, longitude, latitude, description, building_hours, building_access):
        self.__name = name
        self.__building_type = building_type
        self.__longitude = longitude
        self.__latitude = latitude
        self.__description = description
        self.__building_hours = building_hours # list of tuples (day, open, close)
        self.__building_access = building_access

    # Getters (encapsulation)
    def getName(self):
        return self.__name
    
    def getBuildingType(self):
        return self.__building_type

    def getLongitude(self):
        return self.__longitude
    
    def getLatitude(self):
        return self.__latitude
    
    def getDescription(self):
        return self.__description

    def getSchedule(self):
        return self.__building_hours
    
    def getAccess(self):
        return self.__building_access
    
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
            if self.getAccess() == 'Locked/Closed':
                result = False
            elif self.getAccess() == 'Unlocked':
                result = True
            else:
                # Depends on view
                if view == 4:
                    result = False
                else:
                    result = False
                    #Check if time is within shedule open hours
                    for hours in self.getSchedule():
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