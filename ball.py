from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("white")
        self.penup()
        self._x = 10
        self._y = 10

    def move(self):
        _x = self.xcor() - self._x
        _y = self.ycor() - self._y
        self.goto(_x, _y)

    def bounce_y(self):
        self._y *= -1

    def bounce_x(self):
        self._x *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.bounce_x()
