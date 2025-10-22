
char=input("character")

if char.isupper():
    if ord(char)<90:
        e=ord(char) 
        e+=1
        char=chr(e)
    else:
        e=65
        char=chr(e)
elif char.islower():
    if ord(char)<122:
        e=ord(char) 
        e+=1
        char=chr(e)
    else:
        e=97
        char=chr(e)
else:
    ord(char)=ord(char)
print(char)