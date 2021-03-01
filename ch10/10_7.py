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
    turtle.setheading(0)
    turtle.forward(10)


turtle.onkeypress(moveUp, "Up")
turtle.onkeypress(moveRight, "Right")

psize = 5
tsize = 1

turtle.title("윈도우 창 제목")
turtle.pensize(psize)
turtle.shape("turtle")
turtle.shapesize(tsize)
turtle.pencolor(0.53, 0.0, 1.0)

### draw circle
##turtle.circle(50)
### draw square
##turtle.pencolor(0.0, 0.0, 1.0)
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(50)
##turtle.right(90)
##turtle.forward(50)

turtle.listen()
turtle.done()











