#SW 2nd Multiplication table

collums=int(input("How many collums would you like to be in your multiplication table?  "))
rows=int(input("How many rows would you like to be in your multiplication table?  "))
num_list=[]
count=1

while rows>=1:
    while rows>=1:
        num_list.append(rows)
        collums=collums-1
    num_list.reverse()
    print(num_list)
    collums=len(num_list)
    num_list.clear()
    count=count+1