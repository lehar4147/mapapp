import navbar

class Building:
    def __init__(self, name, code, building_type, address, longitude, latitude, image, description, building_hours, shops):
        self.name = name
        self.code = code
        self.building_type = building_type
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.image = image
        self.description = description
        self.building_hours = building_hours # list of tuples (day, open, close)
        self.shops = shops

    def getName(self):
        return self.name
    
    def getBuildingType(self):
        return self.building_type

    def getLongitude(self):
        return self.longitude
    
    def getLatitude(self):
        return self.latitude

    def getShcedule(self):
        return self.building_hours
    
    def isOpen(self):
        time = navbar.getTime()
        for hours in self.building_hours:
            if hours[1] <= time and time <= hours[2]:
                return True

class Shop:
    def __init__(self, name, code, shop_type, shop_hours):
        self.name = name
        self.code = code
        self.shop_type = shop_type
        self.shop_hours = shop_hours

    def getShedule(self):
        return self.shop_hours
    
# List of buildings to be read into the map
buildings = []