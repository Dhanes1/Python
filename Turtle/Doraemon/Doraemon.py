from turtle import *
speed(300)
width(2)
shape('arrow')
bgcolor("white")
setup(width=500,height=500)
def draw_circle(radius,filled,line_color,filled_color):
    color(line_color,filled_color)
    pendown()
    if filled:
        begin_fill()
    circle(radius,360)
    if filled:
        end_fill()
def rectangle(length,width,filled,line_color,filled_color):
    color(line_color,filled_color)
    pendown()
    if filled:
        begin_fill()
    for i in range(2):
        forward(length)
        left(90)
        forward(width)
        left(90)
    if filled:
        end_fill()
# draw_circle(20,True,"black","blue")
# rectangle(50,20,True,"black","Green")
#hand
penup()
goto(37,-45)
setheading(-30)
pendown()
color("black","blue")
begin_fill()
forward(65)
left(90)
forward(25)
left(90)
forward(65)
end_fill()

penup()
goto(-37,-45)
setheading(-150)
pendown()
color("black","blue")
begin_fill()
forward(65)
left(-90)
forward(25)
left(-90)
forward(65)
end_fill()
#body
penup()
setheading(0)
goto(0,-140)
draw_circle(75,True,"black","blue")
penup()
goto(0,-113)
draw_circle(60,True,"black","white")
#HEAD
penup()
goto(0,-5)
draw_circle(70,True,"black","blue")
draw_circle(60,True,"black","white")
#Eyes
penup()
goto(12,100)
draw_circle(13,True,"black","white")
penup()
goto(-12,100)
draw_circle(13,True,"black","white")
penup()
goto(-6,107)
draw_circle(4,True,"black","black")
goto(6,107)
draw_circle(4,True,"black","black")
#Mouth
penup()
goto(-40,30)
setheading(-47)
pendown()
circle(55,100)
#nose
penup()
setheading(0)
goto(0,95)
draw_circle(6,True,"black","red")
#line
setheading(-90)
forward(80)
#leg
penup()
setheading(0)
goto(37,-145)
draw_circle(15,True,"black","white")
penup()
goto(-37,-145)
draw_circle(15,True,"black","white")
#hand circle
penup()
goto(-97,-78)
draw_circle(15,True,"black","white")
penup()
goto(97,-78)
draw_circle(15,True,"black","white")
#whiskers
penup()
goto(-5,70)
pendown()
goto(-26,84)

penup()
goto(-5,57)
pendown()
goto(-26,57)

penup()
goto(-5,47)
pendown()
goto(-26,33)


penup()
goto(5,70)
pendown()
goto(26,84)

penup()
goto(5,57)
pendown()
goto(26,57)

penup()
goto(5,47)
pendown()
goto(26,33)
#pocket
penup()
goto(-35,-49)
pendown()
setheading(-90)
circle(35,180)
setheading(180)
forward(70)
done()