import mysql.connector as mariadb
#open database connection
db = mariadb.connect(host='localhost', database='construction', user='root', password = 'groot')
cursor = db.cursor()


#function to display blocked users
def dispBlockedUsers():
    sql = "SELECT * FROM users where blocked = "+ str(1)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            count+=1
            name = row[0]
            uname = row[1]
            usertype = row[3]
            block = row[4]
            blocked = getBlock(block)
            print(str(count)+" : name=%s, username=%s, usertype=%s, blocked=%s" % (name,uname,usertype,blocked))
    except:
        print("unable to fetch data")
    input("Press enter to continue...")

#function to block a user
def blockUser():
    ename = input("Enter username of the user : ")
    sql = "SELECT * FROM users where uname = '"+ename+"'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            count+=1
            name = row[0]
            uname = row[1]
            usertype = row[3]
            block = row[4]
            blocked = getBlock(block)
            print(str(count)+" : name=%s, username=%s, usertype=%s, blocked=%s" % (name,uname,usertype,blocked))
    except:
        print("unable to fetch data")

    c = int(input("What do you want to do with this user !!\n1.BLOCK\n2.UNBLOCK\nEnter Your Choice - 1 or 2 : "))
    if c == 1:
        sql2 = "update users set blocked = 1 where uname = '"+ename+"'"
        try:
            cursor.execute(sql2)
            print("updated")
        except:
            print("unable to do the operation")
    
    elif c == 2:
        sql3 = "update users set blocked = 0 where uname = '"+ename+"'"
        try:
            cursor.execute(sql3)
            print("updated")
        except:
            print("unable to do the operation")
    input("Press enter to continue...")

#function to get blocked status
def getBlock(block):
    blocked = "NO"
    if block == 1:
        blocked = "YES"
    else:
        blocked = "NO"
    return blocked

#function to check user details
def chkUser():
    name = input("Enter name of the user : ")
    sql = "SELECT * FROM users where name = '"+name+"'"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            count+=1
            name = row[0]
            uname = row[1]
            usertype = row[3]
            block = row[4]
            blocked = getBlock(block)
            print(str(count)+" : name=%s, username=%s, usertype=%s, blocked=%s" % (name,uname,usertype,blocked))
    except:
        print("unable to fetch data")
    input("Press enter to continue...")

#function to display all users
def allUsers():
    sql = "SELECT * FROM users"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        count = 0
        for row in results:
            count+=1
            name = row[0]
            uname = row[1]
            usertype = row[3]
            block = row[4]
            blocked = getBlock(block)
            print(str(count)+" : name=%s, username=%s, usertype=%s, blocked=%s" % (name,uname,usertype,blocked))
    except:
        print("unable to fetch data")
    input("Press enter to continue...")

def gotoAdmin():
    #start user interaction
    msg = "Welcome Admin".center(50,"*")
    print(msg)
    while True:
        #start user interaction
        msg = "Welcome Admin".center(50,"*")
        choice  = int(input("\nWhat do you want to do ?\n1.Check User Details\n2.Display Blocked Users\n3.Block User\n4.Display All Users\n5.Logout\nEnter Choice : "))
        if choice == 1:
            chkUser()
        elif choice == 2:
            dispBlockedUsers()
        elif choice == 3:
            blockUser()
        elif choice == 4:
            allUsers()
        elif choice == 5:
            break
        else:
            print("Please choose correct option !!")
