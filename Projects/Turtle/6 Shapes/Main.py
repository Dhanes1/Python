from turtle import *
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(0)
# square
turtle.penup()
turtle.goto(-230, 230)
turtle.pendown()
for i in range(4):
    turtle.forward(50)
    turtle.right(90)
# rectangle
turtle.penup()
turtle.goto(-150, 230)
turtle.pendown()
for i in range(2):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
# right angled triangle
turtle.penup()
turtle.goto(-20, 230)
turtle.pendown()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)
turtle.left(135)
turtle.forward(74)
# equilateral triangle
turtle.penup()
turtle.goto(60, 180)
turtle.pendown()
turtle.setheading(0)
turtle.forward(50)
for i in range(2):
    turtle.left(120)
    turtle.forward(50)
#circle
turtle.penup()
turtle.goto(165, 225)
turtle.pendown()
angle=0
for i in range(360):
    turtle.setheading(angle)
    angle-=1
    turtle.forward(0.4)
# pentagon
turtle.penup()
turtle.goto(-200, 80)
turtle.pendown()
turtle.setheading(0)
for i in range(5):
    turtle.forward(50)
    turtle.left(72)
# hexagon
turtle.penup()
turtle.goto(-80, 80)
turtle.pendown()
turtle.setheading(0)
for i in range(6):
    turtle.forward(45)
    turtle.left(60)
done()