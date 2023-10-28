from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forward():
    turtle.forward(10)


def turn_right():
    turtle.setheading(turtle.heading() + 5)  # change the direction


def turn_left():
    turtle.setheading(turtle.heading() - 5)


screen.onkey(key="space", fun=move_forward)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Left", fun=turn_left)
screen.listen()

screen.exitonclick()
