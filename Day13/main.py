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

screen.listen() # loading failed until the listen function was placed below object instantiation

screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()