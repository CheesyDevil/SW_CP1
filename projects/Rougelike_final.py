#SW 2nd Cat Rougelike Final Project


#import random

#create 8 dictionaries for indexes, (common cards, uncommon cards, rare cards, epic cards, legendary cards, basic cats, elite cats, boss cats) with a number as key and a list as the value with the list holding the different stats as well as the description
"""
cat_example :{ 1("index number"),['orange cat'("base description"),"Food and throwing toys"("weaknesses"),'boxes'("resistances"),3 ("attack bonus"), 20 ("base friendliness"), 10 ("Base agita")]}
card_example:{1('index number'),["melee toy effectiveness"("card name"), "1"("affected toy"),'1' ("bonus type"), 2 ("bonus number")]}"""

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





import random

#Dictionaries
basic_cats={
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
}
elite_cats={
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
}
boss_cats={
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
}

common_cards={
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
}
uncommon_cards={
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
}
rare_cards={
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
}
epic_cards={
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
}
legendary_cards={
0:[],
1:[],
2:[],
3:[],
4:[],
5:[],
6:[],
7:[],
8:[],
9:[],
}

#Lists
actions=["Melee Toy", "Throwing Toy", "Cat Food", 'Box', "Bandage", "Check", "Inentory", "Pet"]
mods=[[0,1],[0,1],[0,1],[0,1],[0,1],[0]]
cat=[]

#Integers
hp=100
bandages=10
boxes=1
friendliness=1
agita=1
cat_level=1
score=1
rooms=1
floors=0

#functions
def dismap():
    types=[]
    levels=[]
    if rooms==4:
        print("You are entering the boss room")
        cat_level=3
    else:
        for x in range(0,3):
            if random.randint(1,15)>=15-floors:
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
                print("Please enter a valid input")

def begin():
    if cat_level==1:
        cat=basic_cats[random.randint(0,9)]
    elif cat_level==2:
        cat=elite_cats[random.randint(0,9)]
    elif cat_level==3:
        cat=boss_cats[random.randint(0,9)]
    else:
        print('error')
    print(f"a {cat[0]} is approaching you")
    friendliness=cat[4]
    agita=cat[5]

def player():
    while True:
        print(f"You have {hp} Health left")
        print(f"to do an action type it's coresponding number\n1:{actions[0]}\n2:{actions[1]}\n3:{actions[2]}\n4:{actions[3]}\n5:{actions[4]}\n6:{actions[5]}\n7:{actions[6]}\n8:{actions[7]}")
        choice=input("what would you like to do?")
        if choice=="1":
            melee()
            break
        elif choice=="2":
            throw()
            break
        elif choice=="3":
            food()
            break
        elif choice=="4":
            box()
            break
        elif choice=="5":
            bandage()
            break
        elif choice=="6":
            check()
            break
        elif choice=="7":
            inventory()
            continue
        elif choice=="8":
            pet()
            break
        else:
            print("please enter a valid input")
def cat_turn():
    if agita>=random.randint(0,100):
        cattack=random.randint(1*cat_level+2*(floors-1),3*cat_level+2*(floors-1))
        print(f"the cat scratched you for {cattack} damage")
        hp-=cattack
    else:
        print("cat doesn't seem to want to scratch you.")

def melee():
    friendliness-=(random.randint(3,9)+mods[0[0]])*mods[0[1]]
    print("cat is playing with toy and seems more friendly")
def throw():
    friendliness-=(random.randint(7,9)+mods[1[0]])*mods[1[1]]
    agita+=10*cat_level
    print("cat went chased toy and seems more agitated and friendly")
def food():
    friendliness-=(random.randint(3,5)+mods[2[0]])*mods[2[1]]
    agita-=5*mods[2[1]]
    print("cat ate the food and seems less agitated and more friendly")
def box():
    boxes-=1
    if ((100-(agita*(cat_level/2))+mods[3[0]])*mods[3[1]])>=random.randint(1,100):
        agita+=20
        print("cat went in box and seems less agitated")
    else:
        print("The cat wasn't lured by the box")
def bandage():
    bandages-=1
    hp+=(random.randint(3,7)+mods[4[0]]*mods[4[1]])
def check():
    print(f"cat has an Agita of {agita}\n cat needs {friendliness} more freindliness points to be pet")
def inventory():
    print(f"Melee flat{mods[0[0]]},\nMelee mult{mods[0[1]]},\nthrowing flat{mods[1[0]]},\nthrowing mult{mods[1[1]]},\nfood flat{mods[2[0]]},\nfood mult{mods[2[1]]},\nbox flat{mods[3[0]]},\nbox mult{mods[3[1]]},\nhealing flat{mods[4[0]]},\nhealing mult{mods[4[1]]},\nLuck{mods[5[0]]}")
def pet():
    if friendliness<=0:
        print('cat let you pet it and gave you some loot')
        victory()
    else:
        print("cat recoiled at your approach")
def cadd():
    for x in range(0,3):
        card=[]
        rng=random.randint(1,50)+mods[5[0]]
        if rng>=50:
            card.append(legendary_cards[random.randint(0,9)])
            print(f"\033[93m{card[0]}\033[0m")
        elif rng>=45:
            card.append(epic_cards[random.randint(0,9)])
            print(f"\033[94m{card[0]}\033[0m")
        elif rng>=35:
            card.append(rare_cards[random.randint(0,9)])
            print(f"\033[96m{card[0]}\033[0m")
        elif rng>=20:
            card.append(uncommon_cards[random.randint(0,9)])
            print(f"\033[92m{card[0]}\033[0m")
        elif rng<20:
            card.append(common_cards[random.randint(0,9)])
            print(card[0])
        else:
            print("Error")
    while True:
        choice=input("which card would you like?")
        if choice=="1" or choice == "2" or choice =="3":
            choice=int(choice)
            card_1=card[1+(choice*4-4)]
            card_2=card[2+(choice*4-4)]
            mods[card_1[card_2]]+=card[3+(choice*4-4)]
            break
        else:
            print("Invalid input")
    
def victory():
    rooms+=1
    box_gain=random.randint(0,mods[5[0]])
    bandage_gain=random.randint(1+mods[5[0]],2*mods[5[0]]+2)
    print(f"you gained {box_gain} boxes and {bandage_gain} bandages")
    score+=(10**cat_level)*floors
    cadd()
    if rooms!=5:
        dismap()
    else:
        print
def defeat():
    print("GAME OVER")

while True:
    print("Welcome to cat cat tower ")
    #create floor loop
        #create room loop
            #player turn function
            #cat turn function 
            #if player hp<=0 
                #player lose function
            #else continue room loop
        #player victory function 
        #map function