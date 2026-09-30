from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self, position, speed):
        """Creates a paddle that has its origin at (x, y) position"""
        super().__init__()
        self.MOVEMENT = speed
        self.stretch = 4.0
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)
        self.shapesize(1.0, self.stretch)

    def move(self):
        """Moves paddle in set pre-set direction"""
        self.forward(self.MOVEMENT)

    def change_direction_up(self):
        self.setheading(UP)

    def change_direction_down(self):
        self.setheading(DOWN)

    def move_up(self, height):
        if self.ycor() <= height - 10*self.stretch:
            self.change_direction_up()
            self.move()

    def move_down(self, height):
        if self.ycor() >= height + 10*self.stretch:
            self.change_direction_down()
            self.move()

    def is_within_distance(self, ball, distance):
        if abs(self.xcor()) - abs(ball.xcor()) >= distance-3:
            if self.ycor() -10*self.stretch <= ball.ycor() <= self.ycor() + 10*self.stretch and abs(self.xcor() - ball.xcor()) <= distance:
                return True
        return False