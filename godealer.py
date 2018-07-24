import mysql.connector as mariadb

def updateDetails(name, itemName, stock, price):
    #open database connection
    db = mariadb.connect(host='localhost', database='construction', user='root', password = 'groot')
    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #execute SQL query using execute method
    sql = "INSERT INTO dealer VALUES('"+name+"','"+itemName+"','"+stock+"','"+price+"')"
    try:
        cursor.execute(sql)
        db.commit()
        print("successfully updated")
    except:
        db.rollback()
        print("Exception")

    #close the connection
    db.close()

def dispAllItems():
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


def goToDealer():
    
    while True:
        #start user interaction
        msg = "Welcome Dealer".center(50,"*")
        print(msg)
        choice  = int(input("\nWhat do you want to do ?\n1.Update Details\n2.Display All Items\n3.Logout\nEnter Choice : "))
        if choice == 1:
            name = input("Enter your name : ")
            itemName = input("Enter Item name : ")
            stock = input("Enter stock : ")
            price = input("Enter price per piece : ")
            updateDetails(name, itemName, stock, price)
        elif choice == 2:
            dispAllItems()
        elif choice == 3:
            break
        else:
            print("Please choose correct option !!")
