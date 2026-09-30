from paddle import Paddle

class LeftPaddle(Paddle):
    def __init__(self, position, speed):
        super().__init__(position, speed)

    def is_within_distance(self, ball, distance):
        """Distance represents the closest distance from wall's center to ball's center means a collision"""
        if self.ycor() - 10 * self.stretch <= ball.ycor() + 10 and ball.ycor() - 10 <= self.ycor() + 10 * self.stretch:
            if -20 <= self.xcor() - ball.xcor() <= -distance:
                    return True
        return False