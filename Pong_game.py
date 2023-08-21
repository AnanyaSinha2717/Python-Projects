from turtle import Screen
from pong_screen import Setup

screen=Screen()               #problem arising
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG-PING')

setup=Setup()



screen.exitonclick()