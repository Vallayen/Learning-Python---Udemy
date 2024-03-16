from turtle import Turtle


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.color("white")
    self.score = 0
    self.hideturtle()
    self.goto(0, 260)
    # self.highscore = 0
    with open("highscore.txt") as file:
      self.highscore = int(file.read())
      
    self.update()
    
  def update(self):
    self.clear()
    self.write(arg="score = " + str(self.score) + "       Highscore = " + str(self.highscore), align="center",font=("Arial", 15, "normal"))
  
  def increase_score(self):
    self.score +=1
    self.update()
    
  def reset(self):
    self.score = 0
    self.update()
    
    
  def commit_highscore(self):
    if self.score > self.highscore:
      self.highscore = self.score
      with open("highscore.txt", mode="w") as file:
        file.write(str(self.highscore))

    
  # def game_over(self):
  #   self.clear()
  #   self.write(arg="Game Over, You lose. Your score was: " + str(self.score), align="center",font=("Arial", 15, "normal"))