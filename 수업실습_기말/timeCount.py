import random
import time

# 삽입 정렬
def insertion_sort(A) :
    n = len(A)
    for i in range(1, n) :
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key :
            A[j + 1] = A[j]
            j-=1
        A[j+1] = key

# 쉘 정렬
def shell_sort(A) :
    n = len(A)
    gap = n // 2
    while gap >= 1 :
        if(gap % 2) == 0 : gap += 1
        for i in range(gap, n) :
            j = i
            while j >= gap and A[j] < A[j- gap] :
                A[j], A[j-gap] = A[j-gap], A[j]
                j-=gap
        gap = gap // 2

# input data
count_ary = [1000, 10000, 12000, 15000]

for count in count_ary: # 4번 돌아감
    # 랜덤 1000개, 10000개, 12000개, 15000개 순서대로 돌아감
    arr = [random.randint(10000, 99999) for i in range(count)]
    insertion_arr = arr.copy()
    shell_arr = arr.copy()
    print(f"데이터 수 : {count}개")

    start = time.time()
    # 삽입 정렬 실행코드
    insertion_sort(insertion_arr)
    end = time.time()
    print(f"삽입정렬 실행시간 = {end-start : 10.3f}")

    start = time.time()
    # 쉘 정렬 실행코드
    shell_sort(shell_arr)
    end = time.time()
    print(f"쉘  정렬 실행시간 = {end-start : 10.3f}")
    print()


