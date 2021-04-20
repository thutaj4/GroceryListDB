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

    # insert cusomters
    cust_1 = Customer('John', 'Doe', 'state street',
                      '1234', 'la crosse', '54601', 'WI')
    cust_2 = Customer('Jane', 'Duh', 'pine street',
                      '333', 'la crosse', '54601', 'WI')
    cust_3 = Customer('Tim', 'Doe', 'state street',
                      '1234', 'la crosse', '54601', 'WI')
    cust_4 = Customer('Timmy', 'Kim', '12th street',
                      '1212', 'la crosse', '54603', 'WI')
    cust_5 = Customer('Jack', 'Bates', 'north street',
                      '111', 'Chicago', '44201', 'IL')
    cust_6 = Customer('Kim', 'Danny', 'tall street',
                      '757', 'Chicago', '44201', 'IL')
    cust_7 = Customer('Timmy', 'Anderson', '100th street',
                      '344', 'Chicago', '44201', 'IL')
    cust_8 = Customer('Timmy', 'Kim', '12th street',
                      '1212', 'la crosse', '54603', 'WI')
    cust_9 = Customer('Dan', 'Wilber', 'cane rd',
                      '1253', 'Dallas', '34832', 'TX')
    cust_10 = Customer('Zane', 'Collin', '3rd street',
                      '989', 'Dallas', '34832', 'TX')
    cust_11 = Customer('Kathy', 'Dug', 'Miller street',
                      '1234', 'Philadelphia', '32342', 'PA')
    cust_12 = Customer('Lily', 'Kim', 'Gold rd',
                      '1212', 'Philadelphia', '32342', 'PA')
    cust_13 = Customer('John', 'Smith', 'State street',
                      '122', 'Philadelphia', '32342', 'PA')
    cust_14 = Customer('Jim', 'Ekler', 'Smith street',
                      '333', 'Phoenix', '90231', 'AZ')
    cust_15 = Customer('Tim', 'Quin', 'Enderway Circle',
                      '1212', 'Phoenix', '90231', 'AZ')
    cust_16 = Customer('Cammy', 'Kim', '12th street',
                      '892', 'Phoenix', '90231', 'AZ')
    cust_17 = Customer('John', 'Andrew', 'Terner road',
                      '124', 'Houston', '65743', 'TX')
    cust_18 = Customer('Kate', 'Don', 'Pine street',
                      '8767', 'Houston', '65743', 'TX')
    cust_19 = Customer('Timmy', 'Gil', '12th street',
                      '876', 'Houston', '65743', 'TX')
    cust_20 = Customer('Ron', 'Fern', '1st street',
                      '555', 'Houston', '65743', 'TX')
    cust_21 = Customer('mMat', 'Andrew', 'smith road',
                      '1645', 'Houston', '65743', 'TX')
    cust_22 = Customer('Kind', 'Don', 'Pine street',
                      '454', 'Houston', '65743', 'TX')
    cust_23 = Customer('Hof', 'Gil', '12th street',
                      '4545', 'Houston', '65743', 'TX')
    cust_24 = Customer('Quincy', 'Fern', '1st street',
                      '5556', 'Houston', '65743', 'TX')

    # insert_customer(cust_1)
    # insert_customer(cust_2)
    # insert_customer(cust_3)
    # insert_customer(cust_4)
    # insert_customer(cust_5)
    # insert_customer(cust_6)
    # insert_customer(cust_7)
    # insert_customer(cust_8)
    # insert_customer(cust_9)
    # insert_customer(cust_10)
    # insert_customer(cust_11)
    # insert_customer(cust_12)
    # insert_customer(cust_13)
    # insert_customer(cust_14)
    # insert_customer(cust_15)
    # insert_customer(cust_16)
    # insert_customer(cust_17)
    # insert_customer(cust_18)
    # insert_customer(cust_19)
    # insert_customer(cust_20)
    # insert_customer(cust_21)
    # insert_customer(cust_22)
    # insert_customer(cust_23)
    # insert_customer(cust_24)

    # insert stores
    store_1 = Store('Festival', 'www.festival.com',
                    'Lousy BLVD', '232', 'La Crosse', '54601', 'WI')
    store_2 = Store('Target', 'www.target.com',
                    'County highway m', '1112', 'Onalaska', '54603', 'WI')
    store_3 = Store('Walmart', 'www.walmart.com',
                    'Main street', '2343', 'Onalaska', '54603', 'WI')
    store_4 = Store('Walmart', 'www.walmart.com',
                    '2nd street', '122', 'Onalaska', '54603', 'WI')
    store_5 = Store('Walmart', 'www.walmart.com',
                    'County highway y', '212', 'Dallas', '34832', 'TX')
    store_6 = Store('Target', 'www.target.com',
                    'Shimer road', '124', 'Dallas', '34832', 'TX')
    store_7 = Store('Walgreens', 'www.walgreens.com',
                    'Main street', '768', 'Dallas', '34832', 'TX')
    store_8 = Store('Walgreens', 'www.walgreens.com',
                    '3rd st', '234', 'Dallas', '34832', 'TX')
    store_9 = Store('Target', 'www.target.com',
                    'Big road', '334', 'Phoenix', '90231', 'AZ')
    store_10 = Store('Target', 'www.target.com',
                    'North curve road', '7667', 'Phoenix', '90231', 'AZ')
    store_11 = Store('Walmart', 'www.walmart.com',
                    'Woods street', '999', 'Phoenix', '90231', 'AZ')

    # insert_store(store_1)
    # insert_store(store_2)
    # insert_store(store_3)
    # insert_store(store_4)
    # insert_store(store_5)
    # insert_store(store_6)
    # insert_store(store_7)
    # insert_store(store_8)
    # insert_store(store_9)
    # insert_store(store_10)
    # insert_store(store_11)

    # insert lists
    list_1 = Product_List("shopping list")
    list_2 = Product_List("wish list")
    list_3 = Product_List("new list")
    list_4 = Product_List("my list")
    list_5 = Product_List("grocery list")
    list_6 = Product_List("food list")
    list_7 = Product_List("needs")
    list_8 = Product_List("wish list")
    list_9 = Product_List("chistmas list")
    list_10 = Product_List("items")
    list_11 = Product_List("clothes wants")
    list_12 = Product_List("need to buy")
    list_13 = Product_List("shopping list")
    list_14 = Product_List("second list")
    list_15 = Product_List("wants list")
    list_16 = Product_List("need to find list")
    list_17 = Product_List("shopping list")
    list_18 = Product_List("grocerys")
    list_19 = Product_List("grocery list")
    list_20 = Product_List("buy next week")
    list_21 = Product_List("products list")
    list_22 = Product_List("wish list")
    list_23 = Product_List("shopping list")
    list_24 = Product_List("wants")
    list_25 = Product_List("everything list")
    list_26 = Product_List("please buy list")

    # insert_list(list_1)
    # insert_list(list_2)
    # insert_list(list_3)
    # insert_list(list_4)
    # insert_list(list_5)
    # insert_list(list_5)
    # insert_list(list_6)
    # insert_list(list_7)
    # insert_list(list_8)
    # insert_list(list_9)
    # insert_list(list_10)
    # insert_list(list_11)
    # insert_list(list_12)
    # insert_list(list_13)
    # insert_list(list_14)
    # insert_list(list_15)
    # insert_list(list_16)
    # insert_list(list_17)
    # insert_list(list_18)
    # insert_list(list_19)
    # insert_list(list_20)
    # insert_list(list_21)
    # insert_list(list_22)
    # insert_list(list_23)
    # insert_list(list_24)
    # insert_list(list_23)
    # insert_list(list_24)
    # insert_list(list_25)
    # insert_list(list_26)

    # insert products
    product_1 = Product("283YDGS", 29.00, "www.paper.com", "paper")
    product_2 = Product("343YDGS", 100.00, "www.shirt.com", "t-shirt")
    product_3 = Product("2586YDGS", 2.99, "www.pen.com", "pen")
    product_4 = Product("sjdDGS", 23.99, "www.pants.com", "pants")
    product_5 = Product("283Yeui8", 25.00, "www.xbox.com", "xbox live")
    product_6 = Product("2dhrudh74", 200.00, "www.hoodie.com", "hoodie")
    product_7 = Product("345334", 29.00, "www.jeans.com", "jeans")
    product_8 = Product("3435464", 150.00, "www.backpack.com", "backpack")
    product_9 = Product("645657", 0.99, "www.orange.com", "orange")
    product_10 = Product("345v3vg", 23.99, "www.pants.com", "pants")
    product_11 = Product("45gg545", 27.00, "www.lobster.com", "lobster tail")
    product_12 = Product("45gvg56g", 2000.00, "www.laptop.com", "laptop")
    product_13 = Product("46b653", 23.00, "www.website.com", "ribs")
    product_14 = Product("453gv5", 160.00, "www.glasses.com", "sun glasses")
    product_15 = Product("4566bh3", 4.99, "www.chips.com", "chips")
    product_16 = Product("3465bg3", 23.99, "www.steak.com", "steak")
    product_17 = Product("345gb6", 25.00, "www.gift.com", "apple gift card")
    product_18 = Product("7654675", 201.05, "www.wallet.com", "wallet")
    product_19 = Product("345gg", 29.99, "www.meat.com", "meat")
    product_20 = Product("46hb6", 100.00, "www.shirt.com", "t-shirt")
    product_21 = Product("46hb36", 2.99, "www.Coke.com", "Coke bottle")
    product_22 = Product("36b67757", 27.99, "www.mouse.com", "mouse")
    product_23 = Product("46b6b55", 25.50, "www.apples.com", "apples")
    product_24 = Product("4567b75", 75.00, "www.jeans.com", "jeans")
    product_25 = Product("457gb7", 59.00, "www.bricks.com", "bricks")
    product_26 = Product("345gvg", 29.70, "www.stand.com", "tv stand")
    product_27 = Product("jh7567", 27.99, "www.shirt.com", "t-shirt")
    product_28 = Product("ty67575", 1.99, "www.straws.com", "straws")
    product_29 = Product("647657", 450.00, "www.website.com", "phone")
    product_30 = Product("678b675", 400.00, "www.phone.com", "phone")
    product_31 = Product("45346ff", 29.70, "www.website.com", "tv stand")
    product_32 = Product("f4354", 7.99, "www.tuna.com", "tuna")
    product_33 = Product("f3465654", 1.99, "www.beef.com", "beef jerky")
    product_34 = Product("45365", 4.00, "www.cofee.com", "cofee")
    product_35 = Product("234532", 4.00, "www.lemon.com", "lemon")

    # insert_product(product_1)
    # insert_product(product_2)
    # insert_product(product_3)
    # insert_product(product_4)
    # insert_product(product_5)
    # insert_product(product_6)
    # insert_product(product_7)
    # insert_product(product_8)
    # insert_product(product_9)
    # insert_product(product_10)
    # insert_product(product_11)
    # insert_product(product_12)
    # insert_product(product_13)
    # insert_product(product_14)
    # insert_product(product_15)
    # insert_product(product_16)
    # insert_product(product_17)
    # insert_product(product_18)
    # insert_product(product_19)
    # insert_product(product_20)
    # insert_product(product_21)
    # insert_product(product_22)
    # insert_product(product_23)
    # insert_product(product_24)
    # insert_product(product_25)
    # insert_product(product_26)
    # insert_product(product_27)
    # insert_product(product_28)
    # insert_product(product_29)
    # insert_product(product_30)
    # insert_product(product_31)
    # insert_product(product_32)
    # insert_product(product_33)
    # insert_product(product_34)
    # insert_product(product_35)

    # assign customers lists
    # insert_customerHAS(1, 1)
    # insert_customerHAS(2, 2)
    # insert_customerHAS(2, 31)
    # insert_customerHAS(2, 32)
    # insert_customerHAS(3, 3)
    # insert_customerHAS(4, 4)
    # insert_customerHAS(5, 5)
    # insert_customerHAS(5, 6)
    # insert_customerHAS(5, 7)
    # insert_customerHAS(6, 8)
    # insert_customerHAS(7, 9)
    # insert_customerHAS(8, 10)
    # insert_customerHAS(8, 11)
    # insert_customerHAS(9, 12)
    # insert_customerHAS(10, 13)
    # insert_customerHAS(12, 14)
    # insert_customerHAS(12, 15)
    # insert_customerHAS(13, 16)
    # insert_customerHAS(14, 17)
    # insert_customerHAS(15, 18)
    # insert_customerHAS(15, 28)
    # insert_customerHAS(15, 29)
    # insert_customerHAS(15, 30)
    # insert_customerHAS(16, 19)
    # insert_customerHAS(17, 20)
    # insert_customerHAS(19, 21)
    # insert_customerHAS(20, 22)
    # insert_customerHAS(24, 23)
    # insert_customerHAS(24, 24)
    # insert_customerHAS(24, 26)
    # insert_customerHAS(24, 27)

    # # insert customer order history
    # insert_customerPURCHASED(1, 1, '12/3/2020')
    # insert_customerPURCHASED(1, 4, '11/3/2020')
    # insert_customerPURCHASED(1, 14, '1/7/2020')
    # insert_customerPURCHASED(1, 2, '12/7/2020')
    # insert_customerPURCHASED(1, 5, '12/5/2020')
    # insert_customerPURCHASED(2, 21, '1/30/2020')
    # insert_customerPURCHASED(2, 30, '2/23/2020')
    # insert_customerPURCHASED(2, 1, '2/31/2020')
    # insert_customerPURCHASED(2, 4, '11/22/2020')
    # insert_customerPURCHASED(2, 5, '2/3/2020')
    # insert_customerPURCHASED(5, 6, '5/30/2020')
    # insert_customerPURCHASED(5, 7, '2/2/2020')
    # insert_customerPURCHASED(5, 16, '6/1/2020')
    # insert_customerPURCHASED(7, 1, '6/9/2020')
    # insert_customerPURCHASED(7, 9, '3/5/2020')
    # insert_customerPURCHASED(7, 20, '4/6/2020')
    # insert_customerPURCHASED(9, 15, '1/7/2020')
    # insert_customerPURCHASED(9, 13, '12/3/2020')
    # insert_customerPURCHASED(9, 12, '12/8/2020')
    # insert_customerPURCHASED(9, 18, '1/4/2020')
    # insert_customerPURCHASED(11, 1, '5/12/2020')
    # insert_customerPURCHASED(11, 3, '5/14/2020')
    # insert_customerPURCHASED(11, 31, '6/3/2020')
    # insert_customerPURCHASED(11, 7, '7/3/2020')
    # insert_customerPURCHASED(11, 8, '12/6/2020')
    # insert_customerPURCHASED(11, 9, '1/4/2020')
    # insert_customerPURCHASED(12, 10, '2/3/2020')
    # insert_customerPURCHASED(13, 14, '1/7/2020')
    # insert_customerPURCHASED(16, 21, '12/6/2020')
    # insert_customerPURCHASED(16, 31, '5/6/2020')
    # insert_customerPURCHASED(19, 32, '10/6/2020')
    # insert_customerPURCHASED(19, 11, '6/7/2020')
    # insert_customerPURCHASED(19, 10, '4/4/2020')
    # insert_customerPURCHASED(19, 15, '6/23/2020')
    # insert_customerPURCHASED(21, 19, '7/23/2020')
    # insert_customerPURCHASED(21, 1, '7/26/2020')
    # insert_customerPURCHASED(21, 5, '3/31/2020')
    # insert_customerPURCHASED(21, 6, '2/6/2020')
    # insert_customerPURCHASED(22, 7, '12/19/2020')
    # insert_customerPURCHASED(23, 3, '1/23/2020')

    # # insert items into lists
    # insert_productListHAS(1, 1)
    # insert_productListHAS(1, 2)
    # insert_productListHAS(1, 3)
    # insert_productListHAS(1, 4)
    # insert_productListHAS(1, 5)
    # insert_productListHAS(3, 2)
    # insert_productListHAS(3, 1)
    # insert_productListHAS(3, 2)
    # insert_productListHAS(4, 1)
    # insert_productListHAS(4, 2)
    # insert_productListHAS(5, 1)
    # insert_productListHAS(6, 2)
    # insert_productListHAS(7, 1)
    # insert_productListHAS(7, 23)
    # insert_productListHAS(7, 6)
    # insert_productListHAS(7, 8)
    # insert_productListHAS(8, 8)
    # insert_productListHAS(8, 28)
    # insert_productListHAS(8, 30)
    # insert_productListHAS(8, 21)
    # insert_productListHAS(8, 15)
    # insert_productListHAS(10, 12)
    # insert_productListHAS(10, 17)
    # insert_productListHAS(10, 20)
    # insert_productListHAS(10, 13)
    # insert_productListHAS(10, 27)
    # insert_productListHAS(11, 1)
    # insert_productListHAS(12, 2)
    # insert_productListHAS(13, 2)
    # insert_productListHAS(13, 23)
    # insert_productListHAS(14, 6)
    # insert_productListHAS(15, 8)
    # insert_productListHAS(15, 2)
    # insert_productListHAS(15, 27)
    # insert_productListHAS(15, 18)
    # insert_productListHAS(15, 21)
    # insert_productListHAS(15, 15)
    # insert_productListHAS(15, 18)
    # insert_productListHAS(15, 17)
    # insert_productListHAS(16, 20)
    # insert_productListHAS(16, 12)
    # insert_productListHAS(16, 27)
    # insert_productListHAS(18, 6)
    # insert_productListHAS(18, 8)
    # insert_productListHAS(18, 2)
    # insert_productListHAS(18, 27)
    # insert_productListHAS(18, 13)
    # insert_productListHAS(18, 21)
    # insert_productListHAS(19, 15)
    # insert_productListHAS(19, 12)
    # insert_productListHAS(19, 17)
    # insert_productListHAS(21, 28)
    # insert_productListHAS(21, 13)
    # insert_productListHAS(21, 27)
    # insert_productListHAS(22, 8)
    # insert_productListHAS(22, 27)
    # insert_productListHAS(22, 12)
    # insert_productListHAS(22, 21)
    # insert_productListHAS(20, 15)
    # insert_productListHAS(20, 18)
    # insert_productListHAS(20, 17)
    # insert_productListHAS(12, 20)
    # insert_productListHAS(12, 12)
    # insert_productListHAS(12, 27)
    # insert_productListHAS(13, 28)
    # insert_productListHAS(13, 13)
    # insert_productListHAS(23, 27)

    # # insert product that stores sell
    # insert_storeSELLS(1, 1)
    # insert_storeSELLS(1, 5)
    # insert_storeSELLS(1, 2)
    # insert_storeSELLS(1, 3)
    # insert_storeSELLS(1, 6)
    # insert_storeSELLS(1, 12)
    # insert_storeSELLS(1, 2)
    # insert_storeSELLS(1, 23)
    # insert_storeSELLS(1, 14)
    # insert_storeSELLS(1, 6)
    # insert_storeSELLS(1, 1)
    # insert_storeSELLS(1, 7)
    # insert_storeSELLS(1, 1)
    # insert_storeSELLS(1, 2)
    # insert_storeSELLS(2, 1)
    # insert_storeSELLS(2, 3)
    # insert_storeSELLS(2, 14)
    # insert_storeSELLS(2, 6)
    # insert_storeSELLS(2, 1)
    # insert_storeSELLS(2, 7)
    # insert_storeSELLS(2, 1)
    # insert_storeSELLS(2, 9)
    # insert_storeSELLS(2, 1)
    # insert_storeSELLS(2, 2)
    # insert_storeSELLS(2, 14)
    # insert_storeSELLS(2, 1)
    # insert_storeSELLS(2, 3)
    # insert_storeSELLS(3, 1)
    # insert_storeSELLS(3, 5)
    # insert_storeSELLS(3, 6)
    # insert_storeSELLS(3, 1)
    # insert_storeSELLS(3, 1)
    # insert_storeSELLS(3, 2)
    # insert_storeSELLS(3, 5)
    # insert_storeSELLS(3, 1)
    # insert_storeSELLS(3, 31)
    # insert_storeSELLS(3, 6)
    # insert_storeSELLS(3, 7)
    # insert_storeSELLS(3, 1)
    # insert_storeSELLS(3, 14)
    # insert_storeSELLS(3, 5)
    # insert_storeSELLS(4, 1)
    # insert_storeSELLS(4, 2)
    # insert_storeSELLS(4, 23)
    # insert_storeSELLS(4, 3)
    # insert_storeSELLS(4, 1)
    # insert_storeSELLS(4, 9)
    # insert_storeSELLS(4, 6)
    # insert_storeSELLS(4, 1)
    # insert_storeSELLS(4, 3)
    # insert_storeSELLS(4, 7)
    # insert_storeSELLS(4, 1)
    # insert_storeSELLS(5, 5)
    # insert_storeSELLS(5, 1)
    # insert_storeSELLS(5, 2)
    # insert_storeSELLS(5, 12)
    # insert_storeSELLS(5, 6)
    # insert_storeSELLS(5, 1)
    # insert_storeSELLS(5, 2)
    # insert_storeSELLS(5, 1)
    # insert_storeSELLS(5, 23)
    # insert_storeSELLS(5, 1)
    # insert_storeSELLS(6, 6)
    # insert_storeSELLS(6, 12)
    # insert_storeSELLS(6, 3)
    # insert_storeSELLS(6, 1)
    # insert_storeSELLS(6, 5)
    # insert_storeSELLS(6, 2)
    # insert_storeSELLS(6, 14)
    # insert_storeSELLS(6, 6)
    # insert_storeSELLS(6, 1)
    # insert_storeSELLS(6, 9)
    # insert_storeSELLS(6, 1)
    # insert_storeSELLS(7, 23)
    # insert_storeSELLS(7, 9)
    # insert_storeSELLS(7, 1)
    # insert_storeSELLS(7, 3)
    # insert_storeSELLS(7, 1)
    # insert_storeSELLS(7, 5)
    # insert_storeSELLS(7, 23)
    # insert_storeSELLS(7, 1)
    # insert_storeSELLS(7, 9)
    # insert_storeSELLS(7, 6)
    # insert_storeSELLS(8, 3)
    # insert_storeSELLS(8, 12)
    # insert_storeSELLS(8, 5)
    # insert_storeSELLS(8, 2)
    # insert_storeSELLS(8, 3)
    # insert_storeSELLS(8, 1)
    # insert_storeSELLS(8, 6)
    # insert_storeSELLS(8, 23)
    # insert_storeSELLS(8, 5)
    # insert_storeSELLS(8, 9)
    # insert_storeSELLS(8, 1)
    # insert_storeSELLS(8, 6)
    # insert_storeSELLS(8, 23)
    # insert_storeSELLS(9, 5)
    # insert_storeSELLS(9, 2)
    # insert_storeSELLS(9, 14)
    # insert_storeSELLS(9, 1)
    # insert_storeSELLS(9, 6)
    # insert_storeSELLS(9, 23)
    # insert_storeSELLS(9, 1)
    # insert_storeSELLS(10, 5)
    # insert_storeSELLS(10, 1)
    # insert_storeSELLS(10, 2)
    # insert_storeSELLS(10, 1)
    # insert_storeSELLS(10, 6)
    # insert_storeSELLS(10, 23)
    # insert_storeSELLS(10, 9)
    # insert_storeSELLS(10, 1)
    # insert_storeSELLS(10, 6)
    # insert_storeSELLS(10, 16)
    # insert_storeSELLS(10, 1)
    # insert_storeSELLS(10, 12)
    # insert_storeSELLS(10, 18)
    # insert_storeSELLS(10, 5)
    # insert_storeSELLS(11, 1)
    # insert_storeSELLS(11, 6)
    # insert_storeSELLS(11, 9)
    # insert_storeSELLS(11, 1)
    # insert_storeSELLS(11, 5)

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

