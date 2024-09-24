from turtle import *
t = Turtle()
t.speed(30)
t.width(4)
screen = Screen()
screen.bgcolor("white")
screen.setup(width=800,height=800)
def square(r,g,b):
    t.color(r, g, b)
    for i in range(0,4):
        t.forward(100)
        t.right(90)
def triangle(r,g,b):
    #t.pencolor(r,g,b)
    for i in range(0,4):
        t.forward(100)
        t.left(120)
def triangle2():
    t.forward(40)
    t.left(150)
    t.forward(50)
    t.left(120)
    t.forward(30)
def circle(r,g,b):
    #t.pencolor(r, g, b)
    t.circle(-50)
def rectangle():
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
def spirograph(amount):
    for i in range(amount):
        t.circle(50)
        t.left(360/amount)
square(255, 255, 255)
# triangle(255,0,0)
# circle(0,0,255)
#triangle2()
#spirograph(40)
#rectangle()
done()