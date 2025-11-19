#SW 2nd Flexible Calculator


def main():#Main loop
    num_list=[]#list holding all of the inputted numbers
    output=0#final output

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
    num_list.sort()#organizes numbers to be easier to use
    print(f"Available opperations:\nsum (adds all numbers together),\n mean (finds the average of the numbers),\nmin (finds the lowest number),\nmax (finds highest number),\nproduct (multiplies all numbers together)")
    opperation=input("which opperation do you want to use?\n").strip().lower()#imput for which opperation is used

    if opperation=="sum": #adds all numbers together
        for numb in num_list:
            output+=numb
    elif opperation=="mean":
        for numb in num_list:
            output+=numb
            output=output/len(num_list)
    elif opperation=="min":
        output=num_list[0]
    elif opperation=="max":
        output=num_list[len(num_list)]
    elif opperation=="product":
        output=1#set to 1 so multplying works
        for numb in num_list:
            output=1
            output=output*numb




def calc():#funtion asking if person is doing another calculation
    awn=input("would you like to preform another calculation? (Yes/No)").strip().lower().title()

