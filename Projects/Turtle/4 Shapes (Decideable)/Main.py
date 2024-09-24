from turtle import *
turtle=Turtle()
screen=Screen()
screen.setup(500,500)
turtle.speed(0)
print("""Pattern Menu:
    1. Diaomond
    2. Square
    3. Heart
    4. Hexagon      """)
user_input=int(input("Pick your shape: "))

if user_input==1:
    temp=170
    turtle.penup()
    turtle.goto(-210,170)
    turtle.pendown()
    for i in range(3):
        for i in range(6):
            turtle.setheading(55)
            turtle.forward(60)
            turtle.right(110)
            turtle.forward(60)
        for i in range(6):
            turtle.setheading(-125)
            turtle.forward(60)
            turtle.right(110)
            turtle.forward(60)
        turtle.penup()
        temp-=120
        turtle.goto(-210,temp)
        turtle.pendown()
elif user_input==2:
    temp=210
    turtle.penup()
    turtle.goto(-210,210)
    turtle.pendown()
    turtle.setheading(0)
    for i in range(3):
        for j in range(6):
            turtle.forward(50)
            turtle.right(90)
        turtle.left(180)
        for q in range(5):
            turtle.forward(50)
            turtle.right(90)
        turtle.left(180)
        for h in range(3):
            for j in range(7):
                turtle.forward(50)
                turtle.right(90)
            turtle.left(180)
            for q in range(5):
                turtle.forward(50)
                turtle.right(90)
            turtle.left(180)
        turtle.penup()
        temp-=120
        turtle.goto(-210,temp)
        turtle.pendown()
        turtle.setheading(0)
elif user_input==3:
    temp=160
    turtle.penup()
    turtle.goto(-210,160)
    turtle.pendown()
    turtle.setheading(90)
    for i in range(2):
        for i in range(2):# how many hearts
            for i in range(2):#how many 1/2 circle
                for i in range(180): # creating the circles
                    turtle.forward(0.9)
                    turtle.right(1)
                turtle.setheading(90)
        turtle.setheading(270)
        for i in range(2):#how many 1/2 circle
                for i in range(180): # creating the circles
                    turtle.forward(1.8)
                    turtle.right(1)
                turtle.setheading(270)
        turtle.penup()
        temp-=170
        turtle.goto(-210,temp)
        turtle.pendown()
        turtle.setheading(90)
elif user_input==4:
    temp=180
    turtle.penup()
    turtle.goto(-210,180)
    turtle.pendown()
    turtle.setheading(0)
    for i in range(2):
        for i in range(3):
            for i in range(8):
                turtle.forward(50)
                turtle.right(60)
            turtle.setheading(0)
            for i in range(8):
                turtle.forward(50)
                turtle.left(60)
            turtle.setheading(0)
        temp-=180
        turtle.penup()
        turtle.goto(-210,temp)
        turtle.pendown()
        turtle.setheading(0)
done()