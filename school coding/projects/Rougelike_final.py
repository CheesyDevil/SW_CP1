#SW 2nd Cat Rougelike Final Project


#import random

#create 8 dictionaries for indexes, (common cards, uncommon cards, rare cards, epic cards, legendary cards, basic cats, elite cats, boss cats) with a number as key and a list as the value with the list holding the different stats as well as the description
"""
cat_example { 1("index number"):['orange cat'("base description"),"Food and throwing toys"("weaknesses"),'boxes'("resistances"),3 ("attack bonus"), 20 ("base friendliness"), 10 ("Base agita")]}
card_example{1('index number'):["melee toy effectiveness"("card name"), "1"("affected toy"),'1' ("bonus type"), 2 ("bonus number")]}"""

#create player action list with (heal, check, pet, melee toy, throwing toy, food, box, inverntory)
#create modifiers list ((melee flat, melee mult), (throwing flat, throwing mult), (food flat, food mult), (box flat, box mult), (heal flat, heal mult), Luck)

#create player HP variable
#create Bandages variable
#create boxes variable

#create a friendliness variable(cat HP)
#create an agita variable(how likely the cat is to scratch you)
#Create cat level variable (changes based on which kind of cat you are fighting (1,2,3))(increases your loot luck)
  
#create score variable (increses after defeating cats)

#Create rooms variable (keeps track of how many rooms you've gone through)
#Create Floors variable (keeps track of how many floors you've cleared)

#make funtion to start battle (check cat level to determine cat dictionary)(randomly pick cat from coresponding dictionary) print("A (base description) is approachinig you."), and set friendliness to ("Base friendliness") , set agita to ("base agita")

#make a function for player turn (print player hp)(shows your action options and lets you choose between them triggering the different action functions)(if you don't have enouhgh bandages or boxes tell player and restart loop)(if player uses in ventoy print inverntoy and let player choose again)

#make Function for inventory (print your bandage amount, boxes amount and all your modifiers(using for loop))
#make function for checking cat that displays ("this cat is weak to ("weaknesses"), resistant to ("resistances"), has a current Agita of (agita), and has (friendliness) left") 
#make funtion for using a bandage, (you lose 1 bandage and heal ((3 to 7 + heal flat)*heal mult) health)
#make funtion for petting (if friendliness=0 you win the battle otherwise you increase agita by 20)

#make a funtion for food ( decreases friendliness by ((3 to 5 + food flat)*food mult) and agita by 5)
#make a funtion for melee toy ( decreases friendliness by ((3 to 9 + melee flat)*melee mult))
#make a funtion for throwing toy ( decreases friendliness by ((7 to 9 + throwing flat)*throwing mult) and increases agita by 10*cat level)
#make a funtion for box (you lose 1 box)( chance to work is ((100-(agita*(cat level/2))+box flat)*box mult) and if sucessful decreases agita by 20)

#make a function for cat turn (cat has a (agita/100)% chance to try to scratch you for (1*cat level) to (3*cat level ) damage)

#make card add funtion (add bonus number to bonus type in affected toy list in the modifiers list)

#make a function for player victory (check if cat rooms=5 and if it does reset the map and increase floors vairable, else add 1 to rooms)(You recieve 0-2 boxes (can increse with luck and cat level))(you recieve 1-3 bandages(can increases with luck and cat level), your score increases by 100**cat level, and you get to choose between 3 cards which are selected by an RNG which picks a number 1-40 with higher numbers coresponding to higher rarity cards(the RNG number can be influenced by luck and cat level))(add card using card add function)
#make a function for player loss (a game over screen with your final score being displayed and the option to continue)(if player says yes restart entire game loop)(if player says no end game)

#make a funtion for the map (check if Rooms=5 and if it does send player to the boss)(Display the map(Show which room player is in)(show the next room options (each one has (1 + Floors)/5 chance of being an Elite fight))(give player option to go left, right, or middle)(set cat level to 1 if room is basic, 2 if room is elite or 3 if room is Boss)

"""                 O
                O   O   O
            O   O   O   O   O
        O   O   O   O   O   O   O
    O   O   O   O   O   O   O   O   O
                  boss                  """

#create game loop
    # Welcome player to game
    #create floor loop
        #create room loop
            #player turn function
            #cat turn function 
            #if player hp<=0 
                #player lose function
            #else continue room loop
        #player victory function 
        #map function




