# # The code `from turtle import Turtle, Screen` is importing the `Turtle` and `Screen` classes from
# the `turtle` module.
from turtle import Turtle, Screen
import random



timmy = Turtle()
timmy.color("green",)
timmy.shape("turtle")
timmy.speed(0)
timmy.pensize(10)

# for i in range(4):
#   timmy.forward(100)
#   timmy.left(90)

# tommy = Turtle()
# tommy.left(180)
# for i in range(4):
#   tommy.forward(100)
#   tommy.left(90)


# for i in range(15):
#   timmy.forward(35)
#   timmy.pencolor("white")
#   timmy.forward(35)
#   timmy.pencolor("black")

# num_side = 3
# def draw_shape(num_side):
#   angle = 360/num_side
#   for i in range(num_side):
#     timmy.forward(100)
#     timmy.right(angle)
    
# for n in range(3, 11):
#   draw_shape(n)


#draw random walk

screen = Screen()
screen.colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color_tupple = (r, g, b)
  return color_tupple

def random_direction():
  directions = [0, 90, 180, 270,]
  change = random.choice(directions)
  timmy.left(change)
  

# def random_walk(movements):
#   for i in range(movements):
#     timmy.forward(35)
#     random_direction()
#     timmy.color(random_color())
    

# random_walk(400)


# for i in range(90):
#   timmy.circle(100)
#   timmy.pencolor(random_color())
#   timmy.left(4)


def dots():
  timmy.penup()
  timmy.left(180)
  timmy.forward(150)
  timmy.left(90)
  timmy.forward(150)
  timmy.left(90)
  for i in range(10):
    dots_row()
    dots_new()

  
    
def dots_row():
  for i in range(10):
    timmy.color(random_color())
    timmy.pendown()
    timmy.forward(0)
    timmy.penup()
    timmy.forward(30)
    
def dots_new():
  timmy.penup()
  timmy.left(90)
  timmy.forward(30)
  timmy.left(90)
  timmy.forward(300)
  timmy.right(180)
  
  
dots()
#stay at the bottom--

screen.exitonclick()
