from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.level = 0
    
    def create_car(self):
        new_car = Turtle()
        self.hideturtle()
        new_car.shape("square")
        new_car.speed("fastest")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.left(180)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        ycor_spawn = random.randint(-250, 250)
        new_car.goto(300, ycor_spawn)
        self.cars.append(new_car)
        
    def car_forward(self):
        for i in self.cars:
            i.forward(MOVE_INCREMENT + self.level)

    def car_level_up(self):
        self.level +=10
    
