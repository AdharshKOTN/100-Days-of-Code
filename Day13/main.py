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

scoreboard = ScoreBoard()

player1 = Player(STARTING_POS_P1)
player2 = Player(STARTING_POS_P2)
ball = Ball()

screen.listen() # loading failed until the listen function was placed below object instantiation

screen.onkey(player2.up, "Up")
screen.onkey(player2.down, "Down")

screen.onkey(player1.up, "w")
screen.onkey(player1.down, "s")

game_is_on = True
paddle_hit_ctr = 1
while game_is_on:
    screen.update()
    print(ball.ball_speed)
    if paddle_hit_ctr % 6 == 0:
        print("increasing ball speed")
        ball.ball_speed *= 1.01
    ball.move()
    if (ball.distance(player2) < 30 and ball.xcor() > 350) or (ball.distance(player1) < 30 and ball.xcor() < -350):
        ball.bounce_x()
        paddle_hit_ctr += 1
    if ball.xcor() > 390:
        scoreboard.update_player2_score()
        ball.reset() 
    if ball.xcor() < -390:
        scoreboard.update_player1_score()
        ball.reset()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

screen.exitonclick()