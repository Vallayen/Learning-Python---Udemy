from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-230, 260)
        self.speed("fastest")
        self.write_score()
        
    def write_score(self):
        self.write(arg=f"Score {self.score}", align="center", font=FONT)
        
    def level_up(self):
        self.clear()
        self.score += 1
        self.write_score()
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(arg=f"Game over, your score is: {self.score}", align="center", font=FONT)
        
    
    
