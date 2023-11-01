from turtle import Turtle, Screen

# create the body of a snake
screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game!")
screen.screensize(600, 600)

t1, t2, t3 = Turtle(shape="square"), Turtle(shape="square"), Turtle(shape="square")

# create the turtles and color

for turtle in screen.turtles():
    turtle.color("white")

screen.exitonclick()
