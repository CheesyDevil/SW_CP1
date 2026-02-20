#SW 2nd Lists Notes

names=["boy","child","man","manly Dan"]
import random

print(names[3])
print(random.choice(names))


#What are lists? 
  # A complex data type, that is a list of 
#How do you find the length of a list?
  # len(names)
#What data types can be put inside of lists?
  # Any data type
#How do you get one item from a list?
  # either declaring the one you want or using random choice 
#How do you replace a value in a list?
names[0] = ["george"]
print(names[0])
#What does append do?
  # adds to the end of a list
#What does insert do?
  # adds to a specific place
#what does extend do?
  # adds things to the list with preexisting data
#How do you remove an item from a list?
names.remove("child")