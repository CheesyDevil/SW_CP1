#SW 2nd For Loops Notes

nums=[30,2,5,42,1,25689,73,94]

#What is iteration
    #an iteraton of the loop
#How do you write a for loop?
for num in nums:
    div=num/2
    if div>100:
        print(f"{div} is half of {num}. And is still a large number") 
    else:
        print(num)
#What is the variable that is represented commonly by i?
    #the itorator
#What can we name that besides i?
    #X
#Why do we indent on the line after the colon?
    #so that only that part of the code is assigned to the loop
#What is repetition in programming?
    #the ability to use a single piece of code multiple times/to iterate
#How do you write a range function?
for x in range(1,10):
    print(x)
print("counting by 2's")
for x in range(2,11,2):
    print(x)
print('countdown')
for x in range(10,0,-1):
    print(x)