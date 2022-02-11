from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as d:
            self.high_score = int(d.read())        
        self.penup()
        self.goto(0, 260)
        self.update_score()
        self.hideturtle()
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as d:
                d.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER",False, align=ALIGNMENT, font=FONT) 
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}",False, align=ALIGNMENT, font=FONT)        
    def increase_score(self):
        self.score  += 1
        self.update_score()




