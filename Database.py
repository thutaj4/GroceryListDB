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
######################## CREATE TABLES ####################################
###########################################################################
# def createTables():
#     try:
#         c.execute("""CREATE TABLE Customer (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                 first text,
#                 last text,
#                 houseNum text,
#                 street text,
#                 city text
#                 )""")
#         print("created customer table")
#     except:
#         print("error creating customer table")
#
#     try:
#         c.execute("""CREATE TABLE Store (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                 compName text,
#                 url text,
#                 buildingNum text,
#                 street text,
#                 city text
#                 )""")
#         print("created store table")
#     except:
#         print("error creating store table")
#
#     try:
#         c.execute("""CREATE TABLE Product_List (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                 title text,
#                 numItems int
#                 )""")
#         print("created Product_list table")
#     except:
#         print("error creating Product_list table")
#
#     try:
#         c.execute("""CREATE TABLE Product (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                 SKU text,
#                 price int,
#                 link int,
#                 item_name text,
#                 List_ID int
#                 )""")
#         print("created Product table")
#     except:
#         print("error creating Product table")


###########################################################################
######################## CUSTOMER METHODS #################################
###########################################################################
def insert_customer(cust):
    with conn:
        c.execute("INSERT INTO Customer VALUES (:CustomerID, :FirstName, :LastName, :Number, :Street, :City)",
                  {'CustomerID': None, 'FirstName': cust.FirstName, 'LastName': cust.LastName, 'Number': cust.HouseNum,
                   'Street': cust.Street, 'City': cust.City})


def get_cust_by_name(lastname):
    c.execute("SELECT * FROM Customer WHERE last=:last", {'last': lastname})
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
        c.execute("INSERT INTO Store VALUES (:id, :CompName, :url, :BuildingNum, :street, :city)",
                  {'id': None, 'CompName': store.CompName, 'url': store.URL, 'BuildingNum': store.BuildingNum,
                   'street': store.Street, 'city': store.City})


def get_all_store():
    c.execute("SELECT * FROM Store")
    return c.fetchall()


###########################################################################
######################## PROUCT LIST METHODS ##############################
###########################################################################


def insert_list(list):
    with conn:
        c.execute("INSERT INTO Product_List VALUES (:id, :Title, :NumItems)",
                  {'id': None, 'Title': list.Title, 'NumItems': list.NumItems})


def get_all_list():
    c.execute("SELECT * FROM Product_List")
    return c.fetchall()


def get_products_in_list(List_ID):
    c.execute("SELECT * FROM Product WHERE list_ID = {}".format(List_ID))
    return c.fetchall()


###########################################################################
######################## PRODUCT METHODS ##################################
###########################################################################
def insert_product(product):
    with conn:
        c.execute("INSERT INTO Product VALUES (:id, :SKU, :Price, :Link, :Item_Name, :List_ID)",
                  {'id': None, 'SKU': product.SKU, 'Price': product.Price, 'Link': product.Link,
                   'Item_Name': product.ItemName, 'List_ID': product.ListID})


def get_all_product():
    c.execute("SELECT * FROM Product")
    return c.fetchall()


###########################################################################
######################## MAIN #############################################
###########################################################################
def main():
    cust_1 = Customer('John', 'Doe', '12345', 'state street', 'la crosse')
    cust_2 = Customer('Jane', 'Doe', '111', 'state street', 'madison')
    cust_3 = Customer('Jim', 'Dolf', '1234', 'pine street', 'la crosse')

    insert_customer(cust_1)
    insert_customer(cust_2)
    insert_customer(cust_3)

    store_1 = Store('Festival', 'www.festival.com',
                    '333', 'lousy BLVD', 'lacrosse')
    store_2 = Store('Target', 'www.target.com', '323', 'streettt', 'lacrosse')

    insert_store(store_1)
    insert_store(store_2)

    list_1 = Product_List("shopping list", 0)
    list_2 = Product_List("wish list", 4)

    insert_list(list_1)
    insert_list(list_2)

    product_1 = Product("283YDGS", 29, "www.website.com", "t-shirt", 1)
    product_2 = Product("343YDGS", 100, "www.website.com", "t-shirt", 2)
    product_3 = Product("2586YDGS", 2, "www.website.com", "t-shirt", 51)
    product_4 = Product("sjdDGS", 23, "www.website.com", "t-shirt", 1)
    product_5 = Product("283Yeui8", 25, "www.website.com", "t-shirt", 19)
    product_6 = Product("2dhrudh74", 200, "www.website.com", "t-shirt", 1)

    insert_product(product_1)
    insert_product(product_2)
    insert_product(product_3)
    insert_product(product_4)
    insert_product(product_5)
    insert_product(product_6)

    # customers = get_cust_by_name('Doe')

    update_address(cust_3, 'Onalaska')
    # remove_cust(cust_1)
    # remove_cust(cust_1)
    # remove_cust(cust_3)

    # customers = get_cust_by_name('Doe')
    # print(customers)

    customers = get_all_cust()
    stores = get_all_store()
    lists = get_all_list()
    products = get_all_product()

    prods_in_1 = get_products_in_list(1)

    print(customers)
    print(stores)
    print(lists)
    print(products)
    print(prods_in_1)

    conn.close()


if __name__ == "__main__":
    connect()
    # main()
