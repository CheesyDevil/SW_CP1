#SW 2nd Cesar Cypher encoder and decoder


#reminder: use "ASCII" python string method
def encode(): #create encoding function
    mess=input("What is the message you would like to have cyphered\n ") #create input for what is being cyphered 
    cyph_chan=input("How many timeswyould you like to chyper this message?\n")#create input for cypher number

    if cyph_chan>0:
        for char in mess:
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
            cyph_chan-=cyph_chan
    elif cyph_chan<0:
        for char in mess:
            if char.isupper():
                if ord(char)>65:
                    e=ord(char) 
                    e-=1
                    char=chr(e)
                else:
                    e=90
                    char=chr(e)
            elif char.islower():
                if ord(char)>97:
                    e=ord(char) 
                    e-=1
                    char=chr(e)
                else:
                    e=122
                    char=chr(e)
            else:
                ord(char)=ord(char)
            cyph_chan+=cyph_chan
    else:
        mess+mess

def decode(): #create encoding function
    mess=input("What is the message you would like to have decoded\n ") #create input for what is being cyphered 
    cyph_chan=input("How many times was this message chypered\n")#create input for cypher number


awn=input("Would you like to encode or decode?\n enter '1' for encode and '2' for decode\n") #add input for wether they are doing encoding or decoding
if awn=="1":#add function for directing whether they go to the encode or decode function
    encode
elif awn=="2":
    decode
else:
    print("please entter valid input")


print(f"A= {ord("Z")}") #Finds index for character
print(f"100= {chr(100)}") #Finds character for index




#create function to cypher the input
#65=A  90=Z
#97=a 122=z