import sqlite3
from sqlite3 import Error
from Customer import Customer
from Store import Store
from Product import Product
from Product_List import Product_List

conn = None
c = None


###########################################################################
######################## CONNECT TO DATABASE ##############################
###########################################################################


def connect():
    global conn
    global c
    try:
        conn = sqlite3.connect('shoppinglist.db')
        c = conn.cursor()
        print("Database connection successful")
        print(sqlite3.version)
    except Error as e:
        print("Database connection failed")
        print(e)

###########################################################################
######################## FILL DATABASE ####################################
###########################################################################
def fill():
    cust_1 = Customer('John', 'Doe', 'state street',
                      '1234', 'la crosse', '54601', 'WI')
    cust_2 = Customer('Jane', 'Duh', 'pine street',
                      '333', 'la crosse', '54601', 'WI')
    cust_3 = Customer('Tim', 'Doe', 'state street',
                      '1234', 'la crosse', '54601', 'WI')
    cust_4 = Customer('Timmy', 'Kim', '12th street',
                      '1212', 'la crosse', '54603', 'WI')

    insert_customer(cust_1)
    insert_customer(cust_2)
    insert_customer(cust_3)
    insert_customer(cust_4)

    store_1 = Store('Festival', 'www.festival.com',
                    'lousy BLVD', '232', 'Lacrosse', '54601', 'WI')
    store_2 = Store('Target', 'www.target.com',
                    'county highway', '1112', 'Onalaska', '54603', 'WI')

    insert_store(store_1)
    insert_store(store_2)

    list_1 = Product_List("shopping list")
    list_2 = Product_List("wish list")

    insert_list(list_1)
    insert_list(list_2)

    product_1 = Product("283YDGS", 29.00, "www.website.com", "paper")
    product_2 = Product("343YDGS", 100.00, "www.website.com", "t-shirt")
    product_3 = Product("2586YDGS", 2.99, "www.website.com", "t-shirt")
    product_4 = Product("sjdDGS", 23.99, "www.website.com", "pants")
    product_5 = Product("283Yeui8", 25.00, "www.website.com", "apple")
    product_6 = Product("2dhrudh74", 200.00, "www.website.com", "t-shirt")

    insert_product(product_1)
    insert_product(product_2)
    insert_product(product_3)
    insert_product(product_4)
    insert_product(product_5)
    insert_product(product_6)

    conn.close()
    print("DB Closed")


###########################################################################
######################## CUSTOMER METHODS #################################
###########################################################################
def insert_customer(cust):
    with conn:
        c.execute("INSERT INTO Customer VALUES (:CustomerID, :FirstName, :LastName, :Street, :Number, :City, :Zip, :State)",
                  {'CustomerID': None, 'FirstName': cust.FirstName, 'LastName': cust.LastName, 'Street': cust.Street, 'Number': cust.Number,
                   'City': cust.City, 'Zip': cust.Zip, 'State': cust.State})

def get_cust_by_name(lastname):
    c.execute("SELECT * FROM Customer WHERE LastName=:LastName", {'LastName': lastname})
    return c.fetchall()

def get_all_cust():
    c.execute("SELECT * FROM Customer")
    return c.fetchall()

def edit_user(CustomerID, attribute, newVal):
    if attribute == "first name":
        with conn:
            c.execute("UPDATE Customer SET FirstName = :FirstName WHERE CustomerID = :CustomerID",
             {'FirstName': newVal, 'CustomerID': CustomerID})
    elif attribute == "last name":
        with conn:
            c.execute("UPDATE Customer SET LastName = :LastName WHERE CustomerID = :CustomerID",
             {'LastName': newVal, 'CustomerID': CustomerID})
    elif attribute == "street":
        with conn:
            c.execute("UPDATE Customer SET Street = :Street WHERE CustomerID = :CustomerID",
             {'Street': newVal, 'CustomerID': CustomerID})
    elif attribute == "number":
        with conn:
            c.execute("UPDATE Customer SET Number = :Number WHERE CustomerID = :CustomerID",
             {'Number': newVal, 'CustomerID': CustomerID})
    elif attribute == "city":
        with conn:
            c.execute("UPDATE Customer SET City = :City WHERE CustomerID = :CustomerID",
             {'City': newVal, 'CustomerID': CustomerID})
    elif attribute == "zip":
        with conn:
            c.execute("UPDATE Customer SET Zip = :Zip WHERE CustomerID = :CustomerID",
             {'Zip': newVal, 'CustomerID': CustomerID})
    elif attribute == "state":
        with conn:
            c.execute("UPDATE Customer SET State = :State WHERE CustomerID = :CustomerID",
             {'State': newVal, 'CustomerID': CustomerID})

