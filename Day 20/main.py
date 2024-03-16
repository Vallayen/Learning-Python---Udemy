
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Screen Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.title("Snake Game")
screen.tracer(0)

#snake setup
snake = Snake()

#food initialize
food = Food()

#scoreboard
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")

#starting snake


#food collision


#main game loop

game = True
while game:
  screen.update()
  time.sleep(0.1)
  snake.move()
  
  #wall collision
  if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() > 295 or snake.segments[0].ycor() < -295:
    # game = False
    score.commit_highscore()
    score.reset()
    snake.reset()
    
  #tail collision
  for segment in snake.segments[1:]:
    if snake.segments[0].distance(segment) < 10:
      # game = False
      score.commit_highscore()
      score.reset()
      snake.reset()
    
  #detect collision food
  if snake.segments[0].distance(food) < 15:
    food.refresh()
    score.increase_score()
    snake.add_segment()
    
  
#stay at bottom:
screen.exitonclick()