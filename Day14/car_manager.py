COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from random import randint, choice
from turtle import Turtle

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_len=2)
        new_car.color(choice(COLORS))
        new_car.penup()
        random_y = randint(-250, 250)
        new_car.goto(300, random_y)
        self.all_cars.append(new_car)
    
    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)