def get_cust_id(FirstName, LastName, Street, Number, City, Zip, State):
    c.execute("""SELECT CustomerID FROM Customer 
    WHERE FirstName=:FirstName AND LastName=:LastName AND Street=:Street AND Number=:Number AND City=:City AND Zip=:Zip AND State=:State""",
     {'FirstName': FirstName, 'LastName': LastName, 'Street': Street, 'Number': Number, 'City': City, 'Zip': Zip, 'State': State})
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

def remove_cust(id):
    with conn:
        c.execute("DELETE from Customer WHERE CustomerID = :CustomerID",
                  {'CustomerID': id})

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

def remove_store(id):
    with conn:
        c.execute("DELETE from Store WHERE StoreID = :StoreID", {'StoreID': id})

def remove_store_from_storeSELLS(id):
    with conn:
        c.execute("DELETE from StoreSELLS WHERE StoreID = :StoreID", {'StoreID': id})

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

def get_list_id(Title):
    c.execute("SELECT ProductListID FROM ProductList WHERE Title=:Title", {'Title': Title})
    return c.fetchall()

def edit_product_list(id, attribute, newVal):
    if attribute == "title":
        with conn:
            c.execute("UPDATE ProductList SET Title = :Title WHERE ProductListID = :ProductListID",
             {'Title': newVal, 'ProductListID': id})

