from turtle import *
import random
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(0)
turtle.penup()
turtle.goto(-130,130)
turtle.pendown()
colormode(255)
for i in range(6):
    for i in range(6):
            turtle.forward(50)
            turtle.right(60)
    turtle.right(60)
    turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
turtle.penup()
turtle.goto(70,6)
turtle.pendown()
for i in range(5):
    for i in range(7):
        turtle.forward(50)
        turtle.left(72)
    turtle.right(72)
    turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
turtle.penup()
turtle.goto(140,-60)
turtle.pendown()
turtle.setheading(0)
temp=72
for i in range(6):
     for i in range(4):
          turtle.forward(30)
          turtle.left(120)
          turtle.pencolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
          
     turtle.right(180)
done()