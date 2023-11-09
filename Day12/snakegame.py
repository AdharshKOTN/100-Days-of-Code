from turtle import Turtle
from time import sleep


class Snake:
    snake_segments = []

    def __init__(self) -> None:
        # create the body of a snake

        starting_pos = [(0, 0), (-20, 0), (-40, 0)]

        for pos in starting_pos:
            new_snake_part = Turtle(shape="square")
            new_snake_part.penup()
            new_snake_part.color("white")
            new_snake_part.goto(pos)
            self.snake_segments.append(new_snake_part)

    def turnLeft(self):
        # turn the first segement of the snake left
        self.snake_segments[0].left(90)

    def turnRight(self):
        # turn the first segement of the snake left and
        self.snake_segments[0].right(90)

    def moveForward(self):
        for i in range(len(self.snake_segments) - 1, 0, -1):
            sleep(0.05)
            self.snake_segments[i].goto(
                self.snake_segments[i - 1].xcor(), self.snake_segments[i - 1].ycor()
            )
        self.snake_segments[0].forward(20)


# move the snake forward

#     if (
#         segment.xcor() >= 300
#         or segment.xcor() <= -300
#         or segment.ycor() >= 300
#         or segment.ycor() <= -300
#     ):
#         game_is_on = False

# screen.bgcolor("white")
# write(
#     "Game Over!",
#     align="center",
#     font=("Cooper Black", 25, "italic"),
# )

# screen.listen()
# screen.onkey(turnLeft, "left")
# screen.onkey(turnRight, "right")
# screen.exitonclick()
