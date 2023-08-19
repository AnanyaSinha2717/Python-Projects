from turtle import Turtle


POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIS = 20

class Snake:

    def __init__(self) :
        self.snake=[]
        self.createsnake()

    def createsnake(self):
        for i in POS:
            t=Turtle('square')
            t.color('brown')
            t.pu()
            t.goto(i)
            self.snake.append(t)

    def move(self):
        for seg in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[seg-1].xcor()
            new_y = self.snake[seg-1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.snake[0].fd(MOVE_DIS)

    def up(self):
        if self.snake[0].heading() != 270.0:
            self.snake[0].setheading(90)
        else:
            pass

    def down(self):
        if self.snake[0].heading() != 90.0:
            self.snake[0].setheading(270)
        else:
            pass

    def left(self):
        if self.snake[0].heading() != 0.0:
            self.snake[0].setheading(180)
        else:
            pass

    def right(self):
        if self.snake[0].heading() != 180.0:
            self.snake[0].setheading(0)
        else:
            pass