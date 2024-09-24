import turtle
from turtle import *
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
screen.bgcolor("black")
turtle.pencolor("white")
turtle.speed(10)
turtle.penup()
turtle.goto(0,-200)
turtle.pendown()
turtle.setheading(90)
color=("red","green","blue","pink","yellow","violet")
turtle.pensize(20)
turtle.pencolor("green")
turtle.forward(200)
turtle.setheading(105)
def flower(length,size):
    turtle.pensize(size)
    for i in range(6):
        turtle.color(color[i])
        turtle.forward(length)
        turtle.right(150)
for i in range(2):
    flower(200,15)
turtle.pensize(10)
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.setheading(70)
turtle.pencolor("green")
for i in range(70):
    turtle.forward(2)
    turtle.right(1)
turtle.left(15)
for i in range(2):
    flower(70,5)
turtle.penup()
turtle.goto(0,-170)
turtle.pendown()
turtle.setheading(90)
turtle.pencolor("green")
for i in range(70):
    turtle.forward(2)
    turtle.left(1)
turtle.left(15)
for i in range(2):
    flower(50,5)
done()
