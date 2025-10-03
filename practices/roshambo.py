#SW 2nd Rosck paper scissors 

playing=True
import random

while playing:
    print("input '1' for rock\n input '2' For scissors\n Input '3' for paper\n Input '4' to quit")
    
    choice=input("choose your fighter")
    opp=random.randint(1,3)
    if choice=="1":
        if opp==1:
            print("You Tied")
        elif opp==2:
            print("You won")
        elif opp==3:
            print("You Lost")
        else:
            break
    elif choice=="2":
        if opp==2:
            print("You Tied")
        elif opp==3:
            print("You won")
        elif opp==1:
            print("You Lost")
        else:
            break   
    elif choice=="3":
        if opp==3:
            print("You Tied")
        elif opp==1:
            print("You won")
        elif opp==2:
            print("You Lost")
        else:
            break   

    