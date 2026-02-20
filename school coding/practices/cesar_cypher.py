#SW 2nd Cesar Cypher encoder and decoder


#reminder: use "ASCII" python string method
def encode(): #create encoding function
    mess=input("What is the message you would like to have cyphered\n ") #create input for what is being cyphered 
    cyph_chan=int(input("How many times would you like to chyper this message?\n"))#create input for cypher number
    out=''#output

    while cyph_chan>0:
        for char in mess:
            if char.isupper():
                if ord(char)<90:
                    e=ord(char) 
                    e+=1
                    out+=(chr(e))
                else:
                    e=65
                    out+=(chr(e))
            elif char.islower():
                if ord(char)<122:
                    e=ord(char) 
                    e+=1
                    out+=(chr(e))
                else:
                    e=97
                    out+=(chr(e))
            else:
                out+=char
        cyph_chan-=1

    while cyph_chan<0:
        for char in mess:
            if char.isupper():
                if ord(char)<90:
                    e=ord(char) 
                    e-=1
                    out+=(chr(e))
                else:
                    e=65
                    out+=(chr(e))
            elif char.islower():
                if ord(char)<122:
                    e=ord(char) 
                    e-=1
                    out+=(chr(e))
                else:
                    e=97
                    out+=(chr(e))
            else:
                out+=char
        cyph_chan+=1
    
    print(f" your final message is:\n {out}")


def decode(): #create encoding function
    mess=input("What is the message you would like to have decoded\n ") #create input for what is being cyphered 
    cyph_chan=-int(input("How many times was this message cyphered?\n"))#create input for cypher number
    out=''#output

    while cyph_chan>0:
        for char in mess:
            if char.isupper():
                if ord(char)<90:
                    e=ord(char) 
                    e+=1
                    out+=(chr(e))
                else:
                    e=65# if the letter is Z it loops back to A
                    out+=(chr(e))
            elif char.islower():
                if ord(char)<122:
                    e=ord(char) 
                    e+=1
                    out+=(chr(e))
                else:
                    e=97# if the letter is z it loops back to a
                    out+=(chr(e))
            else:
                out+=char
        cyph_chan-=1

    while cyph_chan<0:
        for char in mess:
            if char.isupper():
                if ord(char)>65:
                    e=ord(char) 
                    e-=1
                    out+=(chr(e))
                else:
                    e=90# if the letter is A it loops back to Z
                    out+=(chr(e))
            elif char.islower():
                if ord(char)>97:
                    e=ord(char) 
                    e-=1
                    out+=(chr(e))
                else:
                    e=122# if the letter is a it loops back to z
                    out+=(chr(e))
            else:
                out+=char
        cyph_chan+=1
    
    print(f" your final message is:\n {out}")


awn=input("Would you like to encode or decode?\n enter '1' for encode and '2' for decode\n") #add input for wether they are doing encoding or decoding
if awn=="1":#add function for directing whether they go to the encode or decode function
    encode()
elif awn=="2":
    decode()
else:
    print("please enter valid input")


#create function to cypher the input
#65=A  90=Z
#97=a 122=z