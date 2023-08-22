from turtle import Turtle

class Line(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.ht()
        self.pu()
        self.color('white')
        self.goto(0, -280)
        self.seth(90)
        for _ in range(29):
            self.pd()
            self.fd(10)
            self.pu()
            self.fd(10)
            