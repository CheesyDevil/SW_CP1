
mess=input("character: ")
for char in mess:
    if char.isupper():
        if ord(char)<90:
            e=ord(char) 
            e+=1
            char.replace(chr(e))
        else:
            e=65
            char.replace(chr(e))
    elif char.islower():
        if ord(char)<122:
            e=ord(char) 
            e+=1
            char.replace(chr(e))
        else:
            e=97
            char.replace(chr(e))
    else:
        ord(char)==ord(char)
    print(char)
print(mess)