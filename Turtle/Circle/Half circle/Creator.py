from turtle import *
user_input=int(input("Lines: "))
t = Turtle()
t.speed(30)
t.width(4)
screen = Screen()
screen.bgcolor("white")
screen.setup(width=500,height=500)
for i in range(user_input):
    t.forward(200)
    t.backward(200)
    t.left(180/(user_input-1))
done()