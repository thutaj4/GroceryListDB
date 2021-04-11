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


def update_address(cust, city):
    with conn:
        c.execute("""UPDATE Customer SET city = :city
                    WHERE first = :first AND last = :last""",
                  {'first': cust.FirstName, 'last': cust.LastName, 'city': city})


def remove_cust(cust):
    with conn:
        c.execute("DELETE from Customer WHERE first = :first AND last = :last",
                  {'first': cust.FirstName, 'last': cust.LastName})


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


# def get_products_in_list(List_ID):
#     c.execute("SELECT * FROM ProductListHAS WHERE list_ID = {}".format(List_ID))
#     return c.fetchall()


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


###########################################################################
######################## MAIN #############################################
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

    customers = get_all_cust()
    stores = get_all_store()
    lists = get_all_list()
    products = get_all_product()

    # print(customers)
    # print(stores)
    # print(lists)
    # print(products)

    conn.close()
    print("DB Closed")

# called when the user want to add data to the database
def addSomthing():
    print("\n(AU) -- Add a user")
    print("(AP) -- Add a product")
    print("(AL) -- Add a list")
    print("(AS) -- Add a store")
    
    selection = input("Select what to add: ").upper()

# called when the user want to remove data to the database
def removeSomthing():
    print("\n(RU) -- Remove a user")
    print("(RP) -- Remove a product")
    print("(RL) -- Remove a list")
    print("(RS) -- Remove a store")
    
    selection = input("Select what to remove: ").upper()

# called when the user want to view data to the database
def viewStoredData():
    print("\n(VU) -- View a user")
    print("(VP) -- View a product")
    print("(VL) -- View a list")
    print("(VS) -- View a store")

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


def main():
    print("Welcome to the shopping list")
    
    while(True):
        print()
        print("add somthing")
        print("remove somthing")
        print("view stored data\n")

        val = input("What would you like to do? ").lower()
        if val == "add somthing":
            addSomthing()
        elif val == "remove somthing":
            removeSomthing()
        elif val == "view stored data":
            viewStoredData()
        else:
            print("\nInput, please try again")


if __name__ == "__main__":
    connect()
    # fill()
    main()
