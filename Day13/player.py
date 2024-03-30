from turtle import Turtle

class Player(Turtle): # establishing the parent class like this
                      # enables me to use the self keyword instead of
                      # creating an object to access the parent class methods
                      # stepping stone goal: learning to code faster, waste less time 
                      # using keyboard shortcuts, explore what VS code can do for me 
                      # this class helped understanding in efficient coding, inheritence in python
                      
        
    def __init__(self, starting_location):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_location)
    
    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
    
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)