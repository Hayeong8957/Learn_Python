# 1. 사용자로부터 도형을 입력받는다.
# 2. 직사각형이면 가로와 세로를 입력 받아 그림
# 3. 정삼각형이면 한 변의 길이를 입력 받아 그림
# 4. 원이면 반지름의 길이를 입력받아 그림
import turtle
t = turtle.Turtle()

t.shape("turtle")
s = turtle.textinput("", "도형을 입력하시오")

if s == "직사각형" :
    w = int(turtle.textinput("", "가로"))
    h = int(turtle.textinput("", "세로"))
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
    t.forward(w)
    t.left(90)
    t.forward(h)
    t.left(90)
elif s == "정삼각형" :
    l = int(turtle.textinput("", "한 변의 길이"))
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.left(120)
    t.forward(l)
    t.left(120)
elif s == "원" :
    r = int(turtle.textinput("", "반지름의 길이"))
    t.circle(r)