def remove_cust(FirstName, LastName):
    with conn:
        c.execute("DELETE from Customer WHERE FirstName = :FirstName AND LastName = :LastName",
                  {'FirstName': FirstName, 'LastName': LastName})

###########################################################################
######################## STORE METHODS ####################################
###########################################################################
def insert_store(store):
    with conn:
        c.execute("INSERT INTO Store VALUES (:id, :StoreName, :URL, :Street, :Number, :City, :Zip, :State)",
                  {'id': None, 'StoreName': store.StoreName, 'URL': store.URL, 'Street': store.Street,
                   'Number': store.Number, 'City': store.City, 'Zip': store.Zip, 'State': store.State})

def get_all_store():
    c.execute("SELECT * FROM Store")
    return c.fetchall()

def get_store_by_name(name):
    c.execute("SELECT * FROM Store WHERE StoreName=:StoreName", {'StoreName': name})
    return c.fetchall()

def edit_store(StoreID, attribute, newVal):
    if attribute == "store name":
        with conn:
            c.execute("UPDATE Store SET StoreName = :StoreName WHERE StoreID = :StoreID",
             {'StoreName': newVal, 'StoreID': StoreID})
    elif attribute == "url":
        with conn:
            c.execute("UPDATE Store SET URL = :URL WHERE StoreID = :StoreID",
             {'URL': newVal, 'StoreID': StoreID})
    elif attribute == "street":
        with conn:
            c.execute("UPDATE Store SET Street = :Street WHERE StoreID = :StoreID",
             {'Street': newVal, 'StoreID': StoreID})
    elif attribute == "number":
        with conn:
            c.execute("UPDATE Store SET Number = :Number WHERE StoreID = :StoreID",
             {'Number': newVal, 'StoreID': StoreID})
    elif attribute == "city":
        with conn:
            c.execute("UPDATE Store SET City = :City WHERE StoreID = :StoreID",
             {'City': newVal, 'StoreID': StoreID})
    elif attribute == "zip":
        with conn:
            c.execute("UPDATE Store SET Zip = :Zip WHERE StoreID = :StoreID",
             {'Zip': newVal, 'StoreID': StoreID})
    elif attribute == "state":
        with conn:
            c.execute("UPDATE Store SET State = :State WHERE StoreID = :StoreID",
             {'State': newVal, 'StoreID': StoreID})

def remove_store(StoreName):
    with conn:
        c.execute("DELETE from Store WHERE StoreName = :StoreName", {'StoreName': StoreName})

###########################################################################
######################## PROUCT LIST METHODS ##############################
###########################################################################

def insert_list(list):
    with conn:
        c.execute("INSERT INTO ProductList VALUES (:id, :Title)",
                  {'id': None, 'Title': list.Title})

def get_list_by_title(title):
    c.execute("SELECT * FROM ProductList WHERE Title=:Title", {'Title': title})
    return c.fetchall()

def get_all_list():
    c.execute("SELECT * FROM ProductList")
    return c.fetchall()

def edit_product_list(id, attribute, newVal):
    if attribute == "title":
        with conn:
            c.execute("UPDATE ProductList SET Title = :Title WHERE ProductListID = :ProductListID",
             {'Title': newVal, 'ProductListID': id})

