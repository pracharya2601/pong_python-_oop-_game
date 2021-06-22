from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.winner = ""
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="Center", font=("Arial", 50, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="Center", font=("Arial", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_score_board()

    def r_point(self):
        self.r_score += 1
        self.update_score_board()

    def game_over(self):
        self.check_winner()
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Arial", 20, "normal"))
        self.goto(0, -30)
        self.write(f"{self.winner} is the winner.", align="center", font=("Arial", 20, "normal"))

    def check_winner(self):
        if self.l_score > self.r_score and self.l_score > 10:
            self.winner = "Left side"
        if self.r_score > self.l_score and self.r_score > 10:
            self.winner = "Right side"



