import mysql.connector as mariadb

def registerUserfunc(name, uname, passwd, usertype):
    print("inside")
    #open database connection
    db = mariadb.connect(host='localhost', database='construction', user='root', password = 'groot')
    print("connected")
    #prepare a cursor object using cursor() method
    cursor = db.cursor()

    #execute SQL query using execute method
    sql = "INSERT INTO users VALUES('"+name+"','"+uname+"','"+passwd+"','"+usertype+"','"+str(0)+"');"
    try:
        cursor.execute(sql)
        db.commit()
        print("successfully updated")
    except:
        db.rollback()
        print("Exception")

    #close the connection
    db.close()