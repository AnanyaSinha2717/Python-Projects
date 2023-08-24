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
        # cars.inc_speed()
        # cars.move()

    #collision with car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()