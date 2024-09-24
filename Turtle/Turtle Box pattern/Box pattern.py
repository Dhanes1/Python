from turtle import *
y=240
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(15)
for a in range(5):
    turtle.penup()
    turtle.goto(-250,y)
    for k in range(5):
        turtle.forward(10)
        turtle.pendown()

        for i in range(4):
            turtle.forward(80)
            turtle.right(90)
        turtle.penup()
        turtle.forward(90)
    y -= 100
        #turtle.pendown()

done()