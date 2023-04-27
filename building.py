'''This module defines the building class'''
import import_schedule

# building class
class Building:
    """
    Represents a building affiliated with RPI.
    """
    # Attributes
    def __init__(self, name, code, building_type, address,
                 longitude, latitude, image,
                 description, building_hours, building_access):
        self.__name = name
        self.__code = code
        self.__building_type = building_type
        self.__address = address
        self.__longitude = longitude
        self.__latitude = latitude
        self.__image = image
        self.__description = description
        self.__building_hours = building_hours # list of tuples (day, open, close)
        self.__building_access = building_access
    # Getters (encapsulation)
    def get_name(self):
        """
        Returns the name of the building.

        Returns:
        str: The name of the building.
        """
        return self.__name
    def get_building_type(self):
        """
        Returns the type of the building.

        Returns:
        str: The type of the building.
        """
        return self.__building_type
    def get_longitude(self):
        """
        Returns the longitude of the building.

        Returns:
        float: The longitude of the building.
        """
        return self.__longitude
    def get_latitude(self):
        """
        Returns the latitude of the building.

        Returns:
        float: The latitude of the building.
        """
        return self.__latitude
    def get_description(self):
        """
        Returns the description of the building.

        Returns:
        str: The description of the building.
        """
        return self.__description
    def get_schedule(self):
        """
        Returns the schedule of the building.

        Returns:
        dict: The schedule of the building.
        """
        return self.__building_hours
    def get_access(self):
        """
        Returns the access of the building.

        Returns:
        str: The access of the building.
        """
        return self.__building_access
    def is_open(self, view, time):
        # view argument represent the point of view of the viewer
        """
        Checks if the building is open at the given time from the given view.

        Args:
            view (int): The point of view of the viewer, where:
                0 = not specified
                1 = Student View
                2 = Faculty View
                3 = Staff View
                4 = Guest View
            time (str): The time to check in the format of "Day Hour:Minute AM/PM", where:
                Day is the three-letter abbreviation for the day of the week (e.g. "Mon")
                Hour is the hour in 12-hour format (1-12)
                Minute is the minute (00-59)
                AM/PM is the meridiem indicator ("AM" or "PM")

        Returns:
            bool: True if the building is open at the given time and from the given view, 
                  False otherwise.
        """
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
        if view is not None:
            if self.get_access() == 'Locked/Closed':
                result = False
            elif self.get_access() == 'Unlocked':
                result = True
            else:
                # Depends on view
                if view == 4:
                    result = False
                else:
                    result = False
                    #Check if time is within shedule open hours
                    for hours in self.get_schedule():
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
