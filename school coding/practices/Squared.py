#SW 2nd Squared numbers



numbers=[123576,342,547,7,798,867,6,7096,646,90762,7,6594,9,908,567,197412,1507624,140742,2150164,1503215743]# number list

squares=list(map(lambda nub: nub**2,numbers))#function to square the numbers


for i, num in enumerate(numbers): #loop to print the numbers an their corresponding squares
    print(f"{num} squared is {squares[i]}")