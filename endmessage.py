from turtle import Turtle

class EndMessage(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.pencolor("white")

    def write_message(self, message):
        self.write(message, align="Center",font=("Arial", 30, "bold"))