import time
import sys
import random

#Dictionaries
'''cat template:["Description",dmg mult for melee,dmg mult for  throwing,dmg mult for  food,dmg mult for box, attack bonus, base friendliness, base agita]'''
basic_cats={
0:["Orange Tabby" , 1, 1.5, 1.5, 1,   2, 15, 15],
1:["Black Cat" , 1.5, 1.5, 1, 2,   4, 15, 20],
2:["White Cat" , 1.5, 1.5, 1.5, 1.5,   1, 35, 10],
3:["Grey Tabby" , 1.5, 1.5, 1.5, 1,   3, 15, 20],
4:["Calico" , 1.5, 2, 1, 1,   2, 25, 15],
5:["Siamese" , 1.5, 1.5, 1.5, 1.5,   5, 10, 30],
6:["British short hair" , 1, 0.5, 1.5, 1,   2, 15, 10],
7:["White Cat with Black Spots" , 2, 2, 0.5, 0.5,   4, 10, 25],
8:["Black Tuxedo" , 1, 1, 2, 1,   2, 15, 15],
9:["Orange Tuxedo" , 1.5, 1, 1, 1.5,   2, 15, 10],
}
elite_cats={
0:["Siamese Twins" , 1.5, 1.5, 1.5, 1,   5, 25, 40],
1:["Scottish Fold" , 1, 1.5, 0.5, 1.5,   3, 40, 10],
2:["Red on Blue Tabby" , 1, 1.5, 1.5, 1,   2, 15, 50],
3:["Sphynx" , 1, 1, 1, 1,   3, 25, 30],
4:["Maine Coon" , 1, 0.5, 0.5, 1.5,   1, 50, 15],
}
boss_cats={
0:["Lykoi" , 1.5, 1.5, 1, 0.5,   7, 25, 60],
1:["Norweigen Forest Cat", 0.5, 1, 0.5, 1.5,   4, 65, 20],
2:["Munchkin" , 1.5, 0.5, 1, 1.5,   5, 40, 50],
}

'''card template:["Card Name",affected list,affected value, added value]'''
common_cards={
0:["Melee Flat:  +2", 0, 0, 2],
1:["Melee Mult:  +0.3", 0, 1, 0.3],
2:["Throwing Flat:  +2", 1, 0, 2],
3:["Throwing Mult:  +0.2", 1, 1, 0.2],
4:["Food Flat:  +2", 2, 0, 2],
5:["Food Mult:  +0.2", 2, 1, 0.2],
6:["Box Flat:  +3", 3, 0, 3],
7:["Box Mult:  +0.3", 3, 1, 0.3],
8:["Healing Flat:  +2", 4, 0, 2],
9:["Healing Mult:  +0.2", 4, 1, 0.2],
}
uncommon_cards={
0:["Melee Flat+:  +3", 0, 0, 3],
1:["Melee Mult+:  +0.4", 0, 1, 0.4],
2:["Throwing Flat+:  +3", 1, 0, 3],
3:["Throwing Mult+:  +0.3", 1, 1, 0.3],
4:["Food Flat+:  +3", 2, 0, 3],
5:["Food Mult+:  +0.3", 2, 1, 0.3],
6:["Box Flat+:  +4", 3, 0, 4],
7:["Box Mult+:  +0.3", 3, 1, 0.3],
8:["Healing Flat+:  +3", 4, 0, 3],
9:["Healing Mult+:  +0.3", 4, 1, 0.3],
10:["Luck:  +2", 5, 0, 2],
}
rare_cards={
0:["Melee Flat++:  +5", 0, 0, 5],
1:["Melee Mult++:  +0.7", 0, 1, 0.7],
2:["Throwing Flat++:  +5", 1, 0, 5],
3:["Throwing Mult++:  +0.5", 1, 1, 0.5],
4:["Food Flat++:  +5", 2, 0, 5],
5:["Food Mult++:  +0.5", 2, 1, 0.5],
6:["Box Flat++:  +4", 3, 0, 4],
7:["Box Mult++:  +0.5", 3, 1, 0.5],
8:["Healing Flat++:  +5", 4, 0, 5],
9:["Healing Mult++:  +0.5", 4, 1, 0.5],
10:["Luck+:  +3", 5, 0, 3],
}
epic_cards={
0:["Melee Flat★:  +7", 0, 0, 7],
1:["Melee Mult★:  +0.9", 0, 1, 0.9],
2:["Throwing Flat★:  +7", 1, 0, 7],
3:["Throwing Mult★:  +0.7", 1, 1, 0.7],
4:["Food Flat★:  +7", 2, 0, 7],
5:["Food Mult★:  +0.7", 2, 1, 0.7],
6:["Box Flat★:  +7", 3, 0, 7],
7:["Box Mult★:  +0.7", 3, 1, 0.7],
8:["Healing Flat★:  +7", 4, 0, 7],
9:["Healing Mult★:  +0.7", 4, 1, 0.7],
10:["Luck++:  +5", 5, 0, 5],
}
legendary_cards={
0:["Melee Flat★★:  +10", 0, 0, 10],
1:["Melee Mult★★:  +1.2", 0, 1, 1.2],
2:["Throwing Flat★★:  +10", 1, 0, 10],
3:["Throwing Mult★★:  +1", 1, 1, 1],
4:["Food Flat★★:  +10", 2, 0, 10],
5:["Food Mult★★:  +1", 2, 1, 1],
6:["Box Flat★★:  +10", 3, 0, 10],
7:["Box Mult★★:  +1", 3, 1, 1],
8:["Healing Flat★★:  +10", 4, 0, 10],
9:["Healing Mult★★:  +1", 4, 1, 1],
10:["Luck★:  +7", 5, 0, 7],
}

