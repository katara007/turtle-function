from turtle import *
import turtle


speed(0)
penup()
setheading(180)
forward(300)
setheading(0)
pendown()
for i in range(1,5):
    color('black','red')

    left(90)
    forward(200)
    right(45)
    forward(100)
    right(90)
    forward(100)
    right(45)
    forward(200)
    penup()
    right(90)
    forward(50)
    right(90)
    forward(100)
    pendown()

    begin_fill()
    circle(30)
    end_fill()
    penup()
    right(180)
    forward(100)
    left(90)
    forward(50)
    pendown()
    forward(10)




done()