import navbar
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
    
    def numShops(self):
        return len(self.shops)

    def getShops(self):
        return self.shops
    
    def isOpen(self): # view argument represent the point of view of the viewer, specifically:
                      # 0 = not specified
                      # 1 = Student View
                      # 2 = Faculty View
                      # 3 = Staff View
                      # 4 = Guest View
        # For now it disregards time
        if self.building_access == 'Locked/Closed':
            result = False
        elif self.building_access == 'Unlocked':
            result = True
        else:
            # Depends on view
            result = True
        #time = navbar.getTime()
        #for hours in self.building_hours:
        #if hours[1] <= time and time <= hours[2]:
        return result

class Shop:
    def __init__(self, name, code, shop_type, shop_hours):
        self.name = name
        self.code = code
        self.shop_type = shop_type
        self.shop_hours = shop_hours

    def getName(self):
        return self.name

    def getSchedule(self):
        return self.shop_hours

# List of buildings to be read into the map
buildings = import_schedule.run_import()