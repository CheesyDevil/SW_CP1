#SW 2nd Crew Shares

print("The crew earned a whole bunch of money on the last outing, but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares." )

Money=float(input("how much money did they make? \n").strip().replace("$",""))
Crew=int(input("How many members of the crew are there? \n"))


Share_number=Crew+10
Share=float(Money/Share_number)
shareR=round(Share, 2)

cap=float(shareR*7)
first=float(shareR*3)
crew=float(shareR-500)

capR=round(cap, 2)
firstR=round(first, 2)
crewR=round(crew, 2)

print("the captain gets $", capR)
print("the firstmate gets $", firstR)
print("the crew still needs $", crewR)