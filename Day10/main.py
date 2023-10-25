from turtle import Turtle, Screen
from random import randint
import colorgram


# turtle = Turtle()
# turtle.shape("turtle")
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
# turtle.width(2)
# screen = Screen()
# screen.colormode(255)
# for i in range(0, 500):
#     c1, c2, c3 = randint(0, 255), randint(0, 255), randint(0, 255)
#     turtle.pencolor((c1, c2, c3))
#     turtle.forward(20)
#     turn = randint(0, 360)
#     turtle.right(turn)

# turtle.speed("fastest")
# for _ in range(50):
#     turtle.pencolor((randint(0, 255), randint(0, 255), randint(0, 255)))
#     turtle.circle(75)
#     turtle.setheading(turtle.heading() + 10)

# python colorgram based dot painting creation
spider = "spiderman-icon.gif"

screen = Screen()
screen.colormode(255)
screen.register_shape(spider)  # register shape does not accept png file types as input
turtle = Turtle(shape=spider)
turtle.penup()
turtle.setposition(-300, 300)
turtle.pendown()
colors = colorgram.extract("spiderman.webp", 10)
right = 1

# screen.register_shape("spider", "spiderman-icon.png")
# screen.getshapes()
# turtle.shape("spiderman-icon.png")


def moveForward():
    turtle.penup()
    turtle.forward(30)
    turtle.pendown()


def turnRight():
    turtle.penup()
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)


def turnLeft():
    turtle.penup()
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)


for _ in range(20):
    for _ in range(20):
        turtle.pencolor(colors[randint(0, len(colors) - 1)].rgb)
        turtle.dot(10)
        moveForward()
    if right > 0:
        turnRight()
        right *= -1
    else:
        turnLeft()
        right *= -1


input("Press any key...")
