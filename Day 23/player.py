from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.speed("fastest")
        self.refresh_turtle()
        self.left(90)
    
    
    def move(self):
        self.forward(MOVE_DISTANCE)
        
    def refresh_turtle(self):
        self.goto(0, -280)