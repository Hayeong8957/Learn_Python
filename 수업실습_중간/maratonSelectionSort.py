person = int(input())
number = []
record = []

for i in range(person):
    x = int(input())
    number.append(x)

for j in range(person):
    y = int(input())
    record.append(y)

# 선택 정렬 알고리즘으로 오름차순 정렬

def selection_sort(x, y):
    for p in range(0, len(x)-1):
        minimum = p
        for q in range(p, len(x)):
            if x[minimum] > x[q]:
                minimum = q
        x[p], x[minimum] = x[minimum], x[p]
        y[p], y[minimum] = y[minimum], y[p]

selection_sort(record, number)

for k in range(3):
    h = (record[k]//3600)
    m = (record[k]%3600)//60
    sec = (record[k]%3600)%60
    print(number[k],h,m,sec)




