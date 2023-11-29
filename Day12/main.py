from snakegame import Snake
from turtle import Screen, Turtle, write, color
from random import randint
from food import Food
from time import sleep
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game!")
screen.setup(600, 600)
screen.tracer(0)

snake = Snake()

food = Food()

scoreboard = ScoreBoard()


# pulling the screen based functions out of the loop,
# the screen object tracks these without the use of a loop?
screen.listen()
# remember when passing a function as a variable, pass the name only
# using parantheses with the function name will call it!
screen.onkey(snake.left, "Left")  
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")



game_is_on = True
while game_is_on:
    # snake movement -------------------------------------------------------
    screen.update()
    sleep(0.1) 
    snake.moveForward()
    #-----------------------------------------------------------------------
    
    # food check and placement ---------------------------------------------
    
    if snake.head.distance(food) < 15:
        food.refresh()
        # increment score counter
        snake.extend_snake()
        scoreboard.update_score()
    
    #-----------------------------------------------------------------------
    
    
    # border check ---------------------------------------------------------
    if (
        snake.head.xcor() >= 300
        or snake.head.xcor() <= -300
        or snake.head.ycor() >= 300
        or snake.head.ycor() <= -300
    ):
        game_is_on = False
        scoreboard.game_over()
        screen.exitonclick()
    #-----------------------------------------------------------------------
    
    # tail check -----------------------------------------------------------
    
    for segment in snake.snake_segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 15:
            game_is_on = False
            scoreboard.game_over()
            
    #-----------------------------------------------------------------------
