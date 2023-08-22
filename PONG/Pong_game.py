from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
from dashed_line import Line
import time

screen=Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG-PING')
screen.tracer(0)

line = Line()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_on=True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.xcor() > 380: #misses left
        ball.reset_pos()
        score.score_inc_l()

    elif ball.xcor() < -380: #misses right
        ball.reset_pos()
        score.score_inc_r()

    elif ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

screen.exitonclick()