def notation_iter(base, num) :
    answer = ''
    value = num
    while value > 1 :
        mod = value % base
        value = value // base
        answer += str(mod)
    answer += str(value)
    return answer[::-1]       # 왼쪽으로 1칸씩 이동하면서 가져옴

numberChar = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
numberChar += ["A", "B", "C", "D", "E", "F"]
number = int(input("10진수 입력 --> "))
print("\n 2진수 : ", end="")
notation_iter(2, number)
print("\n 8진수 : ", end="")
notation_iter(8, number)
print("\n 8진수 : ", end="")
notation_iter(16, number)
