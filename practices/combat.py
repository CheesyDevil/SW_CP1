#SW 2nd combat Program


import random

#inputs to set character name and class
name=input("What is the name of your adventurer?\n")
class_no=input(f"And what is {name}'s class?\n type '1' for barbarian, type '2' for wizard, type '3' for monk\n")
#sets move names
if class_no=="1":
    attack="axe swing"
    attack_dmg=random.randint(1,12)+3
    special="raging axe"
    special_dmg=random.randint(6,17)+3
    hp=20
    bonus=3
    charges=3
elif class_no=="2":
    attack="firebolt"
    attack_dmg=random.randint(1,12)+5
    special="magic missle"
    special_dmg=random.randint(1,4)+random.randint(1,4)+random.randint(1,4)+5
    hp=10
    bonus=5
    charges=4
elif class_no=="3":
    attack="double bonk"
    attack_dmg=random.randint(1,6)+random.randint(1,6)+4
    special="axe kick"
    special_dmg=random.randint(1,10)+random.randint(1,10)+4
    hp=15
    bonus=4
    charges=3
else:
    print("please enter a valid class")

#sets enemy Hp and damage
op_hp=30
op_dmg=random.randint(1,8)


#function for displaying actions and taking them
def turn():
    print(f"{name} has {hp} health\nan attack bonus of {bonus}\nand {charges} special moves left\n")
    print(f"type '1' to attack with your {attack}")
    print(f"type '2' to attack with your {special}")
    print(f"type '3' to drink a health potion")
    print(f"type '4' to run away\n")
    act=input("what is your choise?\n")
    roll=random.randint(1,20)#d20 roll to determine success of attack
    if act=="1":
        if roll==20:
            op_hp-=2*attack_dmg
        elif roll<20 and roll>9:
            op_hp-=attack_dmg
        elif roll<10 and roll>1:
            print("you missed")
        elif roll==1:
            print("you tripped and hur your self and took 2 damage")
            hp-=2
        else:
            print("Error in code")
    elif act=="2":
            if roll==20:
                op_hp-=2*special_dmg
            elif roll<20 and roll>9:
                op_hp-=special_dmg
            elif roll<10 and roll>1:
                print("you missed")
            elif roll==1:
                print("you tripped and hur your self and took 2 damage")
                hp-=2
            else:
                print("Error in code")
    elif act=="3":
            if roll==20:
                hp+=7
                print("you healed 7 health")
            elif roll<20 and roll>9:
                hp+=5
                print("you healed 5 health")
            elif roll<10 and roll>1:
                print("you missed")
            elif roll==1:
                print("you tripped and hur your self and took 2 damage")
                hp-=2
            else:
                print("Error in code")