# from turtle import Turtle, Screen
import turtle as t
import random
t_turtle = t.Turtle()
t.colormode(255)
t_turtle.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_rgb = (r, g, b)
    return color_rgb


# 1.drawing a square with a dotted line (for loop is the most convenient solution)
for _ in range(4):
    for _ in range(5):
        t_turtle.forward(10)
        t_turtle.penup()
        t_turtle.forward(10)
        t_turtle.pendown()
    t_turtle.right(90)


# 2.drawing 3 - 10 sided shapes using a new colour each time
colours = ["blue", "chartreuse", "cyan", "DarkOrange", "CornflowerBlue", "BlueViolet", "DarkGreen", "DeepPink",
           "DarkOrchid", "green", "hotpink", "LightBlue", "IndianRed", "wheat", "SlateGray", "SeaGreen"]


shapes = [3, 4, 5, 6, 7, 8, 9, 10]

t_turtle.penup()
t_turtle.left(90)
t_turtle.forward(100)
t_turtle.right(90)
t_turtle.pendown()

for number in shapes:
    turn = int(360/number)
    shape_type = number
    t_turtle.color(random.choice(colours))
    for _ in range(shape_type):
        t_turtle.forward(100)
        t_turtle.right(turn)

# 3. drawing a random line with a new random colour each time
t_turtle.pensize(10)
t_turtle.speed(10)
possible_angles = [0, 90, 180, 270]

for x in range(200):
    t_turtle.color(random_color())
    t_turtle.forward(random.randint(10, 50))
    t_turtle.setheading(random.choice(possible_angles))

# 4. drawing a spirograph (circles with radius of 100 in distance, with random colors)
t_turtle.speed(20)


def draw_spirograph(size_of_gap):
    for x in range(int(360/size_of_gap)):
        t_turtle.color(random_color())
        angle = size_of_gap
        t_turtle.circle(100)
        t_turtle.right(angle)
        angle += size_of_gap


draw_spirograph(5)


# Keep at bottom to ensure code above runs before the below happens
screen = t.Screen()
screen.exitonclick()
