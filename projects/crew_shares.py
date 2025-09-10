#SW 2nd Crew Shares





Money=int(input("how much money did they make? \n"))
Crew=int(input("How many members of the crew are there? \n"))

Share_number=Crew+10
Share=float(Money-(Crew*500)/Share_number)
shareR=round(Share, 2)
print(shareR)