from turtle import Turtle, Screen
import random

# Initializing the turtle
t = Turtle()
my = Screen()
my.colormode(255)
t.speed('fastest')

def random_color():
    red = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (red, g, b)
    return rand_color

for i in range(60):
    r = 50
    t.color(random_color())
    t.circle(r)
    t.lt(6)

my.exitonclick()
