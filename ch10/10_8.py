import turtle
import random

def moveUp():
    turtle.pencolor(
        random.random(),
        random.random(),
        random.random()
        )
    turtle.setheading(90)
    turtle.forward(10)

def moveRight():
    turtle.pencolor(
        random.random(),
        random.random(),
        random.random()
        )
    turtle.setheading(0)
    turtle.forward(10)

def moveDown():
    turtle.pencolor(
        random.random(),
        random.random(),
        random.random()
        )
    turtle.setheading(270)
    turtle.forward(10)

def moveLeft():
    turtle.pencolor(
        random.random(),
        random.random(),
        random.random()
        )
    turtle.setheading(180)
    turtle.forward(10)

def clickLeft(x, y):
    turtle.clear()

def clickRight(x, y):
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()


psize = 5
tsize = 1

r = 0.0 # red (0.0 ~ 1.0)
g = 1.0 # green
b = 1.0 # blue

turtle.title("거북이")
turtle.pensize(psize)
turtle.shape("turtle")
turtle.shapesize(tsize)
turtle.pencolor(r, g, b)

### draw circle
##turtle.circle(50)
### draw square
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(50)

turtle.onkeypress(moveUp, "Up")
turtle.onkeypress(moveRight, "Right")
turtle.onkeypress(moveDown, "Down")
turtle.onkeypress(moveLeft, "Left")

turtle.onscreenclick(clickLeft, 1)
turtle.onscreenclick(clickRight, 3)

turtle.listen()








