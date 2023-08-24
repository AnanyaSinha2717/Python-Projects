from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


game_on = True
class CarManager():
    def __init__(self):
        
        self.all_cars = []

    def generate(self):
        random_chance = random.randint(1,6)
        if random_chance==1:
            new_car=Turtle('square')
            new_car.pu()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-230, 230)
            new_car.goto(300, y_cor)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def inc_speed(self):
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT