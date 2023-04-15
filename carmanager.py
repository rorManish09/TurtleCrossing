import random
from turtle import Turtle
CAR_POSITION_X = 340
MOVE_INCREMENT = 10
CAR_COLOR = ["red", "green", "yellow", "blue", "orange", "purple"]
STARTING_MOVE_DISTANCE = 10



class CarManager(Turtle):

    def __init__(self):
        self.all_cars = []

        self.CAR_SPEED = 10
    def create_car(self):

        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.color(random.choice(CAR_COLOR))
            random_y = random.randint(-240, 240)
            new_car.goto(CAR_POSITION_X, random_y)
            new_car.forward(self.CAR_SPEED)
            self.all_cars.append(new_car)

    def move_cars(self):

        for cars in self.all_cars:

            cars.forward(self.CAR_SPEED)

    def level_up(self):

        self.CAR_SPEED += MOVE_INCREMENT