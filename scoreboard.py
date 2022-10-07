from turtle import Turtle

LEVEL_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.color("black")
        self.goto(-280, -280)
        self.write("Press space to cross the road.", align="left", font=("Courier", 12, "normal"))
        self.goto(-280, 260)
        self.write_level()

    def write_level(self):
        self.write(f"Level: {self.level}", align="left", font=LEVEL_FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=LEVEL_FONT)
