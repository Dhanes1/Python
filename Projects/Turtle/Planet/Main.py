import turtle
from turtle import *
turtle=Turtle()
turtle1=Turtle()
turtle2=Turtle()
turtle3=Turtle()
turtle4=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(0)
turtle.penup()
turtle.goto(0,-75)
turtle.pendown()
colormode(255)
bgcolor("black")
sun=[255,204,51]
mercury=[151,151,159]
venus=[211,156,126]
earth=[140,177,222]
mars=[198,123,92]
turtle.color(sun)
turtle1.color(sun)
turtle2.color(sun)
turtle3.color(sun)
turtle4.color(sun)
#SUN
turtle.fillcolor(sun)
turtle.begin_fill()
turtle.circle(100)
turtle.end_fill()
turtle.goto(0,-45)
#MERCURY
turtle1.shape("circle")
turtle1.penup()
turtle1.goto(0,-100)
turtle1.pendown()
turtle1.color(mercury)
turtle1.circle(125)
#VENUS
turtle2.shape("circle")
turtle2.penup()
turtle2.goto(0,-125)
turtle2.pendown()
turtle2.color(venus)
turtle2.circle(150)
#EARTH
turtle3.shape("circle")
turtle3.penup()
turtle3.goto(0,-150)
turtle3.pendown()
turtle3.color(earth)
turtle3.circle(175)
#MARS
turtle4.shape("circle")
turtle4.penup()
turtle4.goto(0,-175)
turtle4.pendown()
turtle4.color(mars)
turtle4.circle(200)
#ROTATE
while True:
    for i in range(360):
        turtle1.forward(2.17*4)
        turtle1.left(4)
        turtle2.forward(2.6*2)
        turtle2.left(2)
        turtle3.forward(3.055)
        turtle3.left(1)
        turtle4.forward(3.445/2)
        turtle4.left(0.5)