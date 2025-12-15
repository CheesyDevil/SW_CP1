#function for creating display with parameters for updates frequency, length and height
#display is a dictionary with lists acting as the rows
def display(length,height):
    line=[]
    disp={

    }

    for x in range(0,length):
        line.append("██")
    for i in range(0,height):
        disp[i]=line
    print(disp)
display(2,3)

