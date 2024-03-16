from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.playerscore = 0
        self.aiscore = 0
        self.color("White")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.update_scoreboard()  # Call a method to update the scoreboard initially

    def update_scoreboard(self):
        self.clear()  # Clear the scoreboard to update it
        # Player score
        self.goto(-120, 250)
        self.write(arg=str(self.playerscore), align="center", font=("Arial", 40, "normal"))
        # AI score
        self.goto(120, 250)
        self.write(arg=str(self.aiscore), align="center", font=("Arial", 40, "normal"))

    def player_score_up(self):
        self.playerscore += 1
        self.update_scoreboard()  # Update the scoreboard with new scores

    def ai_score_up(self):
        self.aiscore += 1
        self.update_scoreboard()  # Update the scoreboard with new scores
        
        
    def game_over(self):
      if self.playerscore == 7:
        winner = "You"
      if self.aiscore == 7:
        winner = "The computer"
      self.clear()
      self.goto(0,0)
      self.write(arg=f"the game is over, the winner is: {winner}", align="center", font=("Arial", 35, "normal"))