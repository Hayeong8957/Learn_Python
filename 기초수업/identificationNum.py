import random
print("주민등록번호의 성별 정보 번호를 생성합니다.")
n = random.randint(1, 4)  # 1~4

if n == 1 or n == 3:
    print(n)
    print("남성")
elif n == 2 or n == 4:
    print(n)
    print("여성")
else:
    print("구분할 수 없다")

print("프로그램을 종료합니다.")