#SW 2nd Cat Rougelike Final Project


#import random

#create 8 dictionaries for indexes, (common cards, uncommon cards, rare cards, epic cards, legendary cards, basic cats, elite cats, boss cats) with a number as key and a list as the value with the list holding the different stats as well as the description
"""
cat_example :{ 1("index number"),['orange cat'("base description"),"Food and throwing toys"("weaknesses"),'boxes'("resistances"),3 ("attack bonus"), 20 ("base friendliness"), 10 ("Base agita")]}
card_example:{1('index number'),["melee toy effectiveness"("card name"), "melee"("affected toy"),'+' ("bonus type"), 2 ("bonus number")]}"""

#create player action list with (heal, check, pet, melee toy, throwing toy, food, box, inverntory)
#create modifiers list (melee flat, melee mult, throwing flat, throwing mult, food flat, food mult, box flat, box mult, heal flat, heal mult, Luck)

#create player HP variable
#create Bandages variable

#create a friendliness variable(cat HP)
#create an agita variable(how likely the cat is to scratch you)
#create cat rank variable (which can be 1 1.5 or 2 wether it's a basic, elite or boss level) (increases agita gain, loot collected, and score)
#Create cat level variable (changes based on which kind of cat you are fighting (1,2,3))(increases your loot luck)
  
#create score variable (increses after defeating cats)

#Create rooms variable (keeps track of how many rooms you've gone through)
#Create Floors variable (keeps track of how many floors you've cleared)


#make funtion to start battle (check cat level to determine cat dictionary)(randomly pick cat from coresponding dictionary) print("A (base description) is approachinig you."), and set friendliness to ("Base friendliness") , set agita to ("base agita")

#make a function for player turn (print player hp)(shows your action options and lets you choose between them triggering the different action functions)

#make Function for inventory (print your bandage amount, your Luck, and all your modifiers)
#make function for checking cat that displays ("this cat is weak to ("weaknesses"), resistant to ("resistances"), has a current Agita of (agita), and has (friendliness) left") 
#make funtion for using a bandage, (you lose 1 bandage and heal ((3 to 7 + heal flat)*heal mult) health)
#make funtion for petting (if friendliness=0 you win the battle otherwise you increase agita by 20)

#make a funtion for food ( decreases friendliness by ((3 to 5 + food flat)*food mult) and agita by 5)
#make a funtion for melee toy ( decreases friendliness by ((3 to 9 + melee flat)*melee mult))
#make a funtion for throwing toy ( decreases friendliness by ((7 to 9 + throwing flat)*throwing mult) and increases agita by 10*cat rank)
#make a funtion for box ( chance to work is ((100-(agita*cat rank)+box flat)*box mult) and if sucessful decreases agita by 20)

#make a function for cat turn (cat has a (agita/100)% chance to try to scratch you for (1*cat level) to (3*cat level ) damage)

#make a function for player victory (add 1 to rooms) (you recieve 1-3 bandages(can increases with luck and cat level), your score increases by 100**cat rank, and you get to choos between 3 cards which are selected by an RNG which picks a number 1-40 with higher numbers coresponding to higher rarity cards(the RNG number can be influenced by luck and cat level))
#make a function for player loss (a game over screen with your final score being displayed and the option to continue)

#make a funtion for the map (check if Rooms=5 and if it does send player to the boss)(Display the map(Show which room player is in)(show the next room options (each one has (1 + Floors)/5 chance of being an Elite fight))(give player option to go left, right, or middle)(set cat level to 1 if room is basic, 2 if room is elite or 3 if room is Boss)

"""                 O
                O   O   O
            O   O   O   O   O
        O   O   O   O   O   O   O
    O   O   O   O   O   O   O   O   O
                  boss                  """

