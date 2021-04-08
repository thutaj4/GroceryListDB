class Store:
    def __init__(self, StoreName, URL, Street, Number, City, Zip, State):
        self.StoreName = StoreName
        self.URL = URL
        self.City = City
        self.Street = Street
        self.Number = Number
        self.Zip = Zip
        self.State = State

    def getStoreName(self):
        return self.StoreName

    def setStoreName(self, StoreName):
        self.StoreName = StoreName

    def getURL(self):
        return self.URL

    def setURL(self, URL):
        self.URL = URL

    def getStreet(self):
        return self.Street

    def setStreet(self, Street):
        self.Street = Street

    def getNumber(self):
        return self.Number

    def setNumber(self, Number):
        self.Number = Number

    def getCity(self):
        return self.City

    def setCity(self, City):
        self.City = City

    def getZip(self):
        return self.Zip

    def setZip(self, Zip):
        self.Zip = Zip

    def getState(self):
        return self.State

    def setState(self, State):
        self.State = State
