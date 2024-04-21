from turtle import Screen, Turtle
from scoreboard import ScoreBoard
from player import Player
from time import sleep
from ball import Ball

# define the starting positons 
STARTING_POS_P1 = ((-350, 0))
STARTING_POS_P2 = ((350, 0))

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game!")
screen.setup(width=800, height=600)
screen.tracer(0)


# scoreboard = ScoreBoard()

player1 = Player(STARTING_POS_P1)
player2 = Player(STARTING_POS_P2)
ball = Ball()

screen.listen() # loading failed until the listen function was placed below object instantiation

screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")

game_is_on = True
ball.right(45)
while game_is_on:
    if ball.xcor() < 390 and ball.xcor() > -390 and ball.ycor() < 290 and ball.ycor() > -290:
        print("ball is in")
        ball.forward(2)
    else:
        if ball.xcor() > 390:
            # player2 scores
        if ball.xcor() < -390:
            # player1 scores
        if ball.ycor() 
        print("ball is out")
    screen.update()

screen.exitonclick()