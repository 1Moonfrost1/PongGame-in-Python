import time
from turtle import Screen
from ball import Ball
from paddle import Paddle

WIDTH = 800
HEIGHT = 600

left_paddle = Paddle((-WIDTH/2 + 20, 0), 20)
right_paddle = Paddle((WIDTH/2 - 25, 0), 5)
ball = Ball(4)
screen = Screen()
screen.bgcolor("black")
screen.title("PongGame")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

screen.listen()
screen.onkeypress(key="w", fun= lambda :left_paddle.move_up(HEIGHT / 2 - 20))
screen.onkeypress(key="s", fun= lambda: left_paddle.move_down(- HEIGHT / 2 + 20))

right_paddle.change_direction_up()

while True:
    screen.update()
    time.sleep(0.01)

    right_paddle.move()
    ball.move()

    if right_paddle.ycor() > HEIGHT / 2 - 10*right_paddle.stretch:
        right_paddle.change_direction_down()
    elif right_paddle.ycor() < - HEIGHT / 2 + 10*right_paddle.stretch:
        right_paddle.change_direction_up()

    if HEIGHT / 2 - 20 < ball.ycor() or ball.ycor() < - HEIGHT / 2 + 20 :
        ball.collision_up_down()

    if left_paddle.is_within_distance(ball, 20) or right_paddle.is_within_distance(ball, 20):
        ball.collision_left_right()

    if ball.out_of_bounds(WIDTH):
        ball.refresh()
