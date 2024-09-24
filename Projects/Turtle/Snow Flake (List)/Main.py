import turtle
from turtle import *
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(0)
turtle.setheading(90)
color=("red","orange","yellow","green","blue","navy","cyan","pink")
def snowflake(length,small_length,color):
    temp_1=length/4
    for i in range(8):
        turtle.pencolor(color[i])
        turtle.forward(length)
        for i in range(3):
            turtle.back(temp_1)
            turtle.left(45)
            turtle.forward(small_length)
            turtle.back(small_length)
            turtle.right(90)
            turtle.forward(small_length)
            turtle.back(small_length)
            turtle.left(45)
        turtle.back(25)
        turtle.right(45)
        
snowflake(100,20,color)
done()