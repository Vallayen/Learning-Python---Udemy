# def greet(name):
#   print("Hello "+name)
  
# player_input = input("What is your name?: ")

# greet(player_input)

# def info(fname, lname, age, gender):
#   print("Hello "+fname+" "+lname+"."+" You are "+age+" years old, and "+gender+".")
  
# first_name = input("What is your first name?: ")
# last_name = input("What is your last name?: ")
# old = input("How old are you?: ")
# identity = input("How do you Identify?: ")

# info(first_name, last_name, old, identity)


import math
import random


# PI = ""
# while PI != "Rock" or "Paper" or "Scissors":
#   PI = input("Rock, Paper, or Scissors? ")
#   if PI == "Rock" or "Paper" or "Scissors":
#     break
#   print(PI)


  
Choices = ["rock", "paper", "scissors"]
player = None
NPC = random.choice(Choices)


while player not in Choices:
  player = input("Rock or Paper or Scissors?: ").lower()
  if player == Choices:
    break


def play(NPC, player)
  if player == NPC:
    print "Its a tie!":
  elif NPC == "Rock" and player == "Paper":
    print('You Lose!')
  elif NPC == "Paper" and player == "Scissors":
    print('You Lose!')
  elif NPC == "Scissors" and player == "Rock":
    print('You Lose!')
  elif NPC =="Paper" and player == "Rock":
    print('You Win!')
  elif NPC == "Rock" and player == "Scissors":
    print('You Win!')
  elif NPC == "Scissors" and player == "Paper":
    print('You Win!')
  else:
    print("Something went wrong")