def remove_product_list(id):
    with conn:
            c.execute("DELETE from ProductList WHERE ProductListID = :ProductListID", {'ProductListID': id})

def remove_product_list_from_custHAS(id):
    with conn:
            c.execute("DELETE from CustomerHAS WHERE ProductListID = :ProductListID", {'ProductListID': id})

def remove_product_list_from_prodListHAS(id):
    with conn:
            c.execute("DELETE from ProductListHAS WHERE ProductListID = :ProductListID", {'ProductListID': id})

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

def get_product_id(sku, price, link, itemName):
    c.execute("SELECT ProductID FROM Product WHERE SKU=:SKU AND Price=:Price AND Link=:Link AND ItemName=:ItemName", {'SKU': sku, 'Price': price, 'Link': link, 'ItemName': itemName})
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

def remove_product(id):
    with conn:
        c.execute("DELETE from Product WHERE ProductId = :ProductId", {'ProductId': id})

def remove_prod_from_custPurch(id):
    with conn:
        c.execute("DELETE from CustomerPURCHASED WHERE ProductId = :ProductId", {'ProductId': id})

def remove_product_from_list(id):
    with conn:
        c.execute("DELETE from ProductListHas WHERE ProductId = :ProductId", {'ProductId': id})
    
def remove_prod_from_storeSells(id):
    with conn:
        c.execute("DELETE from StoreSELLS WHERE ProductId = :ProductId", {'ProductId': id})
