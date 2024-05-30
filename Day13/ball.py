from turtle import Turtle
class Ball(Turtle):

    start_direction = 1
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0,0)
        self.setheading(0)

        self.ball_speed = 0.01
        self.move_x = 10
        self.move_y = 10

    def move(self):
        new_x = self.xcor() + self.move_x * self.ball_speed
        new_y = self.ycor() + self.move_y * self.ball_speed
        self.goto(new_x, new_y)
    
    def bounce(self):
        self.move_y *= -1
    
    def bounce_x(self):
        self.move_x *= -1
    

    def reset(self):
        self.penup()
        self.ball_speed = 0.01
        self.goto(0,0)
        self.bounce_x()
        # self.start_direction *= -1
        # if self.start_direction == 1:
        #     self.setheading(randint(0,179))
        # else:
        #     self.setheading(randint(180, 360))
        
        
    # movement for the ball
    # starts at one heading
    # vv---This needs to happen in the game runner
    # changes heading on contact with top or bottom wall
    # changes heading when contact with player 1 or player 2  
    # def movement(self):