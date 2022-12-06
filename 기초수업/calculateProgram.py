# 계산대 프로그램
# 물건의 가격과 지불한 금액을 입력하면 거스름돈을 알려주는 계산대 프로그램
# 동전의 개수는 최대한 적게, 물건가격과 투입한 돈은 100원 단위로 입력되고,
# 거스릅돈은 500원, 100원짜리로만 거슬러 준다..

inputPrice = int(input("투입한 돈: "))
realPrice = int(input("물건가격: "))

charge = inputPrice - realPrice

coin500 = charge // 500
a500 = charge % 500

coin100 = a500 // 100
a100 = a500 % 100

print("거스름돈: ", charge)
print("500원 동전의 개수: ", coin500)
print("100원 동전의 개수: ", coin100)
