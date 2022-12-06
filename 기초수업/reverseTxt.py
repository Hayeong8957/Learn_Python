# 4주차 실습4-암호프로그램 만들기
oriTxt = input("평문: ")
reverseTxt = ""

for i in oriTxt:
    reverseTxt = i + reverseTxt

print("암호문: "+reverseTxt)