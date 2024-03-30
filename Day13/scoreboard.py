from turtle import Turtle

class ScoreBoard(Turtle):
    player1_score = 0
    player2_score = 0
    writer = Turtle()
    
    def __init__(self):
        super().__init__()
        self.writer.color("white")
        self.writer.teleport(1, 350)
        self.writer.hideturtle()
        self.display_score()
        self.board_setup()
        
    def update_player1_score(self):
        self.player1_score += 1
        self.writer.clear()
        self.display_score()
    
    def update_player2_score(self):
        self.player2_score += 1
        self.writer.clear()
        self.display_score()
        
    def display_score(self):
        self.writer.write(
            f"{self.player1_score} : {self.player2_score}",
            align="center",
            font=("Cooper Black", 40),
        )
    def game_over(self):
        self.writer.teleport(0, 0)
        self.writer.hideturtle()
        self.writer.write(
            "GAME OVER!",
        align="center",
        font=("Cooper Black", 25, "italic"),
        )
        
    def board_setup(self):
        setup_turtle = Turtle()
        setup_turtle.hideturtle()
        setup_turtle.color("white")
        setup_turtle.teleport(0, 400)
        setup_turtle.right(90)
        setup_turtle.pensize(10)
        for i in range(20):
            setup_turtle.pendown()
            setup_turtle.forward(20)
            setup_turtle.penup()
            setup_turtle.forward(20)
            