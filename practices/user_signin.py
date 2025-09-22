#SW 2nd User Signin

usernameC=input("What would you like your username to be? ")
passwordC=input("And What About your password? ")

username=input("Please enter your username: ")
password=input("Please enter your password: ")

if username == usernameC:
    print("correct username")
    if password == passwordC:
        print("Correct password \n Welcome to the Program")
    
    else:
        print("Incorrect password")
else:
    print("Incorrect username and/or passord")