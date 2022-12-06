# str = "welcome"
# for i in range(len(str)) :
#     print(str[i])

# sum = 0
# for i in range(1, 101) :
#     sum += i
# print("1~100까지 합 : "+str(sum))

# password=""
# cnt = 0
# while password != "pythonisfun" :
#     password = input("암호입력 : ")
#     cnt += 1
# print("로그인 성공, 시도 횟수 :", cnt)

# import random
# n = random.randint(1, 100)
# user = int(input("1부터 100사이의 숫자를 맞추시오\n숫자를 입력하시오: "))
# cnt = 1
#
# while user != n :
#     if user < n :
#         print("너무 낮음!")
#         cnt += 1
#         user = int(input("숫자를 입력하시오: "))
#
#     elif user > n :
#         print("너무 큼!")
#         cnt += 1
#         user = int(input("숫자를 입력하시오: "))
#     else :
#         break
# print(f"축하합니다. 시도횟수={cnt}")


# turtle그림 반복문으로
# import turtle
# t = turtle.Turtle()
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# t.left(60)
# t.circle(100)
# i = 1
# while i <=  5 :
#     t.circle(100)
#     t.left(60)
#     i += 1
# t.circle(100)

# 실습. 도돌이표
# print("연주 순서: ")
# print("A", end="-")
# print("B", end="-")
#
# for i in range(2):
#     if i == 0 :
#         print("C", end="-")
#         print("D", end="-")
#     elif i == 1 :
#         print("C", end="-")
#         print("D", end="")

# 실습. n각형 입력 받아 한 변의 길이가 100인 정 n각형 그림
# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
#
# a = turtle.textinput("", "몇각형을 원하시나요?:")
# n = int(a)
#
# for i in range(n) :
#     t.forward(100)
#     t.left(360/n)

# 실습. 랜덤 워크 시뮬레이션
# 랜덤 워크(random walk) : 수학, 컴퓨터 과학, 물리학 분야에서
# 임의 방향으로 향하는 연속적인 걸음을 나타내는 수학적 개념
# 랜덤워크의 성질을 시뮬레이션하는 프로그램을 작성
# 터틀 그래픽 사용 > 반복 부분 구조화, 터틀이 이동할 위치 랜덤 값 받기, 터틀 이동
# import turtle
# import random
# t = turtle.Turtle()
# t.shape("turtle")
# a = turtle.textinput("", "몇번 반복을 원하시나요? :")
# n = int(a)
#
# for i in range(n) :
#     mv = random.randint(1, 100)
#     t.forward(mv)
#     ag = random.randint(0, 360)
#     t.right(ag)

# 실습. 범인찾기게임
# 3개의 방 중 한 곳에 숨은 범인 찾기, 범인 숨은 방 맞추면 100점추가 후 게임종료
# 틀리면 범인은 다른 방에 숨고 10점 감점 후 다시 맞춤
# import random
# score = 0
#
# while True :
#     room = random.randint(1, 3)
#     n = int(input("방 번호를 입력하세요: "))
#
#     if n == room :
#         print("범인 체포!")
#         score += 100
#         break
#     elif n > 3 :
#         print(n, "번 방은 없습니다.")
#     else :
#         print("범인 없습니다.")
#         score -= 10
# print("게임 종료")
# print("점수 :", score, "점")