# 사용자로부터 정수를 받아서 정수의 종류에 따라서 거북이가
# 양의 정수, 0, 음의 정수 메시지가 있는 위치로 이동하는 프로그램
# 각 메시지의 위치는 양의 정수는(100,100)
# 0은 (100, 0), 음의 정수는 (100,-100)의 위치이다.

import turtle
t = turtle.Turtle()
t.shape("turtle")
t.penup()
t.goto(100,100)
t.write("입력된 정수는 양의 정수입니다.")

t.goto(100,0)
t.write("입력된 정수는 0입니다.")

t.goto(100,-100)
t.write("입력된 정수는 음의 정수입니다.")

t.goto(0,0)
t.pendown()

n = int(turtle.textinput("", "숫자를 입력하시오."))

if n > 0:
    t.goto(100,100)
elif n == 0:
    t.goto(100,0)
else:
    t.goto(100,-100)