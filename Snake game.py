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
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect collision with food
    if snake.snake[0].distance(food) < 18:
        food.refresh()
        snake.extend()
        score.score_calc()

    #detect collision with wall
    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280 or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:
        game_on = False
        
    #detect collision with tail
    for seg in snake.snake[1:]:
        if snake.snake[0].distance(seg) < 10:
            game_on=False
    
score.game_over()

screen.exitonclick()                                                   