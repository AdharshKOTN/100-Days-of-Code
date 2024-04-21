from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0,0)
        
        
    # movement for the ball
    # starts at one heading
    # vv---This needs to happen in the game runner
    # changes heading on contact with top or bottom wall
    # changes heading when contact with player 1 or player 2  
    # def movement(self):