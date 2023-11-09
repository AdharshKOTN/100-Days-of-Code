from snakegame import Snake
from turtle import Screen


screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game!")
screen.screensize(600, 600)
screen.tracer(0)

snake = Snake()


game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(
        snake.turnLeft, "Left"
    )  # remember when passing a function as a variable, pass the name only
    # using parantheses with the function name will call it!
    screen.onkey(snake.turnRight, "Right")
    snake.moveForward()
    screen.update()