#Lists
actions=["Melee Toy", "Throwing Toy", "Cat Food", 'Box', "Bandage", "Check", "Inventory", "Pet"]
mods=[[0,1],[0,1],[0,1],[0,1],[0,1],[0]]
cat=[]

#Integers
hp=100
bandages=10
boxes=1
friendliness=1
agita=1
cat_level=1
score=0
room=1
floor=1

#booleans
unpetted=True
checked=False

#functions
def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)  
    print()

def dismap(room,cat_level,floor):
    types=[]
    levels=[]
    if room==5:
        slow_print("You are entering the boss room", delay=0.2)
        cat_level=3
    else:
        for x in range(0,3):
            if random.randint(1,15)+room>=(15-floor):
                types.append("elite")
                levels.append(2)
            else:
                types.append("basic")
                levels.append(1)
        while True:
            direct=input(f"would you like to go to the\n Left:{types[0]} (1)\n Middle:{types[1]} (2)\n Right:{types[2]}(3)\n")
            if direct=="1" or direct == "2" or direct =="3":
                direct=int(direct)
                cat_level=levels[direct-1]
                break
            else:
                slow_print("Please enter a valid input")
    return cat_level

def begin(cat_level,basic_cats,elite_cats,boss_cats):
    cat=[]
    if cat_level==1:
        cat=basic_cats[random.randint(0,len(basic_cats)-1)]
    elif cat_level==2:
        cat=elite_cats[random.randint(0,len(elite_cats)-1)]
    elif cat_level==3:
        cat=boss_cats[random.randint(0,len(boss_cats)-1)]
    else:
        slow_print('error')
    slow_print(f"a {cat[0]} is approaching you", delay=0.1)
    return cat

def melee(friendliness,mods,cat):
    friendliness_gain=int(((random.randint(3,9)+mods[0][0])*mods[0][1])*cat[1])
    friendliness-=friendliness_gain
    slow_print(f"cat is playing with toy and got {friendliness_gain} points more friendly")
    return int(friendliness)
def throw(friendliness,mods,cat_level,agita,cat):
    friendliness_gain=int(((random.randint(7,9)+mods[1][0])*mods[1][1])*cat[2])
    friendliness-=friendliness_gain
    agita+=10*cat_level
    slow_print(f"cat went chased toy and got {cat_level*10} points more agitated and {friendliness_gain} points more friendly")
    return int(friendliness) , int(agita)
def food(friendliness,mods,agita,cat):
    friendliness_gain=int(((random.randint(3,5)+mods[2][0])*mods[2][1])*cat[3])
    friendliness-=friendliness_gain
    agita-=int((5*mods[2][1])*cat[3])
    slow_print(f"cat ate the food and got {int(5*mods[2][1]*cat[3])} points less agitated and {friendliness_gain} points more friendly")
    return int(friendliness) , int(agita)
