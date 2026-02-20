#SW 2nd Maze generator

import turtle
import random

visited=set()#set to hold all coordinates

turt=turtle.Turtle() #drawing turtle
turt_scout=turtle.Turtle() #checks all spaces

screen=turtle.Screen()
screen.setworldcoordinates(-5,-5,35,35)



while len(visited)<=36:
    turt_scout.setheading(random.randint(0,270,90))
    turt_scout.forward(random.randint(0,5))
    turt_coords=(f"{turt_scout.xcor},{turt_scout.ycor}")#coordinates of Scout turtle
    
    visited.add(f"{turt_coords}") #adds coordinates to visited
    if turt_coords in visited:
        continue
    else:
        visited.add(f"{turt_coords}") #adds coordinates to visited    
        