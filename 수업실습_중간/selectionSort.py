def selection_sort(a):
    for i in range(0, len(a)-1):
        minimum = i
        for j in range(i, len(a)):
            if a[minimum] > a[j]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]
        print(f"step{i+1}: {a}")
# 내부 반복문 > 현재 index부터 마지막 index까지 최소값의 index찾아냄
# 외부 반복문 > 이 최소값의 index와 현재 index에 있는 값을 상호 교대(swap)
# 외
# for i in range(len(a)) :
#     min_idx = i
#     for j in range(i+1, len(a)):
#         if a[min_idx] > a[j]:
#             min_idx = j
#     a[i], a[min_idx] = a[min_idx], a[i]
# print(a)
a=[40,60,70,50,10,30,20]
# a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print("정렬 전: \t", end="")
print(a)
selection_sort(a)
print("정렬 후: \t", end="")
print(a)