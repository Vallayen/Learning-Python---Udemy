
from turtle import Turtle

class Snake:
  def __init__(self):
    self.segments = []
    self.create_snake()
    
    
    
  def create_snake(self):
    for i in range(3):
      self.add_segment()
      
      
      
  def move(self):
    for i in range(len(self.segments) - 1, 0, -1):
      new_x = self.segments[i - 1].xcor()
      new_y = self.segments[i - 1].ycor()
      self.segments[i].goto(new_x, new_y)
    self.segments[0].forward(20)
  
    
  def up(self):
      if self.segments[0].heading() != 270:  # Prevent backward movement
          self.segments[0].setheading(90)

  def down(self):
      if self.segments[0].heading() != 90:  # Prevent backward movement
          self.segments[0].setheading(270)

  def left(self):
      if self.segments[0].heading() != 0:  # Prevent backward movement
          self.segments[0].setheading(180)

  def right(self):
      if self.segments[0].heading() != 180:  # Prevent backward movement
          self.segments[0].setheading(0)
          
  def extend(self):
    self.add_segment(self.segments[-1].position())
    
  def add_segment(self):
    seg = Turtle("square")
    seg.penup()
    seg.color("white")
    seg.setpos(-20 * len(self.segments), 0)
    self.segments.append(seg)
    
  def reset(self):
    for i in self.segments:
      i.hideturtle()
    self.segments.clear()
    self.create_snake()
    