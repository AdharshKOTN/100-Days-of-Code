from turtle import Turtle
from turtle import Screen
from random import randint


turtle = Turtle()
turtle.shape("turtle")
# draw a red square
# turtle.color("red")
# for i in range(0, 4):
#     turtle.forward(100)
#     turtle.right(90)

# trying example from py documentation
# for steps in range(100):
#     for c in ("blue", "red", "green"):
#         turtle.color(c)
#         turtle.forward(steps)
#         turtle.right(30)

#  draw dashed line
# for i in range(50):
#     turtle.forward(10)
#     turtle.up()
#     turtle.forward(10)
#     turtle.down()

# draw multiple shapes
# for i in range(3, 10):
#     for j in range(i):
#         turtle.forward(30)
#         turn = 360 / i
#         turtle.right(turn)

# draw a random walk
turtle.width(2)
screen = Screen()
screen.colormode(255)
# for i in range(0, 500):
#     c1, c2, c3 = randint(0, 255), randint(0, 255), randint(0, 255)
#     turtle.pencolor((c1, c2, c3))
#     turtle.forward(20)
#     turn = randint(0, 360)
#     turtle.right(turn)

turtle.speed("fastest")
for _ in range(50):
    turtle.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
    turtle.circle(75)
    turtle.setheading(turtle.heading() + 10)

# python colorgram based dot painting creation

input("Press any key...")
