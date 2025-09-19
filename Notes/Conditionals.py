#SW 2nd Conditionals Notes

variable=float(input("enter a number: "))



#What are conditionals in python? 
  #a system that checks booleans to dicide weather or not a piece of code runs
#How do we write an if statement? 
if variable > 4:
    print('greater than 4')
elif variable < 4:
    print('less than 4')
else:
    print("variable is 4")
#How do we write conditions?
  #start with if end with else and elif's are in the middle
#Why does the code need to be indented after the if?
  #so it isn't just treated as a normal piece of code
#Why do we want to have else statements?
  #so we can have multiple results rather than a single one
#How many else if statements can you create? 
  #As many as you want
#Why does the order of your statements matter in a conditional?
  #so the conditional actually works
#How do we use boolean instead of boolean statements? 
if False:
    print('flase')



import random
monster_hp=30
dmg_mod=2
atk_bonus=3


roll=random.randint(1,20)

print(f"you rolled a {roll}.")
if monster_hp<=0:
    print('you have defeated the monster')
elif roll==20:
    print('you crit!!')
    attack=random.randint(1,8) + random.randint(1,8) + dmg_mod 
    monster_hp-=attack
    print(f"you delt {attack} damage, the monster dropped to {monster_hp}.")
elif roll> 10:
    print('you hit')
    attack=random.randint(1,8) + dmg_mod
    monster_hp-=attack
    print(f"you delt {attack} damage, the monster dropped to {monster_hp}.")
elif roll<=10:
    if roll==1:
        print("you killed the cleric, you're screwed")
    else:
        print("you missed")
else:
    print('HOW!?!??!')
print("your turn is over")