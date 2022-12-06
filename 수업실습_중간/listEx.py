def listEx(a):
    b = sorted(a, reverse=True)
    c = b[0:3]
    for i in c:
        while i in a:
            a.remove(i)
    return a

a= [-3.2, 5.5, 4.1, 1.1, -1.3, 2.7, 0.5]
print("삭제 전: \t", end="")
print(a)
print("삭제 후: \t", end="")
print(listEx(a))