def box(boxes,agita,mods,cat):
    boxes=int(boxes-1)
    if (((100-(agita*cat_level))+mods[3][0])*mods[3][1])>=random.randint(1,100):
        agita+=int(20*cat[4])
        slow_print(f"cat went in box and got {int(20*cat[4])} points less agitated")
    else:
        slow_print("The cat wasn't lured by the box")
    return int(agita),int(boxes)
def bandage(bandages,hp,mods):
    bandages=int(bandages-1)
    hp_gain=int(random.randint(3,7)+mods[4][0]*mods[4][1])
    hp=hp+hp_gain
    slow_print(f"the bandage healed you {hp_gain}")
    return int(bandages) , int(hp)
def check(friendliness,agita,cat,checked):
    slow_print(f"cat has an Agita of {int(agita)}\ncat needs {int(friendliness)} more freindliness points to be pet\nMults:\nMelee:{cat[1]}X  Throwing:{cat[2]}X   Food:{cat[3]}X  Box:{cat[4]}X")
    checked=True
    return checked
def inventory(mods,boxes,bandages):
    slow_print(f"Bandages:{int(bandages)},\nBoxes:{int(boxes)},\nMelee flat:{int(mods[0][0])},\nMelee mult:{mods[0][1]},\nThrowing flat:{int(mods[1][0])},\nThrowing mult:{mods[1][1]},\nFood flat:{int(mods[2][0])},\nFood mult:{mods[2][1]},\nBox flat:{int(mods[3][0])},\nBox mult:{mods[3][1]},\nHealing flat:{int(mods[4][0])},\nHealing mult:{mods[4][1]},\nLuck:{int(mods[5][0])}")
def pet(friendliness):
    if friendliness<=0:
        slow_print('cat let you pet it and gave you some loot')
        return False
    else:
        slow_print("cat recoiled at your approach")
        return True

def player(hp,actions,mods,cat_level,friendliness,agita,bandages,boxes,unpetted,cat,checked):
    slow_print(f"You have {int(hp)} Health left",delay=0.02)
    slow_print(f'you need {int(friendliness)} more friendliness points to pet the cat',delay=0.02)
    while True:
        slow_print(f"to do an action type it's coresponding number\n1:{actions[0]}\n2:{actions[1]}\n3:{actions[2]}\n4:{actions[3]}\n5:{actions[4]}\n6:{actions[5]}\n7:{actions[6]}\n8:{actions[7]}\ninput ? for more info", delay=0.02 )
        choice=input("what would you like to do?")
        if choice=="1":
            friendliness=melee(friendliness,mods,cat)
            break
        elif choice=="2":
            friendliness,agita=throw(friendliness,mods,cat_level,agita,cat)
            break
        elif choice=="3":
            friendliness,agita=food(friendliness,mods,agita,cat)
            break
        elif choice=="4":
            if boxes>0:
                agita,boxes=box(boxes,agita,mods,cat)
                break
            else:
                slow_print("you seem to be out of boxes")
                continue
        elif choice=="5":
            if bandages>0:
                bandages,hp=bandage(bandages,hp,mods)
                break
            else:
                slow_print("You seem to have run out of bandages.")
                continue
        elif choice=="6":
            if checked==False:
                check(friendliness,agita,cat)
                break
            else:
                continue
        elif choice=="7":
            inventory(mods,boxes,bandages)
            continue
        elif choice=="8":
            unpetted=pet(friendliness)
            break
        elif choice=='?':
            slow_print(f"agita refers to the percent chance for the cat to attack you\nto defeat the cat you mut select the pet option when friendliness left is less than or equal to 0\nmelee only increases frendliness\nthrowing toy increases freindliness more but increases agita\nfood decreases agita but increases friendliness less\nbox only has a chance of workinbg and just lower agita by 20\nbandages are used to increase your health but you only have a limited amount of them\ncheck gives you information on the cat's weaknesses\ninventory lets you check your stats and doesn't take your turn\npet is you win condition and only works if cat has 0 or less friendship befor being able to be pet")
        else:
            slow_print("please enter a valid input")
    return int(agita),int(friendliness),int(hp),int(bandages),int(boxes),unpetted,checked
