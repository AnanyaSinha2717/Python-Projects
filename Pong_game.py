from turtle import Screen, Turtle

screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG-PING')

t = Turtle()
t.ht()
t.pencolor('white')
t.pu()
t.goto(0, -300)
t.seth(90)
for _ in range(30):
    t.fd(10)
    t.pu()
    t.fd(10)
    t.pd()

screen.exitonclick()