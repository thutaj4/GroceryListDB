class Customer:

	def __init__(self, FirstName, LastName, HouseNum, Street, City):
		self.FirstName = FirstName
		self.LastName = LastName
		self.HouseNum = HouseNum
		self.Street = Street
		self.City = City

	def getFirstName(self):
		return self.FirstName

	def setFirstName(self, FirstName):
		self.FirstName = FirstName

	def getLastName(self):
		return self.LastName

	def setLastName(self, LastName):
		self.LastName = LastName

	def getHouseNum(self):
		return self.HouseNum

	def setHouseNum(self, HouseNum):
		self.HouseNum = HouseNum

	def getCity(self):
		return self.City

	def setCity(self, City):
		self.City = City

	def getStreet(self):
		return self.Street

	def setStreet(self, Street):
		self.Street = Street
