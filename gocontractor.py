import mysql.connector as mariadb

def updateDetails(name, houseType, locality, price):
    #open database connection
    db = mariadb.connect(host='localhost', database='construction', user='root', password = 'groot')
    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #execute SQL query using execute method
    sql = "INSERT INTO contractor VALUES('"+name+"','"+houseType+"','"+locality+"','"+price+"')"
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


def gotoContractor():
    
    while True:
        #start user interaction
        msg = "Welcome Contractor".center(50,"*")
        print(msg)
        choice  = int(input("\nWhat do you want to do ?\n1.Update Details\n2.Display All Items\n3.Logout\nEnter Choice : "))
        if choice == 1:
            name = input("Enter your name : ")
            houseType = input("Enter house type : ")
            locality = input("Enter locality : ")
            price = input("Enter your price : ")
            updateDetails(name, houseType, locality, price)
        elif choice == 2:
            dispAllItems()
        elif choice == 3:
            break
        else:
            print("Please choose correct option !!")
