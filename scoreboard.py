from turtle import Turtle

FONT = ("Courier", 13, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.level = 1
        self.penup()
        self.setposition(-230, 270)

        self.update_level()
        self.hideturtle()

    def update_level(self):
        self.write(f"Level {self.level}", False, align='center', font=FONT)
        print("work")
