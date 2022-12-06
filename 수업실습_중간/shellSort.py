def shell_sort(a) :
    n = len(a)
    gap = n // 2
    while gap >= 1 :
        if (gap % 2) == 0 : gap += 1
        for i in range(gap, n) :
            j = i
            while j >= gap and a[j] < a[j-gap] :
                a[j], a[j-gap] = a[j-gap], a[j]
                print(f"    Step= {a}")
                j -= gap
        print("    Gap=", gap, a)
        gap = gap // 2

a=[40,60,70,50,10,30,20]
# a = [5,3,8,4,9,1,6,2,7]
print("Original : ", a)
shell_sort(a)
print("Shell    : ", a)