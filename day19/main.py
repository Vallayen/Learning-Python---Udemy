from turtle import Turtle
from turtle import Screen
import random


# timmy = Turtle()

screen = Screen()
screen.setup(width=500, height=400)
screen.title("Welcome to the Turtle Grand Race")

bet = screen.textinput(title="Make your bet", prompt="Would you like to bet on Timmy, Tommy, Janet, Brad, or Tichondrius")
print("bet: ", bet)
def random_move():
  x = random.randint(0, 10)
  return x

def check_winner():
  print("winner: ", winner)
  if winner == bet.lower():
    screen.textinput(title="Results", prompt="You were right, well done!")
  else:
    cwin = winner.title()
    screen.textinput(title="Results", prompt="The winner is " + cwin + "\nYou chose........Poorly")

timmy = Turtle()
timmy.penup()
timmy.goto(x=-200, y=-75)
timmy.shape("turtle")
timmy.color("green")

tommy = Turtle()
tommy.penup()
tommy.goto(x=-200, y=-150)
tommy.shape("turtle")
tommy.color("red")

janet = Turtle()
janet.penup()
janet.goto(x=-200, y=75)
janet.shape("turtle")
janet.color("pink")


brad = Turtle()
brad.penup()
brad.goto(x=-200, y=150)
brad.shape("turtle")
brad.color("orange")

tichondrius = Turtle()
tichondrius.penup()
tichondrius.goto(x=-200, y=0)
tichondrius.shape("turtle")
tichondrius.color("blue")

winner = ""
no_win = False
if bet:
  no_win = True
while no_win:

  timmy.forward(random_move())
  if timmy.xcor() > 230:
    print("Timmy wins")
    winner = "timmy"
    break
  tommy.forward(random_move())
  if tommy.xcor() > 230:
    print("Tommy wins")
    winner = "tommy"
    break
  janet.forward(random_move())
  if janet.xcor() > 230:
    print("Janet wins")
    winner = "janet"
    break
  brad.forward(random_move())
  if brad.xcor() > 230:
    print("Brad wins")
    winner = "brad"
    break
  tichondrius.forward(random_move())
  if tichondrius.xcor() > 230:
    print("Tichondrius wins")
    winner = "tichondrius"
    break
  
check_winner()







screen.exitonclick()