import time
from turtle import Screen
from endmessage import EndMessage
from ball import Ball
from leftpaddle import LeftPaddle
from midline import Midline
from rightpaddle import RightPaddle
from scoreboard import Scoreboard

WIDTH = 800
HEIGHT = 600
FINAL_SCORE = 10

left_paddle = LeftPaddle((-WIDTH/2 + 20, 0), 20)
left_score = Scoreboard((-110, HEIGHT/2 - 80))
right_paddle = RightPaddle((WIDTH/2 - 25, 0), 5)
right_score = Scoreboard((60, HEIGHT/2 - 80))
midline = Midline(HEIGHT)
endTurtle = EndMessage()

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

    if left_paddle.is_within_distance(ball, 10) or right_paddle.is_within_distance(ball, 10):
        ball.collision_left_right()

    if ball.out_of_left_bound(WIDTH):
        right_score.update_score()
        ball.refresh()

    if ball.out_of_right_bound(WIDTH):
        left_score.update_score()
        ball.refresh()

    if left_score.get_score() > FINAL_SCORE:
        endTurtle.write_message("You Win!")
        screen.update()
        screen.exitonclick()
        break

    if right_score.get_score() > FINAL_SCORE:
        endTurtle.write_message("You Lose!")
        screen.update()
        screen.exitonclick()
        break