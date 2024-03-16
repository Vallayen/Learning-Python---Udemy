from turtle import Turtle

class Ai_paddle(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.speed("fastest")
    self.color("white")
    self.shape("square")
    self.goto(750, 0)
    self.shapesize(stretch_wid=7, stretch_len=1, outline=None)
    
    
  def move_up(self):
    ycor = self.ycor()
    xcor = self.xcor()
    self.goto(xcor, ycor + 3.75)
    
  def move_down(self):
    ycor = self.ycor()
    xcor = self.xcor()
    self.goto(xcor, ycor - 3.75)