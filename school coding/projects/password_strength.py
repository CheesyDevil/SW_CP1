#SW 2nd Password Strength checker



list=["`","~","!","@","#","$","%","^","&","*","(",")","'",'"',"-","_","=","+","[","]","{","}","|",";",":",",","<",".",">","/","?"]

#Define points
points=int(0)
#have user input thier password
password=input("please input a password")
#if password length is greater or equal to 8 set char to true
if len(password) >= 8:
    char=True
else:
    char=False
#if password contains number set numb to true
if password.isdigit():
    numb=True
else:
    numb=False
#if password contains uppercase letter set upp to true
if password.isupper():
    upp=True
else:
    upp=False
#if password contains lowercase letter set low to true
if password.islower():
    low=True
else:
    low=False
#if any special characters are in password set special to true
special=False
for cha in password:
    if cha in list:
        special=True
        break
    else: 
        continue
#check if all the vaiables are true and display thier status to the user; also increase score accordingly
if char:
    print("your password is long enough")
    points+=1
else:
    print("your password should be 8+ characters long.")
if numb:
    print("your password contains a number")
    points+=1
else:
    print("For a better password add a number")
if upp:
    print("your password contains an uppercase letter")
    points+=1
else:
    print("For a better password add an uppercase letter")
if low:
    print("your password contains a lowercase letter")
    points+=1
else:
    print("For a better password add a lowercase letter")
if special:
    print("your password contains a special character")
    points+=1
else:
    print("For a better password add aspecial character")
#display how good their password is according to their point count
if points>=5:
    print("Congladulatuions, your password is very strong!")
elif points>=4:
    print("goob job, your pass word is pretty strong.")
elif points>=3:
    print("Nice, your pass word is decent, but maybe consider improving it?")
elif points>=2:
    print("please improve your password it's kind of weak")
elif points>=1:
    print("you need to improve your password it's very weak")
else:
    print("Okay, I understand that having a super weak password makes it easier to log into stuff,\nbut seriously man in todays day and age hackers are every where you need to have a strong password, \nso please change it and try to learn from this experience.")