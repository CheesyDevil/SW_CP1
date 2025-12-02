#SW 2nd Cat Rougelike Final Project


#import random

#create 8 dictionaries for indexes, (common cards, uncommon cards, rare cards, epic cards, legendary cards, basic cats, elite cats, boss cats) with a number as key and a list as the value with the list holding the different stats as well as the description
"""
cat_example :{ 1("index number"),['orange cat'("base description"),"Food and throwing toys"("weaknesses"),'boxes'("resistances"),3 ("attack bonus"), 20 ("base friendliness")]}
card_example:{1('index number'),["melee toy effectiveness"("card name"), "melee"("affected toy"),'+' ("bonus type"), 2 ("bonus number")]}"""

#create player action list with (heal, check, pet, melee toy, throwing toy, food, box)

#create player stats(Hp, Bandages, Luck)
#create modifiers(melee flat, melee mult, throwing flat, throwing mult, food flat, food mult, box flat, box mult, heal flat, heal mult)
#create a friendliness variable(cat HP)
#create an agita variable(how likely the cat is to scratch you)
#create cat rank variable (which can be 1 1.5 or 2 wether it's a basic, elite or boss level) (increases agita gain, loot collected, and score)  
#create score variable (increses after defeating cats)

#make funtion to randomly pick cat from dictionary, print("A (base description) is approachinig you."), and set friendliness to ("Base friendliness") 

#make a function that shows your action options and lets you choose between them triggering the different action functions

#make function for checking cat that displays ("this cat is weak to ("weaknesses"), resistant to ("resistances"), and has (friendliness) left") 
#make funtion for using a bandage, (you lose 1 bandage and heal ((3 to 7 + heal flat)*heal mult) health)
#make funtion for petting (if friendliness=0 you win the battle otherwise you increase agita by 20)

#make a funtion for food ( decreases friendliness by ((3 to 5 + food flat)*food mult) and agita by 5)
#make a funtion for melee toy ( decreases friendliness by ((3 to 9 + melee flat)*melee mult))
#make a funtion for throwing toy ( decreases friendliness by ((7 to 9 + throwing flat)*throwing mult) and increases agita by 10*cat rank)
#make a funtion for box ( chance to work is ((100-(agita*cat rank)+box flat)*box mult) and if sucessful decreases agita by 20)

#make a function for player victory (you recieve 1-3 bandages(can increases with luck), your score increases by 100**cat rank, and you get to choos between 3 cards which are selected by an RNG which picks a number 1-40 with higher numbers coresponding to higher rarity cards(the RNG number can be influenced by luck))
#make a function for player loss (a game over screen with your final score being displayed and the option to continue)

#make a funtion for the map()