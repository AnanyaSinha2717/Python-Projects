from turtle import Turtle

STARTING_POSITION = (0, -270)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 270


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.pu()
        self.go_to_start()
        self.seth(90)

    def move(self):
        self.goto(0, self.ycor() + MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def success(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
