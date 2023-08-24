from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.goto(STARTING_POSITION)
        self.seth(90)

    def move(self):
        if self.ycor() < FINISH_LINE_Y:
            self.goto(0, self.ycor() + MOVE_DISTANCE)
        elif self.ycor() == FINISH_LINE_Y:
            self.goto(0, -FINISH_LINE_Y)
            self.seth(90)