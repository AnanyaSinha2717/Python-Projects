from turtle import Turtle

class Setup:
    
    t = Turtle()
    t.ht()
    t.speed('fastest')
    t.pencolor('white')
    t.pu()
    t.goto(0, -300)
    t.seth(90)
    for _ in range(30):
        t.fd(10)
        t.pu()
        t.fd(10)
        t.pd()