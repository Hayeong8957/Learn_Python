# print(f"9*8은 {9*8}입니다.")
# print("9*8은 " +str(9*8)+"입니다.")
#
# print("너무 "+"반짝"*2 + " 눈이 부셔 " + "No "*4)
# print("너무 "+"깜짝"*2 + " 놀란 나는 " + "Oh "*4)
# print("너무 "+"짜릿"*2 + " 몸이 떨려 " + "Gee "*4)

# import turtle
# t = turtle.Turtle()
# t.shape("turtle")
# n = int(turtle.textinput("정다각형 입력", "몇각형을 그릴건가요?"))
# for i in range(n):
#     turtle.forward(100)
#     turtle.left(360/n)

# for i in range(10,51,10) :
#     print(f"반지름이 {i}인 원의 넓이: {i} * {i} * 3.14")

# x = -1
# y = 3
# print(f"다항식의 계산 결과: {(-y)**3+2*(x**2)*y}")

# ftemp = int(input("화씨온도: "));
# ctemp = (ftemp - 32) * 5/9
# print("섭씨온도 : ", ctemp)

# n = 29
# for i in range(2, n+1) :
#     for j in range(2, i) :
#         if i % j == 0 :
#             break
#     else:
#         print(f"{i} ", end="")

# num = int(input("수 : "))
# for i in range(1, num+1) :
#     if num % i == 0 :
#         print(i, end=" ")

# a = 10
# b = 12
# # 최대 공약수
# for i in range(min(a, b), 0, -1) :
#     if a % i == 0 and b % i == 0 :
#         print(i)
#         break
# # 최소 공배수
# for i in range(max(a, b), (a*b)+1) :
#     if i % a == 0 and i % b == 0 :
#         print(i)
#         break
#
# a=10
# b=20
# for i in range(max(a, b), (a*b)+1) :
#     if i % a == 0 and i % b == 0 :
#         print(i)
#         break
# price = 10000
# print("상품의 가격은 %s원입니다."%price)
# print("이렇게 정다운\n너 하나 나 하나는\n어디서 무엇이 되어\n다시 만나랴")
# print('''이렇게 정다운
# 너 하나 나 하나는
# 어디서 무엇이 되어
# 다시 만나랴''')
# s = "Hello Python"
# print(s[5:2:-2])
# print(s[-1::-1])
# print(s[::-1])
# animal = "frog"
# print(animal[1:4:2])
# animal = 'elephant'
# print(animal[5:])
# print(animal[:3])
# print(animal[3:-3])
# print(animal[:])

# print("안녕하세요")
# name = input("이름이 뭐예요? ")
# print(f"만나서 반갑습니다. {name}님")
# print(f"{name} 님, 이름의 길이는 다음과 같군요: {len(name)}")
# age = int(input("나이가 어떻게 돼? "))
# print(f"내년이면 {age+1}세가 되시는 군요")
# str = "도서관에서 보자"
# print(str[::-1])

# from datetime import datetime
# print(datetime.today())
# thisYear = datetime.today().year
# print(f"올해는 {thisYear}년입니다.")
# age = int(input("당신의 나이를 입력하세요 : "))
# print(f"2050년에는 {age+(2050-thisYear)}살이군요")

# import random
# n = random.randint(1, 4)
#
# print("주민등록번호의 성별 정보 번호를 생성합니다.")
# print(f"생성번호: {n}")
# if n==1 or n==3 :
#     print("남성입니다.")
# else :
#     print("여성입니다.")
# print("프로그램을 종료합니다.")

# year = int(input("연도를 입력하시오: "))
# if year % 4 == 0 and year % 100 != 0 :
#     print(f"{year}년은 윤년입니다.")
# elif year % 400 == 0 :
#     print(f"{year}년은 윤년입니다.")
# else :
#     print(f"{year}년은 윤년이 아닙니다.")
#
# for i in range(3, 10, 2) :
# 	print(i)

# sum = 0
# for i in range(1, 11) :
#     sum += i
# print(sum)

# import time
# for i in range(10, 0, -1) :
#     print(i)
#     time.sleep(1)
# print("Fire!")
# for i in range(1, 6) :
#     for j in range(6-i, 0, -1) :
#         print("*", end=" ")
#     print("")
#
# for i in range(1, 6) :
#     for j in range(1, i+1) :
#         print("*", end=" ")
#     print("")
#
# sign = True
# while sign :
#     light = input("신호등 색상을 입력하시오: ")
#     if light == "blue" :
#         sign = False
# print("전진!")

