def printStar(n) :
    if 0 < n :
        printStar(n - 1)
        print("★"*n)

printStar(5)