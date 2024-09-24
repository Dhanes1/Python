from turtle import *
sides=int(input("Sides of the polygon: "))
t = Turtle()
t.speed(30)
t.width(4)
screen = Screen()
screen.bgcolor("white")
screen.setup(width=500,height=500)
for i in range(sides):
    t.forward(40)
    t.left(360/sides)
done()