def cat_turn(agita,cat,cat_level,hp):
    if agita>=random.randint(1,100):
        cattack=int(random.randint(1*cat_level+3*(floor-1),3*cat_level+4*(floor-1))+cat[5])
        slow_print(f"the cat scratched you for {cattack} damage")
        hp-=cattack
    else:
        slow_print("cat doesn't seem to want to scratch you.")
    return int(hp)

def cadd(mods,common_cards,uncommon_cards,rare_cards,epic_cards,legendary_cards):
    card=[]
    for i in range(3):
        rng=random.randint(1,50)+mods[5][0]
        if rng>=50:
            card.append(legendary_cards[random.randint(0,len(legendary_cards)-1)])
            slow_print(f"Card #{i+1}:\033[93m{card[i][0]}\033[0m")
        elif rng>=45:
            card.append(epic_cards[random.randint(0,len(epic_cards)-1)])
            slow_print(f"Card #{i+1}:\033[94m{card[i][0]}\033[0m")
        elif rng>=35:
            card.append(rare_cards[random.randint(0,len(rare_cards)-1)])
            slow_print(f"Card #{i+1}:\033[96m{card[i][0]}\033[0m")
        elif rng>=20:
            card.append(uncommon_cards[random.randint(0,len(uncommon_cards)-1)])
            slow_print(f"Card #{i+1}:\033[92m{card[i][0]}\033[0m")
        elif rng<20:
            card.append(common_cards[random.randint(0,len(common_cards)-1)])
            slow_print(f"Card #{i+1}:{card[i][0]}")
        else:
            slow_print("ERROR CODE: 346")
    while True:
        choice=input("which card would you like?")
        if choice=="1" or choice == "2" or choice =="3":
            choice=int(choice)
            card_1=card[choice-1][1]
            card_2=card[choice-1][2]
            mods[card_1][card_2]+=card[choice-1][3]
            break
        else:
            slow_print("Invalid input")
    return mods
    
def victory(room,boxes,bandages,cat_level,floor,mods,common_cards,uncommon_cards,rare_cards,epic_cards,legendary_cards,score):
    room+=1
    box_gain=int(random.randint(0,mods[5][0]))
    bandage_gain=int(random.randint(1+mods[5][0],2*mods[5][0]+2))
    slow_print(f"you gained {box_gain} boxes and {bandage_gain} bandages")
    bandages+=bandage_gain
    boxes+=box_gain
    score+=(10**cat_level)*floor
    mods=cadd(mods,common_cards,uncommon_cards,rare_cards,epic_cards,legendary_cards)
    if room==6:
        floor+=1
        room=1
    return mods , int(boxes) , int(bandages) , int(score) ,int(room), int(floor)
def defeat(score,floor,room):
    slow_print(f"GAME OVER\n FLOOR:{floor}  ROOM:{room}\nFINAL SCORE:{score}",delay=0.2)
    while True:
        cont=input(f"would you like to play again?\n Yes(1) or No(2)")
        if cont=="1":
            return True
        elif cont=="2":
            return False
        else:
            slow_print("Invalid input")

#main game loop
while True:#game loop
    slow_print("Welcome to the cat tower ", delay=0.3)
    while True:#room loop
        cat=begin(cat_level,basic_cats,elite_cats,boss_cats)
        friendliness=int((cat[6]*floor)+room)
        agita=int(cat[7]+(room*floor))
        while True:#combat loop
            agita,friendliness,hp,bandages,boxes,unpetted,checked=player(hp,actions,mods,cat_level,friendliness,agita,bandages,boxes,unpetted,cat,checked)
            if unpetted:
                hp=cat_turn(agita,cat,cat_level,hp)
                if hp<=0:
                    break
                else:
                    continue
            else:
                break
        if not unpetted:
            mods , boxes , bandages , score ,room, floor=victory(room,boxes,bandages,cat_level,floor,mods,common_cards,uncommon_cards,rare_cards,epic_cards,legendary_cards,score)
            cat_level=dismap(room,cat_level,floor)
            unpetted=True
            checked=False
            continue
        elif hp==0:
            break
        else:
            slow_print("ERROR CODE: 417")
    if defeat(score,floor,room):
        continue
    else:
        slow_print("thanks for playing")
        break