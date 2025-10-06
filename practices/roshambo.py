#SW 2nd Rosck paper scissors 

playing=True
import random

while playing:
    print("input '1' for rock\n input '2' For scissors\n Input '3' for paper\n Input '4' to quit\n")
    
    choice=input("choose your fighter: ")
    opp=random.randint(1,3)
    if choice=="1":
        if opp==1:
            print("You chose rock and so did your opponent, You Tied\n( O )        ( O )\n        --\n  ______________\n  \    ____    /\n   \__(____)__/")
        elif opp==2:
            print("You chose rock and your opponent chose scissors, You won\n         ___\n        /  _)\n       |  /\n ______|  |\n(__       |\n(__       |\n(__       |\n(________/")
        elif opp==3:
            print("You chose rock and your opponent chose paper, You lost\n(___)  (___)\n | |    | |\n  ________  \n /        \ ")
        else:
            break
    elif choice=="2":
        if opp==2:
            print("You chose scissors and so did your opponent, You Tied\n( O )        ( O )\n        --\n  ______________\n  \    ____    /\n   \__(____)__/")
        elif opp==3:
            print("You chose scissors and your opponent chose paper, You won\n         ___\n        /  _)\n       |  /\n ______|  |\n(__       |\n(__       |\n(__       |\n(________/")
        elif opp==1:
            print("You chose scissors and your opponent chose rock, You lost\n(___)  (___)\n | |    | |\n  ________  \n /        \ ")
        else:
            break   
    elif choice=="3":
        if opp==3:
            print("You chose paper and so did your opponent, You Tied\n( O )        ( O )\n        --\n  ______________\n  \    ____    /\n   \__(____)__/")
        elif opp==1:
            print("You chose paper and your opponent chose rock, You won\n         ___\n        /  _)\n       |  /\n ______|  |\n(__       |\n(__       |\n(__       |\n(________/")
        elif opp==2:
            print("You chose paper and your opponent chose scissors, You lost\n(___)  (___)\n | |    | |\n  ________  \n /        \ ")
        else:
            break   
    elif choice=="4":
        playing=False
    else:
        print("\nplease use a valid input\n")
        continue
print("Thank you for playing.")