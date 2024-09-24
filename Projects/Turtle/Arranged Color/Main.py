from turtle import *
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(0)
turtle.penup()
turtle.goto(-210,150)
turtle.pendown()
color_star=["Red", "Orange", "Yellow", "Green", "Blue"]
for i in range(5):
    turtle.forward(150)
    turtle.right(144)
    turtle.pencolor(color_star[i])
turtle.penup()
turtle.goto(120,80)
turtle.pendown()
color_pentagon=["Red", "Green", "Blue", "Purple", "Yellow", "Orange"]
for i in range(6):
    turtle.forward(80)
    turtle.left(72)
    turtle.pencolor(color_pentagon[i])
color_square=["Blue","Green","Yellow","Purple"]
length=90
turtle.penup()
turtle.goto(-150,-50)
turtle.pendown()
turtle.setheading(0)
temp=0
turtle.pensize(3)
turtle.pencolor('Purple')
for i in range(3):
    turtle.forward(100)
    turtle.right(90)
    turtle.pencolor(color_square[temp])
    temp+=1
for i in range(9):
    for i in range(2):
        turtle.forward(length)
        turtle.right(90)
        turtle.pencolor(color_square[temp])
        if temp==3:
            temp=-1
        temp+=1

    length-=10



color_spiral=["Blue","Green","Yellow","Purple","Red","Pink"]
length=1
turtle.penup()
turtle.goto(100,-80)
turtle.pendown()
turtle.setheading(0)
for i in range(20):
    for i in range(6):
        turtle.forward(length)
        turtle.right(61)
        turtle.pencolor(color_spiral[i])
        length+=1
done()