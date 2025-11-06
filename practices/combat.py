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

#sets enemy Hp and damage
op_hp=30
op_dmg=random.randint(1,8)


player_turn=True#to make sure the player can use their turn
playing=True#to continue the game loop
potions=4


#function for displaying actions and taking them
def turn():
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

    #sets enemy Hp and damage
    op_hp=30
    op_dmg=random.randint(1,8)


    player_turn=True#to make sure the player can use their turn
    playing=True#to continue the game loop
    potions=4

    op_hp=30
    op_dmg=random.randint(1,8)

    print(f"\n{name} has {hp} health\nan attack bonus of {bonus}\n{charges} special moves left\nand {potions} healing potions left")
    print(f"\nthe enemy has {op_hp} HP left\n" )
    print(f"type '1' to attack with your {attack}")
    print(f"type '2' to attack with your {special}")
    print(f"type '3' to drink a health potion")
    print(f"type '4' to run away\n")
    act=input("what is your choise?\n")
    roll=random.randint(1,20)#d20 roll to determine success of action
    op_roll=random.randint(1,20)#d20 roll to determine success of enemy attack
    
    while player_turn:
        if act=="1":
            if roll==20:
                op_hp-=2*attack_dmg
                print(f"You crit with your {attack} and dealt {attack_dmg*2} damage")
            elif roll<20 and roll>9:
                op_hp-=attack_dmg
                print(f"You hit with your {attack} and dealt {attack_dmg} damage")
            elif roll<10 and roll>1:
                print("you missed")
            elif roll==1:
                print("you tripped and hur your self and took 2 damage")
                hp-=2
            else:
                print("Error in code")
        elif act=="2":
            if charges>0:#makes sure you can only use the charges you have
                if roll==20:
                    op_hp-=2*special_dmg
                    print(f"You crit with your {special} and dealt {special_dmg*2} damage")
                elif roll<20 and roll>9:
                    op_hp-=special_dmg
                    print(f"You hit with your {special} and dealt {special_dmg} damage")
                elif roll<10 and roll>1:
                    print("you missed")
                elif roll==1:
                    print("you tripped and hur your self and took 4 damage")
                    hp-=4
                else:
                    print("Error in code")
                charges-=1
            else:
                print("You ran out of uses for you special move")
                continue
        elif act=="3":
            if potions>0:# makes sure you can only use the potions you have
                if roll==20:
                    hp+=10
                    print("you healed a whole  10 health")
                elif roll<20 and roll>9:
                    hp+=7
                    print("you healed 7 health")
                elif roll<10 and roll>1:
                    hp+=5
                    print("you healed 5 health")
                elif roll==1:
                    print("you healed only 3 health")
                    hp+=3
                else:
                    print("Error in code")
                potions-=1
            else:
                print("You're out of potions")
                continue
        elif act=="4":
            if roll==20:
                print("you easily got away")
                playing=False
            elif roll<20 and roll>13:
                print("you just managed to slip away")
                playing=False
            elif roll<14 and roll>1:
                print("you weren't able to get away")
            elif roll==1:
                print("you failed to run and tripped losing 3 health")
                hp-=3
            else:
                print("Error in code")
        else:
            print("please choose a valid action")
            continue
        break

    if op_hp<=0: #end game if player wins
        print("\nYou defeated the monster congradulations")
        playing=False


    if op_roll==20:
        print(f"\nthe enemy crit you dealing {op_dmg*2}")
        hp-=op_dmg*2
    elif op_roll<20 and roll>11:
        print(f"\nthe enemy hit you and dealt {op_dmg}")
        hp-=op_dmg
    elif op_roll<12 and roll>1:
        print("\nthe emeny missed you")
    elif op_roll==1:
        print("\nthe ememy hurt itself for 3 damage ")
        op_hp-=3
    else:
        print("Error in code")
    
    if hp<=0: #end game if player dies 
        print(f"\n{name} has died\n GAME OVER")
    playing=False

while playing:
    turn()
    player_turn=True