###########################################################################
######################## CustomerHAS methods ##############################
###########################################################################

def insert_customerHAS(custID, listID):
    with conn:
        c.execute("INSERT INTO CustomerHAS VALUES (:CustomerID, :ProductListID)",
                  {'CustomerID': custID, 'ProductListID': listID})

def get_all_cust_list():
    with conn:
        c.execute("SELECT FirstName, LastName, Title FROM Customer NATURAL JOIN CustomerHAS NATURAL JOIN ProductList")
        return c.fetchall()

def get_cust_list(custID):
    with conn:
        c.execute("SELECT Title FROM Customer NATURAL JOIN CustomerHAS NATURAL JOIN ProductList WHERE CustomerID = {}".format(custID))
        return c.fetchall()

def remove_cust_from_custHas(id):
    with conn:
        c.execute("DELETE from CustomerHAS WHERE CustomerID = :CustomerID",
                  {'CustomerID': id})
###########################################################################
######################## CustomerPURCHASED methods ##############################
###########################################################################

def insert_customerPURCHASED(custID, prodID, date):
    with conn:
        c.execute("INSERT INTO CustomerPURCHASED VALUES (:CustomerID, :ProductID, :Date)",
                  {'CustomerID': custID, 'ProductID': prodID, 'Date': date})

