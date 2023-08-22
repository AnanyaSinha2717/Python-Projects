from turtle import Turtle

class Score(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.write(f'Score : {self.score}', align='center', font=('Courier', 18, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Courier', 20, 'normal'))

    def score_calc(self):
        self.score += 1
        self.clear()
        self.write(f'Score : {self.score}', align='center', font=('Courier', 18, 'normal'))



        