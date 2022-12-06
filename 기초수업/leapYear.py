# 윤년 판단
# 사용자로부터 입력받은 연도가 윤년인지 아닌지 판단
# [윤년]
# - 연도가 4로 나누어 떨어지고, 100으로 나누어 떨어지지 않는 연도는 윤년
# - 400으로 나누어 떨어지는 연도는 윤년

inputYear = int(input("연도를 입력하시오: "))

if ((inputYear % 4 == 0) and (inputYear % 100 !=0)) or (inputYear % 400 == 0):
    print(str(inputYear)+"년은 윤년입니다.")
else :
    print(str(inputYear) + "년은 윤년이 아닙니다.")