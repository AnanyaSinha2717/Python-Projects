import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

cars = CarManager()
player = Player()
score = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate()
    cars.move()

    if player.ycor() == 270:
        score.level()

    #collision with car
    elif player.distance(cars) < 28:
        score.game_over()
        game_is_on = False

screen.exitonclick()