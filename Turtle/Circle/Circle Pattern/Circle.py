from turtle import *
r=250
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(15)
while r > 10:
    turtle.penup()
    turtle.goto(0,-r)
    turtle.pendown()
    turtle.circle(r)
    r-=10
done()