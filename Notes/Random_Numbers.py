#SW 2nd Random Numbers Notes

#Can computers really generate a "random" number?
  #No it uses arbitrary stuff to make it har to predict
#What is a python library?
  #A collction of prebuilt algorithms that we can access
#What are functions?
  #a collection of code that runs an algorithm
#How do you call a function?
  #nameoflibrary.nameoffunction()
#What have we already learned that is similar to a function?
  # methods
#What function to I call to get a random number?
  #.random
#What are arguments?
  #the paramiters for the function
#What arguments are needed to generate a random number:
  # 2 numbers

import random

print(random.random())# Float between 0 and 1
print(random.randint(1,6)) # Integer between the 2 numbers you put down

name=input("what is your name? \n").strip().title()