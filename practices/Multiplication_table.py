#SW 2nd Multiplication table

size=int(input("How big would you like your multiplication tables?  "))
size2=int(size)
num_list=[]

while size2>=1:
    while size>=1:
        num_list.append(size)
        size=size-1
    num_list.reverse()