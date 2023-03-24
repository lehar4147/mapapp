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
        self.building_hours = building_hours
        self.shops = shops

    def getShedule(self):
        return self.building_hours

class Shop:
    def __init__(self, name, code, shop_type, shop_hours):
        self.name = name
        self.code = code
        self.shop_type = shop_type
        self.shop_hours = shop_hours

    def getShedule(self):
        return self.shop_hours