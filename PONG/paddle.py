from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)
        else:
            pass

    def down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)
        else:
            pass


          