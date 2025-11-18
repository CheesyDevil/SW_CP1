#SW 2nd Flexible Calculator


def main():#Main loop
    num_tup=()#Tuple holding all of the inputted numbers
    num_list=[]#list holding all of the inputted numbers

    print("Ener your numbers of choice, type 'done' when finished")
    while True:
        num=input("Number:")
        if num.isdigit():
            num=float(num)
            num_list.append(num)
        elif num=="done":
            break
        else:
            print("Please use a valid input")
    num_list.sort()
    num_tup=tuple(num_list)#makes the numbers more accessable inside a tuple
    print(f"Available opperations:\nsum (adds all numbers together),\n mean (finds the average of the numbers),\nmin (finds the lowest number),\nmax (finds highest number),\nproduct (multiplies all numbers together)")
    input("which opperation do you want to use?\n")




def calc():#funtion asking if person is doing another calculation
    awn=input("would you like to preform another calculation? (Yes/No)").strip().lower().title()

