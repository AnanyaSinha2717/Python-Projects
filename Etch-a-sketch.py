from turtle import Turtle, Screen

t=Turtle()
screen=Screen()

def move_fd():
    t.fd(20)

def move_bk():
    t.bk(20)

def move_counter():
    new = t.heading() + 10
    t.seth(new)

def move_clock():
    new = t.heading() - 10
    t.seth(new)

def clear_slate():
    t.reset()


screen.listen()
screen.onkey(key='w', fun=move_fd)
screen.onkey(key='s', fun=move_bk)
screen.onkey(key='a', fun=move_counter)
screen.onkey(key='d', fun=move_clock)
screen.onkey(clear_slate, 'c')

screen.exitonclick()