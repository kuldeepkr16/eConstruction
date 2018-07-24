import goadmin,gocontractor,godealer,gouser
import mysql.connector as mariadb

#open database connection
db = mariadb.connect(host='localhost',database='construction',user='root',password = 'groot')

#prepare a cursor object using cursor() method
cursor = db.cursor()

#function to go to admin panel
def goToAdminPanel():
    goadmin.gotoAdmin()

#function to go to admin panel
def goToUserPanel():
    gouser.goToUser()

#function to go to admin panel
def goToDealerPanel():
    godealer.goToDealer()

#function to go to contractor panel
def goToContractorPanel():
    gocontractor.gotoContractor()

def signIn():
    #user message
    str = "Welcome to Login Panel !!".center(50,"*")
    print(str)
    while True:    
        #user message
        str = "Welcome to Login Panel !!".center(50,"*")
        choice = int(input("Login as :\n1.Admin\n2.Normal User\n3.Contractor\n4.Hardware Dealer\n5.Exit\nEnter Your Choice (1,2,3,4 or 5) :"))
        if choice == 1:
            uname = input("Enter user name : ")
            passwd = input("Enter password : ")
            sql = "select name from users where uname='"+uname+"' and password = '"+ passwd +"' and usertype = 'admin'" 
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                print(data)
                goToAdminPanel()
            else:
                print("Wrong Credentials!!\n")

        elif choice == 2:
            uname = input("Enter user name : ")
            passwd = input("Enter password : ")
            sql = "select name from users where uname='"+uname+"' and password = '"+ passwd +"' and usertype = 'normal user'" 
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                goToUserPanel()
            else:
                print("Wrong Credentials!!\n")

        elif choice == 3:
            uname = input("Enter user name : ")
            passwd = input("Enter password : ")
            sql = "select name from users where uname='"+uname+"' and password = '"+ passwd +"' and usertype = 'contractor'" 
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                goToContractorPanel()
            else:
                print("Wrong Credentials!!\n")
            
        elif choice == 4:
            uname = input("Enter user name : ")
            passwd = input("Enter password : ")
            sql = "select name from users where uname='"+uname+"' and password = '"+ passwd +"' and usertype = 'hardware dealer'" 
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                goToDealerPanel()
            else:
                print("Wrong Credentials!!\n")
            
        elif choice == 5:
            break
        else :
            print("Please Enter Correct option !!")