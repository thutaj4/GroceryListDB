class Store:
    def __init__(self, CompName, URL, BuildingNum, City, Street):
        self.CompName = CompName
        self.URL = URL
        self.BuildingNum = BuildingNum
        self.City = City
        self.Street = Street

    def getCompName(self):
	    return self.CompName

    def setCompName(self, CompName):
	    self.CompName = CompName

    def getURL(self):
        return self.URL

    def setURL(self, URL):
        self.URL = URL

    def getBuildingNum(self):
	    return self.BuildingNum

    def setBuildingNum(self, BuildingNum):
	    self.BuildingNum = BuildingNum

    def getCity(self):
	    return self.City

    def setCity(self, City):
	    self.City = City

    def getStreet(self):
	    return self.Street

    def setStreet(self, Street):
	    self.Street = Street


    