def get_all_cust_purch():
    with conn:
        c.execute("SELECT FirstName, LastName, ItemName, Date FROM Customer NATURAL JOIN CustomerPURCHASED NATURAL JOIN Product")
        return c.fetchall()

def get_cust_purch(custID):
    with conn:
        c.execute("SELECT ItemName, Date FROM Customer NATURAL JOIN CustomerPURCHASED NATURAL JOIN Product WHERE CustomerID = {}".format(custID))
        return c.fetchall()

def remove_cust_from_custPurch(id):
    with conn:
        c.execute("DELETE from CustomerPURCHASED WHERE CustomerID = :CustomerID",
                  {'CustomerID': id})
###########################################################################
######################## ProductListHAS methods ##############################
###########################################################################

def insert_productListHAS(listID, prodID):
    with conn:
        c.execute("INSERT INTO ProductListHAS VALUES (:ProductListID, :ProductID)",
                  {'ProductListID': listID, 'ProductID': prodID})

def get_all_list_prods():
    with conn:
        c.execute("SELECT Title, ItemName FROM ProductList NATURAL JOIN ProductListHAS NATURAL JOIN Product")
        return c.fetchall()

def get_list_prods(custID):
    with conn:
        c.execute("SELECT ItemName FROM Customer NATURAL JOIN CustomerHAS NATURAL JOIN ProductList NATURAL JOIN ProductListHAS NATURAL JOIN Product WHERE CustomerID = {}".format(custID))
        return c.fetchall()


