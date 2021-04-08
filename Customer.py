class Customer:

    def __init__(self, FirstName, LastName, Street, Number, City, Zip, State):
        self.FirstName = FirstName
        self.LastName = LastName
        self.Street = Street
        self.Number = Number
        self.City = City
        self.Zip = Zip
        self.State = State

    def getFirstName(self):
        return self.FirstName

    def setFirstName(self, FirstName):
        self.FirstName = FirstName

    def getLastName(self):
        return self.LastName

    def setLastName(self, LastName):
        self.LastName = LastName

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
