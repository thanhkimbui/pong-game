from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # For left player
        self.goto(-150, 200)
        self.write(self.l_score, False, align="center", font=("Courier", 50, 'bold'))

        # For right player
        self.goto(150, 200)
        self.write(self.r_score, False, align="center", font=("Courier", 50, 'bold'))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()