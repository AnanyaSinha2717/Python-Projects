from turtle import Turtle

STARTING_POSITIONS = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
MOVE_DIS = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__(self)
        
