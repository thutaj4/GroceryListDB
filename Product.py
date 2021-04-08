class Product:
    def __init__(self, SKU, Price, Link, ItemName):
        self.SKU = SKU
        self.Price = Price
        self.Link = Link
        self.ItemName = ItemName

    def getSKU(self):
        return self.SKU

    def setSKU(self, SKU):
        self.SKU = SKU

    def getPrice(self):
        return self.Price

    def setPrice(self, Price):
        self.Price = Price

    def getLink(self):
        return self.Link

    def setLink(self, Link):
        self.Link = Link

    def getItemName(self):
        return self.ItemName

    def setItemName(self, ItemName):
        self.ItemName = ItemName
