from turtle import *
length=250
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(15)
while length>10:
    turtle.penup()
    turtle.goto(-length,length)
    turtle.pendown()
    for i in range(4):
        turtle.forward(length*2)
        turtle.right(90)
    length-=10
done()