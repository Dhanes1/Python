from turtle import *
width_screen=int(input("Width of screen: "))
t = Turtle()
t.speed(30)
t.width(4)
screen = Screen()
screen.bgcolor("white")
screen.setup(width=width_screen,height=width_screen)
t.penup()
t.goto(-width_screen/2,width_screen/2)
t.pendown()
while width_screen > 0:
    t.forward(width_screen)
    t.right(90)
    t.forward(width_screen)
    t.right(90)
    width_screen-=10
done()
