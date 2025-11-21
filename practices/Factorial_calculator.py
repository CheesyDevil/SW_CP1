#SW 2nd Falctorial Calculator


"""1. print welcome to the factorial calculator
2. ask user for input, input as "num", make sure
3. if the input is not an integer, print "Not valid input, please only input integers"--> xint
4. ask user input, input as num2
5.num x num2 x num3 x num4
6."""

print("welcome to the factorial calculator")
num=input("please enter a to factorial").strip()

while True:#added loop so it actually requires integer
    num=input("please enter a to factorial").strip().replace(".", "")

    if num.isnumeric():
        num=int(num)
        break
    else: print("Not valid input, please only input integers")


