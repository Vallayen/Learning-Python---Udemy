import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

#Turtle Init
timmy = Player()

#Car init
car = CarManager()

#score Init
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkeypress(timmy.move, "Up")
    
    
    
    #car collision:
    for i in car.cars:
      if timmy.distance(i) < 20:
        game_is_on = False
        screen.clear()
        score.game_over()
    
    #create cars
    if random.randint(1, 6) == 1:
      car.create_car()
      
    car.car_forward()

    #wall collision logic
    if timmy.ycor() > 280:
      timmy.refresh_turtle()
      car.car_level_up()
      score.level_up()
      
#stay @ bottom
screen.exitonclick()
