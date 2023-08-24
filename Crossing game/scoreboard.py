from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.ht()
        self.penup()
        self.goto(-250, 260)
        self.level = 1
        self.write(f'Level: {self.level}' , align='left', font=FONT)

    def level(self):
        self.level += 1
        self.clear()
        self.write(f'Level: {self.level}' , align='left', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER' , align='center', font=FONT)
