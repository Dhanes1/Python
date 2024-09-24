import turtle
from turtle import *
import random
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(0)
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.shape("turtle")
angle=random.randint(45,135)
turtle.setheading(angle)
turtle.color("red")
turtle.width(5)
colnum=1
color=["red","orange","yellow","green","blue","indigo","violet"]
while True:
    turtle.setheading(angle)
    turtle.forward(1)
    if turtle.xcor()>=250 or turtle.xcor()<=-250:
        turtle.color(color[colnum])
        colnum+=1
        angle=180-angle
    if turtle.ycor()>=250 or turtle.ycor()<=-250:
        turtle.color(color[colnum])
        colnum+=1
        angle=360-angle
    if colnum==7:
        colnum=0