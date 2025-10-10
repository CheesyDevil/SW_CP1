#SW 2nd Password Strength checker




#have user input thier password
password=input("please input a password")
#if password length is greater or equal to 8 set char to true
if len(password) >= 8:
    char=True
else:
    char=False
#if password contains number set numb to true
if password.isdigit:
    numb=True
else:
    numb=False
#if password contains uppercase letter set upp to true
if password.isupper:
    upp=True
else:
    upp=False
#if password contains lowercase letter set low to true
if password.islower:
    low=True
else:
    low=False
#if any special characters are in password set special to true
if "`"or"~"or"!"or"@"or"#"or"$"or"%"or"^"or"&"or"*"or"("or")"or"'"or'"'or"-"or"_"or"="or"+"or"["or"]"or"{"or"}"or"|"or";"or":"or","or"<"or"."or">"or"/"or"?"in password:
    special=True
else:
    special=False
#check if all the vaiables are true and display thier status to the user; also increase sccore accordingly
if char==True:
    print("your password is long enough")