def remove_product_list(Title):
    with conn:
            c.execute("DELETE from ProductList WHERE Title = :Title", {'Title': Title})

###########################################################################
######################## PRODUCT METHODS ##################################
###########################################################################
def insert_product(product):
    with conn:
        c.execute("INSERT INTO Product VALUES (:id, :SKU, :Price, :Link, :ItemName)",
                  {'id': None, 'SKU': product.SKU, 'Price': product.Price, 'Link': product.Link,
                   'ItemName': product.ItemName})

def get_all_product():
    c.execute("SELECT * FROM Product")
    return c.fetchall()

def get_product_by_name(name):
    c.execute("SELECT * FROM Product WHERE ItemName=:ItemName", {'ItemName': name})
    return c.fetchall()

def edit_product(id, attribute, newVal):
    if attribute == "sku":
        with conn:
            c.execute("UPDATE Product SET SKU = :SKU WHERE ProductID = :ProductID",
             {'SKU': newVal, 'ProductID': id})
    elif attribute == "price":
        with conn:
            c.execute("UPDATE Product SET price = :price WHERE ProductID = :ProductID",
             {'price': newVal, 'ProductID': id})
    elif attribute == "link":
        with conn:
            c.execute("UPDATE Product SET link = :link WHERE ProductID = :ProductID",
             {'link': newVal, 'ProductID': id})
    elif attribute == "item name":
        with conn:
            c.execute("UPDATE Product SET ItemName = :ItemName WHERE ProductID = :ProductID",
             {'ItemName': newVal, 'ProductID': id})

def remove_product(SKU):
    with conn:
        c.execute("DELETE from Product WHERE SKU = :SKU", {'SKU': SKU})

###########################################################################
######################## USER INPUT #######################################
###########################################################################

# called when the user want to add data to the database
def addSomthing():
    print("\n(AU) -- Add a user")
    print("(AP) -- Add a product")
    print("(AL) -- Add a list")
    print("(AS) -- Add a store\n")
    
    selection = input("Select what to add: ").upper()

    if selection == "AU":
        FirstName = input("Enter a first name: ")
        LastName = input("Enter a last name: ")
        Street = input("Enter a street: ")
        Number = input("Enter a house number: ")
        City = input("Enter a city: ")
        Zip = input("Enter a zip code: ")
        State = input("Enter a state: ")
        cust = Customer(FirstName, LastName, Street, Number, City, Zip, State)
        insert_customer(cust) 
        print(FirstName + " has been added")

    elif selection == "AP":
        SKU = input("Enter a SKU: ")
        Price = input("Enter a price: ")
        Link = input("Enter a link: ")
        ItemName = input("Enter a item name: ")
        prod = Product(SKU, Price, Link, ItemName)
        insert_product(prod) 
        print(ItemName + " has been added")

    elif selection == "AL":
        Title = input("Enter a title: ")
        list = Product_List(Title)
        insert_list(list)
        print(Title + " has been added")

    elif selection == "AS":
        StoreName = input("Enter a store name: ")
        URL = input("Enter a url: ")
        Street = input("Enter a street: ")
        Number = input("Enter a house number: ")
        City = input("Enter a city: ")
        Zip = input("Enter a zip code: ")
        State = input("Enter a state: ")
        store = Store(StoreName, URL, Street, Number, City, Zip, State)
        insert_store(store)
        print(StoreName + " has been added")

# called when the user want to remove data to the database
def removeSomthing():
    print("\n(RU) -- Remove a user")
    print("(RP) -- Remove a product")
    print("(RL) -- Remove a list")
    print("(RS) -- Remove a store\n")
    
    selection = input("Select what to remove: ").upper()

    if selection == "RU":
        print("Enter first and last name of user to remove")
        FirstName = input("Enter a first name: ")
        LastName = input("Enter a last name: ")
        remove_cust(FirstName, LastName)
        print(FirstName + " " + LastName + " has been removed")

    elif selection == "RP":
        print("Enter SKU of item to remove")
        SKU = input("Enter a SKU: ")
        remove_product(SKU)
        print(SKU + " has been removed")

    elif selection == "RL":
        print("Enter title of list to remove")
        Title = input("Enter a title: ")
        remove_product_list(Title)
        print(Title + " has been removed")
    elif selection == "RS":
        print("Enter name of store to remove")
        StoreName = input("Enter a name: ")
        remove_store(StoreName)
        print(StoreName + " has been removed")

