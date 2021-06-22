from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

import time

_t = Turtle()
_s = Screen()
_s.bgcolor('black')
_s.setup(width=1000, height=600)
_s.title("Pong Game")
_s.tracer(0)

_r_p = Paddle((450, 0))
_l_p = Paddle((-450, 0))
_ball = Ball()
_scoreboard = Score()

_s.listen()
_s.onkey(_r_p.go_up, 'Up')
_s.onkey(_r_p.go_down, 'Down')

_s.onkey(_l_p.go_up, 'w')
_s.onkey(_l_p.go_down, 's')

_s.onkey(_ball.increase_speed, 'u')
_s.onkey(_ball.decrease_speed, 'd')

game_on = True
while game_on:
    time.sleep(_ball.ball_speed)
    _s.update()
    _ball.move()

    # detection of collision
    if _ball.ycor() > 270 or _ball.ycor() < -270:
        # bounce the ball
        _ball.bounce_y()

    # detect collision with paddle with right paddle
    if _ball.xcor() > 420 and _ball.distance(_r_p) < 50 or _ball.xcor() < -420 and _ball.distance(_l_p) < 50:
        # contact with right paddle detection
        _ball.bounce_x()

    # ball lose detection
    if _ball.xcor() > 460:
        # right side lose the ball
        _ball.reset_pos()
        _scoreboard.l_point()

    if _ball.xcor() < -460:
        # left side lose the ball
        _ball.reset_pos()
        _scoreboard.r_point()

    # check the total round count
    if _scoreboard.l_score > 10 or _scoreboard.r_score > 10:
        _ball.reset_pos()
        game_on = False
        _scoreboard.game_over()

_s.exitonclick()
