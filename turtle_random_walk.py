from turtle import Turtle,Screen
from random import choice,randint

t=Turtle()
screen=Screen()
t.shape("turtle")

screen.colormode(255)
def random_color():
  r=randint(0,255)
  g=randint(0,255)
  b=randint(0,255)
  random_color=(r,g,b)
  return random_color

t.pensize(10)
t.speed(0)
angle=[90,180,270,0]

for i in range(200):
  t.color(random_color())
  t.seth(choice(angle))
  t.fd(20)

screen.exitonclick()
