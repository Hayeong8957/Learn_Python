L=[1, 3, 4, 4, 3, 2, 7, 4, 1, 7, 4]
del_list=[4, 7]
for x in del_list:
    while x in L:
        L.remove(x)
print(L)