from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_score()

    def update_score(self):
        self.goto(-100, 240)
        self.write(self.score_l, align='center', font=('Courier', 40, 'normal'))
        self.goto(100, 240)
        self.write(self.score_r, align='center', font=('Courier', 40, 'normal'))


    def score_inc_r(self):
        self.score_r += 1
        self.clear()
        self.update_score()

    def score_inc_l(self):
        self.score_l += 1
        self.clear()
        self.update_score()
