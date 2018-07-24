import mysql.connector as mariadb

def dispContractorDetails():
    #open database connection
    db = mariadb.connect(host='localhost', database='construction', user='root', password = 'groot')
    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #function to display all items
    sql = "SELECT * FROM contractor"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            count+=1
            name = row[0]
            houseType = row[1]
            locality = row[2]
            price = row[3]
            print(str(count)+" : name=%s, house type=%s, locality=%s, price=%s" % (name,houseType,locality,price))
    except:
        print("unable to fetch data")
    input("Press enter to continue...")


def dispDealerDetails():
    #open database connection
    db = mariadb.connect(host='localhost', database='construction', user='root', password = 'groot')
    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #function to display all items
    sql = "SELECT * FROM dealer"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            count+=1
            name = row[0]
            itemName = row[1]
            stock = row[2]
            price = row[3]
            print(str(count)+" : name=%s, item name=%s, stock=%s, price=%s" % (name,itemName,stock,price))
    except:
        print("unable to fetch data")
    input("Press enter to continue...")


def goToUser():
    
    while True:
        #start user interaction
        msg = "Welcome User".center(50,"*")
        print(msg)
        choice  = int(input("\nWhat do you want to do ?\n1.Display Contractor Details\n2.Display Dealer Details\n3.Logout\nEnter Choice : "))
        if choice == 1:
            dispContractorDetails()
        elif choice == 2:
            dispDealerDetails()
        elif choice == 3:
            break
        else:
            print("Please choose correct option !!")
