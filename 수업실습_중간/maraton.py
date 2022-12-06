# 1. 정렬 함수나 메서드를 이용해서 정렬
# 2. 순수하게 선택정렬 알고리즘 기법을 사용해서 정렬

# 총 인원수, 각 선수마다 참가번호,
# 6번의 참가번호를 입력받음
# 각 선수마다 초단위로 입력
# 시, 분, 초 단위로 출력
# 동일기록은 없다고 가정 > 중복 허용 X
# 예시 2~3개를 넣어서 출력결과 제출

# 함수 & 메서드 사용한 문제풀이
person = int(input())
number = []
record = {}

for i in range(person):
    x = int(input())
    number.append(x)
for j in number:
    y = int(input())
    record[j]=y
lank = sorted(record.items(), key=lambda i: i[1])
# lambda함수: dictionary에서 참가번호과 기록을 튜플 리스트로 가지고 옴
# lambda 매개변수 : 표현식
# (lambda x,y: x + y)(10, 20) >>> 30

for k in range(3):
    h=(lank[k][1]//3600)
    m=(lank[k][1]%3600)//60
    sec=(lank[k][1]%3600)%60
    print(lank[k][0],h,m,sec)

# 참가번호도 list로 받고, 기록도 list로 받음
# 선택정렬로 구현


