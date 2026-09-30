from turtle import Turtle

class Midline(Turtle):
    def __init__(self, HEIGHT):
        super().__init__()
        self.hideturtle()
        self.HEIGHT = HEIGHT
        self.penup()
        self.goto((0, -HEIGHT/2))
        self.pendown()
        self.color("white")
        self.setheading(90)
        self.drawline()

    def drawline(self):
        while self.ycor()<=self.HEIGHT/2:
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()