def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i,0,-1):
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
                # print(f"step{i + 1}: {a}")
            # print(f"step{i + 1}: {a}")
        print(f"step{i + 1}: {a}")

a=[40,60,70,50,10,30,20]# a = [54,88,77,26,93,17,49,10,17,77,11,31,22,44,17,20]
print("정렬 전: \t", end="")
print(a)
insertion_sort(a)
print("정렬 후: \t", end="")
print(a)