###########################################################################
######################## StoreSELLS methods ##############################
###########################################################################

def insert_storeSELLS(storeID, prodID):
    with conn:
        c.execute("INSERT INTO StoreSELLS VALUES (:StoreID, :ProductID)",
                  {'StoreID': storeID, 'ProductID': prodID})

def get_all_store_sells():
    with conn:
        c.execute("SELECT StoreName, ItemName FROM Product NATURAL JOIN StoreSELLS NATURAL JOIN STORE")
        return c.fetchall()

def get_store_sells(storeID):
    with conn:
        c.execute("SELECT ItemName, Price FROM Product NATURAL JOIN StoreSELLS NATURAL JOIN STORE WHERE StoreID = {}".format(storeID))
        return c.fetchall()

###########################################################################
######################## Advanced Queries ##############################
###########################################################################

# get the stores ID, name, and URL for the stoes whos name start with a W, order by the store name
def advanced1(x):
    with conn:
        c.execute("""
        SELECT StoreID, StoreName, URL 
        FROM Store 
        WHERE StoreName LIKE '{}%' ORDER BY StoreName""".format(x))
        return c.fetchall()

# gets customers and their order count with more than 2 orders, sorted by most to fewest orders
def advanced2(n):
    with conn:
        c.execute("""
        SELECT FirstName, LastName, Count(*)
        FROM Customer NATURAL JOIN CustomerPURCHASED NATURAL JOIN Product
        GROUP BY CustomerID 
        HAVING Count(*) > {} ORDER BY Count(*) DESC""".format(n))
        return c.fetchall()

