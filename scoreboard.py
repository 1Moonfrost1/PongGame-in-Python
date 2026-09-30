from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.pencolor("white")
        self.write_score()

    def write_score(self):
        self.write(f"{self.score}", font=("Arial", 50, "bold"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write_score()

    def get_score(self):
        return self.score