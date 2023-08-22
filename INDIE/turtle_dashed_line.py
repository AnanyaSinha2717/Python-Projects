from turtle import Turtle,Screen
from random import choice

t=Turtle()
screen=Screen()
t.shape("turtle")

for i in range(15):
  t.pd()
  t.fd(10)
  t.pu()
  t.fd(10)

screen.exitonclick()
