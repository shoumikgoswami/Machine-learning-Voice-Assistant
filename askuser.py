

def askUser(mode):
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    checkPass(username, password)
def checkPass(use, pwd):
    if use == "username" and pwd == "password":
        login(use)
    else:
        print "Your username and/or password was incorrect"
        askUser()
def login(use):
    print "Welcome " + use
    print "You have successfully logged in!"
    askCom()
def askCom():
    command = raw_input("Enter your command: ")
    if command == "log off" or command == "quit":
        username = ""
        password = ""
        print "You have logged off"
        askUser()
    else:
        print "Unknown command"
        askCom()