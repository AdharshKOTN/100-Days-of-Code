from turtle import Turtle, write

class ScoreBoard(Turtle):
    score = 0
    writer = Turtle()
    
    def __init__(self):
        super().__init__()
        self.writer.color("white")
        self.writer.teleport(0, 270)
        self.writer.hideturtle()
        self.display_score()
        
    def update_score(self):
        self.score += 1
        self.writer.clear()
        self.display_score()
        
    def display_score(self):
        self.writer.write(
            "Score: " + str(self.score),
            align="center",
            font=("Cooper Black", 25),
        )
    def game_over(self):
        self.writer.teleport(0, 0)
        self.writer.hideturtle()
        self.writer.write(
            "GAME OVER!",
        align="center",
        font=("Cooper Black", 25, "italic"),
        )