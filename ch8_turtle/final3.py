import turtle
import random

def screenLeftClick(x, y):
	# apply random
	r = random.random()
	g = random.random()
	b = random.random()
	
	turtle.pencolor((r, g, b))
	turtle.pendown()
	turtle.goto(x, y)

def screenRightClick(x, y):
	turtle.penup()
	turtle.goto(x, y)

psize = 5
tsize = random.randrange(1, 5)

turtle.title("거북이")
turtle.pensize(psize)
turtle.shape("turtle")
turtle.shapesize(tsize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
