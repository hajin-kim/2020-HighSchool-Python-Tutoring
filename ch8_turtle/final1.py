import turtle

def screenLeftClick(x, y):
    r = 0.0 # 빨강
    g = 1.0 # 초록(0~1 사이 소수)
    b = 1.0 # 파랑
    turtle.pencolor((r, g, b))  # 펜 색상 설정  *주의* 괄호 2개
    turtle.pendown()
    turtle.goto(x, y)

psize = 5   # 펜 두께
tsize = 1   # 펜 크기

turtle.title("화이팅")  # 윈도우 창의 이름
turtle.pensize(psize)   # 펜 두께 설정
turtle.shape("turtle")  # 펜 모양 설정
turtle.shapesize(tsize) # 펜(거북이) 크기 설정

turtle.onscreenclick(screenLeftClick, 1)

turtle.done()
