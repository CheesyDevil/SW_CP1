#SW 2nd Turtle race

import turtle
import random

screen=turtle.Screen()
screen.setworldcoordinates(-10,-10,50,50) #zooming in screen

t1=turtle.Turtle() #creating turtles
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()

t1.setposition(0,20) #puttling turtles in position
t2.setposition(0,15)
t3.setposition(0,10)
t4.setposition(0,5)
t5.setposition(0,0)
t6.setposition(40,0)

t1.pencolor("red")
t2.pencolor("green")
t3.pencolor("blue")
t4.pencolor("purple")
t5.pencolor("yellow")
t6.pencolor("black")

t6.hideturtle() 

t6.setheading(90)
t6.forward(20) #making finish line

racing=True
while racing: #game loop
    t1.forward(random.randint(0,2))
    t2.forward(random.randint(0,2))
    t3.forward(random.randint(0,2))
    t4.forward(random.randint(0,2))
    t5.forward(random.randint(0,2))
    if t1.xcor()==40:
        print("Turtle 1 has won")
        break
    if t2.xcor()==40:
        print("Turtle 2 has won")
        break
    if t3.xcor()==40:
        print("Turtle 3 has won")
        break
    if t4.xcor()==40:
        print("Turtle 4 has won")
        break
    if t5.xcor()==40:
        print("Turtle 5 has won")
        break