# select all the First name, last name, and total spening amount for every cutomer from a given state who spent less then average from all states
def advanced3(s):
    with conn:
        c.execute("""
        SELECT FirstName, LastName, sum(Price) AS Total 
        FROM Customer NATURAL JOIN CustomerPURCHASED NATURAL JOIN Product 
        GROUP BY CustomerID
        HAVING State = "{}" AND Total < avg((SELECT sum(Price) AS Cost FROM Customer NATURAL JOIN CustomerPURCHASED NATURAL JOIN Product GROUP BY CustomerID))""".format(s))
        return c.fetchall()

def advanced4():
    with conn:
        c.execute("")
        return c.fetchall()

def advanced5():
    with conn:
        c.execute("")
        return c.fetchall()

def advanced6():
    with conn:
        c.execute("SELECT StoreName, ItemName FROM Product NATURAL JOIN StoreSELLS NATURAL JOIN STORE")
        return c.fetchall()

###########################################################################
######################## USER INPUT #######################################
###########################################################################

# called when the user want to add data to the database
def addSomthing():
    print("\n(AU) -- Add a user")
    print("(AP) -- Add a product")
    print("(AL) -- Add a list")
    print("(APL) -- Add a product to list")
    print("(APO) -- Add a product to order history")
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
        enterRel = input("would you like to set the store that sells this product? (y, n) ")
        if(enterRel == 'y'):
            ID = get_product_id(SKU, Price, Link, ItemName)
            prodID = ID[0][0]
            storeID = input("Enter store ID ")
            insert_storeSELLS(storeID, prodID)
        print(ItemName + " has been added")

    elif selection == "AL":
        Title = input("Enter a title: ")
        list = Product_List(Title)
        insert_list(list)
        enterRel = input("would you like to associate a cutomer with this list? (y, n) ")
        if(enterRel == 'y'):
            ID = get_list_id(Title)
            listID = ID[0][0]
            custID = input("Enter customer ID ")
            insert_customerHAS(custID, listID)
        print(Title + " has been added")

    elif selection == "APL":
        listID = input("Enter list ID for the list ")
        prodID = input("Enter product ID for the product ")
        insert_productListHAS(listID, prodID)
        print("Product has been added to the list")

    elif selection == "APO":
        custID = input("Enter customer ID for the customer ")
        prodID = input("Enter product ID for the product ")
        date = input("Enter the date of purchase ")
        insert_customerPURCHASED(custID, prodID, date)
        print("Product has been added to the order history")

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
        print("Enter id of user to remove")
        id = input("Enter a id: ")
        remove_cust(id)
        remove_cust_from_custHas(id)
        remove_cust_from_custPurch(id)
        print(id + " has been removed")

    elif selection == "RP":
        print("Enter id of item to remove")
        id = input("Enter a id: ")
        remove_product(id)
        remove_product_from_list(id)
        remove_prod_from_custPurch(id)
        remove_prod_from_storeSells(id)
        print(id + " has been removed")

    elif selection == "RL":
        print("Enter id of list to remove")
        ID = input("Enter a id: ")
        remove_product_list(ID)
        remove_product_list_from_custHAS(ID)
        remove_product_list_from_prodListHAS(ID)
        print(ID + " has been removed")
        
    elif selection == "RS":
        print("Enter id of store to remove")
        ID = input("Enter a id: ")
        remove_store(ID)
        remove_store_from_storeSELLS(ID)
        print(ID + " has been removed")

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
    print("(VS) -- View a store")
    print("(VCL) -- View customer's lists")
    print("(VIL) -- View all Items in lists")
    print("(VSP) -- View all store's products")
    print("(VCH) -- View customer's order history\n")

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
    elif selection == "VCL":
        choice = input("Enter a customer id to view their lists, or ALL to view all the customer's lists ").lower()
        if choice == 'all':
            print(get_all_cust_list())
        else:
            print(get_cust_list(choice))
    elif selection == "VIL":
        choice = input("Enter a customer id to view their list items, or ALL to view all the list's items ").lower()
        if choice == 'all':
            print(get_all_list_prods())
        else:
            print(get_list_prods(choice))
    elif selection == "VSP":
        choice = input("Enter a store id to view its products, or ALL to view all the stores inventory ").lower()
        if choice == 'all':
            print(get_all_store_sells())
        else:
            print(get_store_sells(choice))
    elif selection == "VCH":
        choice = input("Enter a customer id to view their history, or ALL to view all the customer's history ").lower()
        if choice == 'all':
            print(get_all_cust_purch())
        else:
            print(get_cust_purch(choice))

