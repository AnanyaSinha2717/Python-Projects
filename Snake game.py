from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Feed the Snake')
screen.tracer(0)

snake=Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with food
    if snake.snake[0].distance(food) < 18:
        food.refresh()
        score.score_calc()
    

screen.exitonclick()                                                   