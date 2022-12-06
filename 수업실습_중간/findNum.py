# 인덱스 번호 먼저 출력, 그 및에 0과 8 랜덤으로 지정
# 2초 카운트
# 화면 클리어
# random, time, clear
# 인덱스와 8자 자리 매칭 => if else문
# 몇 번 맞췄는지 카운팅
# 40개 숫자 중에 사용자가 위치를 맞춰야함,
# 실제 저장된 데이터와 매칭 총 5번
# 맞춘 횟수, 틀린 횟수
# os함수가 제대로 지원이 된다면 clear됨
# 현재 작업

import os            # clear을 위해 필요
import random as r   # ramdom으로 범위지정
import time as t     # sleep

# 화면에 뿌려주는 부분
# 40개를 다 0으로 세팅
palja = [0] * 40
# success -> 성공한 횟수
success = 0

for k in range(5):
    # pos는 8이 들어갈 인덱스
    pos = r.randrange(40)
    palja[pos] = 8

    # 0부터 39까지 출력
    for m in range(40):
        print("%2d " % m, end="")
    print("\n")

    # 8자에 있는 값 출력
    for m in range(40):
        print("%2d " % palja[m], end="")
    print("\n")
    t.sleep(2)
    os.system("cls")

# 사용자 입력받는 부분
    user = int(input("8자 어디에? : "))
    if user == pos:
        success = success + 1
        print("\n%d번 맞췄음" % success)
    else:
        print("\n틀렸음, 맞춘 횟수 = %d" % success)
    palja[pos] = 0

input()