# called when the user want to edit data already in the database
def editSomthing():
    print("\n(EU) -- Edit a user")
    print("(EP) -- Edit a product")
    print("(EL) -- Edit a list")
    print("(ES) -- Edit a store\n")
    
    selection = input("Select what to Edit: ").upper()

    if selection == "EU":
        print("Enter id of user to edit")
        id = input("Enter a id: ")
        attribute = input("Enter the attribute you want to change (first name, last name, street, number, city, zip, state): ").lower()
        newVal = input("Enter the new value: ")
        edit_user(id, attribute, newVal)
        print("User has been updated")

    elif selection == "EP":
        print("Enter id of product to edit")
        id = input("Enter a id: ")
        attribute = input("Enter the attribute you want to change (SKU, price, link, item name): ").lower()
        newVal = input("Enter the new value: ")
        edit_product(id, attribute, newVal)
        print("Product has been updated")

    elif selection == "EL":
        print("Enter id of list to edit")
        id = input("Enter a id: ")
        attribute = input("Enter the attribute you want to change (title): ").lower()
        newVal = input("Enter the new value: ")
        edit_product_list(id, attribute, newVal)
        print("List has been updated")

    elif selection == "ES":
        print("Enter id of store to edit")
        id = input("Enter a id: ")
        attribute = input("Enter the attribute you want to change (store name, URL, street, number, city, zip, state): ").lower()
        newVal = input("Enter the new value: ")
        edit_store(id, attribute, newVal)
        print("User has been updated")

# called when the user want to view data to the database
def viewStoredData():
    print("\n(VU) -- View a user")
    print("(VP) -- View a product")
    print("(VL) -- View a list")
    print("(VS) -- View a store\n")

    selection = input("Select what to see: ").upper()

    if selection == "VU":
        nextSelection = input("(name, all) Would you like to look up by name or view all users? ")
        if nextSelection == "name":
            name = input("Enter a last name: ")
            print(get_cust_by_name(name))
        elif nextSelection == "all":
            print(get_all_cust())

    elif selection == "VP":
        nextSelection = input("(name, all) Would you like to look up by name or view all products? ")
        if nextSelection == "name":
            name = input("Enter a product name: ")
            print(get_product_by_name(name))
        elif nextSelection == "all":
            print(get_all_product())

    elif selection == "VL":
        nextSelection = input("(title, all) Would you like to look up by title or view all lists? ")
        if nextSelection == "title":
            title = input("Enter a list title: ")
            print(get_list_by_title(title))
        elif nextSelection == "all":
            print(get_all_list())

    elif selection == "VS":
        nextSelection = input("(name, all) Would you like to look up by name or view all stores? ")
        if nextSelection == "name":
            name = input("Enter a store name: ")
            print(get_store_by_name(name))
        elif nextSelection == "all":
            print(get_all_store())

###########################################################################
######################## MAIN #############################################
###########################################################################
def main():
    print("Welcome to the shopping list")
    
    while(True):
        print()
        print("add somthing")
        print("remove somthing")
        print("edit somthing")
        print("view stored data\n")

        val = input("What would you like to do? ").lower()
        if val == "add somthing":
            addSomthing()
        elif val == "remove somthing":
            removeSomthing()
        elif val == "edit somthing":
            editSomthing()
        elif val == "view stored data":
            viewStoredData()
        else:
            print("\nInput, please try again")


if __name__ == "__main__":
    connect()
    # fill()
    main()
