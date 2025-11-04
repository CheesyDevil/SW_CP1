def e:
    mess=input("character: ")
    mess_out=''
    for char in mess:
        if char.isupper():
            if ord(char)<90:
                e=ord(char) 
                e+=1
                mess_out+=(chr(e))
            else:
                e=65
                mess_out+=(chr(e))
        elif char.islower():
            if ord(char)<122:
                e=ord(char) 
                e+=1
                mess_out+=(chr(e))
            else:
                e=97
                mess_out+=(chr(e))
        else:
            ord(char)==ord(char)
        print(char)
    print(mess_out)