# for i in range(1, 7) :
#     for j in range(1, 7) :
#         if i + j == 6 :
#             print(f"첫 번째 주사위={i} 두 번째 주사위={j}")
# n = int(input("몇까지의 소수를 찾아드릴까요? : "))
# for i in range(2, n+1) :
#     for j in range(2, i):
#         if (i % j) == 0 :
#             break
#     else :
#         print(i, end=" ")
#

# for i in range(3) :
#     for j in range(3) :
#         print("*", end="")
#     print()

# for i in range(1, 10) :
#     for j in range(1, 10) :
#         print(i*j, end=" ")
#     print()

# for i in range(1, 6):
#     for j in range(1, i+1) :
#         print("*", end="")
#     print()
# for i in range(1, 6) :
#     for j in range(6-i, 0, -1) :
#         print("*", end="")
#     print()

# for i in range(1, 8) :
#     for j in range(8-i) :
#         print(" ", end="")
#     for k in range(1, i) :
#         print("*", end="")
#     for p in range(i, 0, -1):
#         print("*", end="")
#     print()

# for i in range(2, 30) :
#     for j in range(2, i) :
#         if i % j == 0 :
#             break
#     else:
#         print(i, end=" ")
# import time
# for i in range(10, 0, -1) :
#     print(i)
#     time.sleep(1)
# print("FIRE!" or "IGNITION!")

# n = 10
# m = 20
# if n < m :
#     n, m = m, n
# while m > 0 :
#     r = n % m
#     n, m = m, r
# if n != 0 :
#     print("최대공약수는 ", n, "입니다.")
# else :
#     print("서로소")

#
# def BMI(h, w) :
#     result = w / h ** 2
#     return result
#
# def BMI_result(result) :
#     if result < 18.5 :
#         print("당신은 저체중입니다.")
#     elif result < 23 :
#         print("당신은 정상입니다.")
#     elif result < 25 :
#         print("당신은 과체중입니다.")
#     elif result < 30 :
#         print("당신은 경도비만입니다.")
#     else :
#         print("당신은 고도비만입니다.")
#
# h = float(input("키를 m단위로 입력하세요: "))
# w = int(input("몸무게를 kg단위로 입력하세요: "))
# result = BMI(h, w)
# BMI_result(result)

# def exchange(kcoin, nation) :
#     if nation == "미국" :
#         print(kcoin // 1182.5, "달러")
#     elif nation == "일본" :
#         print(kcoin // 1078.14, "엔")
#     elif nation == "유럽연합" :
#         print(kcoin // 1286.74, "유로")
#     elif nation == "중국" :
#         print(kcoin // 169.22, "위안")
#     else :
#         print("해당 국가 정보가 없습니다.")

# def exchange(k, n) :
#     if n in nation:
#         code = nation.index(n)
#         result = round(k/rate[code], 2)
#         print(k,"원은:", result, unit[code], "입니다.")
#     else:
#         print("해당 국가가 없습니다.")
#
# nation = ["미국", "일본", "유럽", "중국"]
# unit = ["달러", "엔", "유로", "위안"]
# rate = [1182.5, 1078.14, 1286.74, 169.22]
# k = int(input("환전 금액(원)을 입력하세요: "))
# n = input("국가를 입력하세요: ")
# exchange(k, n)

# def fact(n) :
#     if n <= 1:
#         return 1
#     else :
#         return n*fact(n-1)
#
# n = int(input("n을 입력하시오 : "))
# print(fact(n))

# 튜링상 수상자

awards = []
awards.append({"이름":"팀 버너스리", "수상년도":2016, "국적":"영국", "대표업적":"월드 와이드 웹의 하이퍼텍스트 시스템을 고안하여 개발"})
awards.append({"이름":"리처드 해밍", "수상년도":1968, "국적":"미국", "대표업적":"오류 검출 부호 및 오류 정정 부호"})
awards.append({"이름":"에츠허르 데이크스트라", "수상년도":1972, "국적":"네덜란드", "대표업적":"프로그래밍 언어 연구, 데이크스트라 알고리즘"})
awards.append({"이름":"더글러스 엥겔바트", "수상년도":1997, "국적":"미국", "대표업적":"마우스의 발명, 대화형 컴퓨팅"})
awards.append({"이름":"데니스 리치", "수상년도":1983, "국적":"미국", "대표업적":"유닉스 운영 체제 개발, C언어 개발"})

for award in awards :
    print(award)

print("==수상자 명단==")
for award in awards:
    print(award["이름"])
print()
print("==수상자 명단과 수상년도==")
for award in awards:
    if award["수상년도"] <= 1990 :
        print(award["이름"], award["수상년도"])
print()
print("==수상자 국가==")
nationality = set()
for award in awards:
    nationality.add(award["국적"])
print(nationality)