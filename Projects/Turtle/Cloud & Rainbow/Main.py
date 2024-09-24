import turtle
from turtle import *
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(0)
turtle.penup()
turtle.goto(100,200)
turtle.pendown()
def cloud(radius):
    turtle.setheading(0)
    turtle.pencolor("white")
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.forward(radius)
    turtle.circle(radius)
    turtle.end_fill()
    for i in range(3):
        turtle.begin_fill()
        turtle.right(90)
        turtle.circle(radius)
        turtle.end_fill()
def rainbow(radius,color):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.pensize(1)
    for i in range(180):
        turtle.forward(3.14*radius/180)
        turtle.left(1)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    for i in range(180):
        turtle.forward(3.14*(radius-10)/180)
        turtle.right(1)
    turtle.left(90)
    turtle.back(5)
    turtle.end_fill()

    turtle.left(90)
screen.bgcolor("lightblue")
rainbowcolor=["red","orange","yellow","green","blue","indigo","violet"]
cloud(20)
turtle.penup()
turtle.goto(-150,150)
turtle.pendown()
cloud(30)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
cloud(50)
turtle.penup()
turtle.goto(200,-100)
turtle.pendown()
cloud(10)
turtle.penup()
turtle.goto(240,-250)
turtle.pendown()
ia=0
for i in rainbowcolor:
    rainbow(radius,rainbowcolor[ia])
    ia+=1
    radius-=15
done()