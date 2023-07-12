from turtle import Turtle,Screen
from random import choice

t=Turtle()
screen=Screen()

'''
for i in range(40):
  t.pd()
  t.fd(10)
  t.pu()
  t.fd(10)
'''
color=['forest green', 'steel blue', 'navy', 'magenta', 'indigo', 'orange red']
for i in range(3,11):
  t.color(choice(color))
  for x in range(i):
    t.right(360/i)
    t.fd(100)
    
screen.exitonclick()
