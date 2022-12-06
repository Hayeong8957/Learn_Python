# 2050년에 나는 몇살?
from datetime import datetime
print(datetime.today())
thisYear=datetime.today().year
print("올해는 "+str(thisYear)+"년입니다.")
age = int(input("당신의 나이를 입력 하세요: "))
print("2050년에는 "+str(age+(2050-thisYear))+"살이군요.")
