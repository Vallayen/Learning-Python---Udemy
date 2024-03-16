from turtle import Turtle
import random

class Ball(Turtle):
  
  def __init__(self):
      super().__init__()
      self.penup()
      self.color('white')
      self.shape("square")
      self.goto(0, 0)  # Start at the center
      self.x_move = 6  # Initial movement step in x
      self.y_move = 4  # Initial movement step in y
      self.collide = False
      
      
  def move(self):
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(new_x, new_y)

  def bounce_y(self):
      self.y_move *= -1
      self.collide = False

  def bounce_x(self):
      self.x_move *= -1
      self.collide = False

  def reset_position(self):
      self.goto(0, 0)
      self.collide = False
      starting_directions = [45, 135, 225, 315, 360, 170]  # Example directions
      self.setheading(random.choice(starting_directions))

      