# 제출코드
# 앞에서부터 하나씩 4개뽑아
# 빈리스트에 앞에서부터 차례로 넣는다.
# buff에서 뺄 땐 뒤에서부터 3개만
# 출력 : e r o
a=['K','o','r','e','a']
temp = []

for i in range(4):
    temp.append(a[i])

for j in range(3):
    print(temp.pop(-1), end=" ")
    # 뒤에서부터 위치 지정하는 경우 -1
    # 인덱스 생략한 경우 마지막 값 취득 후 삭제



