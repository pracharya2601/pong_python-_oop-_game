from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self._x = 10
        self._y = 10
        self.ball_speed = 0.1

    def move(self):
        _x = self.xcor() - self._x
        _y = self.ycor() - self._y
        self.goto(_x, _y)

    def bounce_y(self):
        self._y *= -1
        self.ball_speed *= 0.95

    def bounce_x(self):
        self._x *= -1
        self.ball_speed *= 0.95

    def reset_pos(self):
        self.ball_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()

    def increase_speed(self):
        self.ball_speed *= 0.8

    def decrease_speed(self):
        self.ball_speed /= 0.8
