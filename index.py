import registerUser as ru
import login as l

#assign user type
def assign_u(t):
    usertype = ""
    if t == 1:
        usertype = "normal user"
    elif t == 2:
        usertype = "contractor"
    elif t == 3:
        usertype = "hardware dealer"
    return usertype

#register function
def signup():
    name = input("Enter your full name : ")
    username = input("Enter username (must be unique) : ")
    passwd = input("Enter password : ")
    t = int(input("Are you a \n1.Normal user\n2.Contractor\n3.Hardware Dealer\nEnter 1,2 or 3 : "))
    if t == 1 or t == 2 or t == 3:
        usertype = assign_u(t)
    else:
        print("Select correct user type !!")
        signup()
    ru.registerUserfunc(name, username, passwd, usertype)

#login function
def signin():
    l.signIn()

# Start user interaction
str = "Welcome to the Application...".center(50,"*")
print(str)

print("Select one of these options...\n1.Login\n2.Signup\n")
a = int(input("Your Choice ? (1 or 2) : "))
if a == 1:
    signin()
elif a == 2:
    signup()
