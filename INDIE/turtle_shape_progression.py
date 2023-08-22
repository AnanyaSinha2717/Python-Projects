from turtle import Turtle,Screen
from random import choice,randint

t=Turtle()
screen=Screen()
t.shape("turtle")
t.speed('fast')

screen.colormode(255)
def random_color():
  r=randint(0,255)
  g=randint(0,255)
  b=randint(0,255)
  random_color=(r,g,b)
  return random_color

for i in range(3,11):
  t.color(random_color())
  for x in range(i):
    t.right(360/i)
    t.fd(100)

screen.exitonclick()
