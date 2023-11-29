from turtle import Turtle
from time import sleep

# using contansts format, lets me define custom constant values
# contants are intended not to be modified by the code
# the value of the constant itself can change
# increases understandability in code rather than looking at a list of characters and numbers


STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    
    def __init__(self) -> None:
        # the self keyword for classes lets me differentiate between local keywords and instance keywords
        self.snake_segments = []
        self.create_snake()
        # adding this piece of code helps with readablity in the movement section
        # from snake_segments[0] to head, 
        # the code is shorter and easier to understand what is being done at a high-level
        self.head = self.snake_segments[0]
        
        
    # moving this code to a function didn't seem necessary
    def create_snake(self):
        for pos in STARTING_POS:
            self.add_snake_segment(pos)
            
    def add_snake_segment(self, position):
        new_snake_part = Turtle(shape="square")
        new_snake_part.penup()
        new_snake_part.color("white")
        new_snake_part.goto(position)
        self.snake_segments.append(new_snake_part)
        
    def extend_snake(self):
        self.add_snake_segment(self.snake_segments[-1].position())
        

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def moveForward(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            self.snake_segments[i].goto(
                self.snake_segments[i - 1].xcor(), self.snake_segments[i - 1].ycor()
            )
        self.head.forward(MOVE_DISTANCE)