def bubble_sort(a) :
    for i in range(len(a)-1, 0, -1) :
        changed = False
        for j in range(i) :
            if (a[j] > a[j+1]) :
                a[j], a[j+1] = a[j+1], a[j]
                changed = True

        if not changed :
            break
        print(f"step{len(a) - i} : {a}")        # 정렬 step별 정렬 결과 & 스캔횟수 print하기 위함
a=[40,60,70,50,10,30,20]
# a=[5,3,8,4,9,1,6,2,7]
print("정렬 전: \t", end="")
print(a)
bubble_sort(a)
print("정렬 후: \t", end="")
print(a)