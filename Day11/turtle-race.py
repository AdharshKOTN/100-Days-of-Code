from turtle import Turtle, Screen, write, hideturtle
from random import randint

# t1, t2, t3, t4 = Turtle(), Turtle(), Turtle(), Turtle()
screen = Screen()
screen.screensize(650, 500)
screen.title("Turtle Race!")
turtles = []
colors = ["red", "blue", "yellow", "green"]
locations = [20, 0, -20, -40]
user_input = screen.textinput("Which turtle will win?", "Red/Blue/Yellow/Black")
for i in range(4):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
for i in range(4):
    turtles[i].penup()
    turtles[i].goto(-400, locations[i])
turtle_index = 0
while True:
    turtles[turtle_index].forward(randint(0, 20))
    print(turtles[turtle_index].xcor())
    if turtles[turtle_index].xcor() > 400:
        break
    turtle_index += 1
    turtle_index %= 4
if colors[turtle_index].lower() == user_input.lower():
    write(
        "Congrats you  got it right!!",
        align="center",
        font=("Cooper Black", 25, "italic"),
    )
else:
    write(
        colors[turtle_index].capitalize() + " Wins! You Lose!",
        align="center",
        font=("Cooper Black", 25, "italic"),
    )
    hideturtle()

screen.exitonclick()
# keyboard inputs
