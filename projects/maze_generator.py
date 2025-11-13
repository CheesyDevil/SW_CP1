#SW 2nd Maze generator

import random
import turtle

visited=set()#set to hold all coordinates

turt=turtle.Turtle() #drawing turtle
turt_scout=turtle.Turtle() #checks all spaces

turt.speed(0)  # Fastest speed
turt_scout.speed(0)  # Fastest speed
turt_scout.hideturtle()  # Hide the scout turtle
turt.hideturtle()  # Hide the drawing turtle

turt.penup()# makes sure turtle only drraws when needed
turt_scout.penup()# makes sure scout never draws

turt.pencolor("white")#makes color white
turt.pensize(3)#makes maze coridors wider

screen=turtle.Screen()
screen.setworldcoordinates(-5,-5,35,35)#zooms in screen
screen.bgcolor("black")
screen.tracer(0)  # Turn off animation for faster drawing

while len(visited)<100:
    turt_scout.setheading(random.choice([0, 90, 180, 270]))
    turt_scout.forward(5)
    turt_coords=(f"{turt_scout.xcor()},{turt_scout.ycor()}")#coordinates of Scout turtle
    if turt_scout.xcor()<-5 or turt_scout.xcor()>35 or turt_scout.ycor()<-5 or turt_scout.ycor()>35:
        turt_scout.backward(5)
        
    if turt_coords in visited:
        turt_scout.backward(5)
    else:
        visited.add(f"{turt_coords}") #adds coordinates to visited 
        turt.setposition(turt_scout.xcor(), turt_scout.ycor())#moves drawing turtle
        turt.pendown()#makes the turtle draw
        turt.seth(turt_scout.heading()+180)#makes the turtle face the same direction 
        turt.forward(5)

screen.update()  # Show the final drawing
screen.mainloop()
