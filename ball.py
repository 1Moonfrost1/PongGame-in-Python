import random
from turtle import Turtle

class Ball(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.direction = 0
        self.set_initial_direction()
        self.MOVEMENT = speed

    def set_initial_direction(self):
        self.direction = random.randint(135, 225)
        self.setheading(self.direction)

    def refresh(self):
        self.goto(0,0)
        self.set_initial_direction()

    def collision_up_down(self):
        self.direction = 360 - self.direction
        self.setheading(self.direction)

    def collision_left_right(self):
        self.direction = (180 - self.direction)%360
        self.setheading(self.direction)

    def move(self):
        self.forward(self.MOVEMENT)

    def out_of_bounds(self, width):
        return not(-width/2 <= self.xcor() <= width/2)