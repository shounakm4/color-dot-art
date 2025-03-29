import random
from main import colour_list
from turtle import *
import turtle as t

tim = t.Turtle()
tim.hideturtle()
tim.penup()
tim.setpos(-200,-200)
my_screen = Screen()
t.colormode(255)
tim.speed(100)
for _ in range(10):
    for i in range(10):
        tim.dot(20,random.choice(colour_list))
        tim.penup()
        tim.forward(40)
        tim.pendown()
    tim.penup()
    tim.left(90)
    tim.forward(40)
    tim.left(90)
    tim.forward(400)
    tim.right(180)












my_screen.exitonclick()



