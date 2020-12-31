import turtle

def screenLeftClick(x, y):
	r = 0.0
	g = 1.0
	b = 1.0

	turtle.pencolor((r, g, b))
	turtle.pendown()
	turtle.goto(x, y)

def screenRightClick(x, y):
	turtle.penup()
	turtle.goto(x, y)

psize = 5
tsize = 1

turtle.title("거북이")
turtle.pensize(psize)
turtle.shape("turtle")
turtle.shapesize(tsize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