# called when the user wants to call complex queries

def otherQueries():
    print("(Q1) -- Get the store ID, name, and URL for the stoes whos name start with x, order by the store name\n")
    print("(Q2) -- Get customers and their order count with more than n orders, sorted by most to fewest orders\n")
    print("(Q3) -- Get every cutomer from a given state who spent less then average from all states\n")
    print("(Q4) -- View customer's lists who have more then 3 items from Target\n")
    print("(Q5) -- View customer's lists who have more then 3 items from Target\n")
    print("(Q6) -- View customer's lists who have more then 3 items from Target\n")

    selection = input("Select what to see: ").upper()

    if selection == 'Q1':
        x = input("Enter x: ")
        print(advanced1(x))
    elif selection == 'Q2':
        n = input("Enter n: ")
        print(advanced2(n))
    elif selection == 'Q3':
        s = input("Enter s (TX): ")
        print(advanced3(s))
    elif selection == 'Q4':
        print(advanced4())
    elif selection == 'Q5':
        print(advanced5())
    elif selection == 'Q6':
        print(advanced6())
    else :
        print("Not a valid selection")


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
        print("view stored data")
        print("other\n")

        val = input("What would you like to do? ").lower()
        if val == "add somthing":
            addSomthing()
        elif val == "remove somthing":
            removeSomthing()
        elif val == "edit somthing":
            editSomthing()
        elif val == "view stored data":
            viewStoredData()
        elif val == "other":
            otherQueries()
        else:
            print("\nInput, please try again")


if __name__ == "__main__":
    connect()
    # fill()
    main()
