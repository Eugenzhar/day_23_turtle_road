import random
import time
from turtle import Turtle


COLORS = ["red", "orange", "brown", "blue", "green"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.goto(300, random.randint(-250, 250))

    def create_car(self):
        if random.randint(1, 7) == 1:
            car = Cars()
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

