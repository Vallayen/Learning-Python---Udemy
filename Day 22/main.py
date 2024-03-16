from turtle import Turtle, Screen
from ai_paddle import Ai_paddle
from ball import Ball
from player_paddle import Player_paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(1600, 1000)
screen.listen()

#player paddle
paddle = Player_paddle()

#ai paddle
ai_paddle = Ai_paddle()

#ball
ball = Ball()

#paddle movement
screen.onkeypress(paddle.move_up, "Up")
screen.onkeypress(paddle.move_down, "Down")

#Scoreboard Init
score = Scoreboard()



#game logic
game = True
screen.tracer(0)
screen.delay(1)
while game:
  ball.move()
  

  #ai paddle logic
  if ai_paddle.ycor() > ball.ycor():
    ai_paddle.move_down()
  if ai_paddle.ycor() < ball.ycor():
    ai_paddle.move_up()

    #bounce Logic
  # Ball Collision with Player Paddle
  if paddle.distance(ball) < 50:
        ball.bounce_x()
    # Ball Collision with AI Paddle
  elif ai_paddle.distance(ball) < 50:
        ball.bounce_x()
    # Wall Collision Logic
  elif ball.ycor() > 490 or ball.ycor() < -490:
        ball.bounce_y()
        
  if paddle.ycor() > 450:
      paddle.goto(-750,420)
  if paddle.ycor() < -450:
      paddle.goto(-750,-420)
      
      
    #wall collision (score)
  if ball.xcor() > 790:
      ball.reset_position()
      score.clear()
      score.player_score_up()
      if score.playerscore == 7:
        ai_paddle.color("black")
        paddle.color("black")
        ball.color("black")
        game = False
        score.game_over()


  if ball.xcor() < - 790:
      ball.reset_position()
      score.clear()
      score.ai_score_up()
      if score.aiscore == 7:
        ai_paddle.color("black")
        paddle.color("black")
        ball.color("black")
        game = False
        score.game_over()

      
      
  screen.update()
  time.sleep(0.01)
    

  
  
  
#stay at bottom
screen.exitonclick()