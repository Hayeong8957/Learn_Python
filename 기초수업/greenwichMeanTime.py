# 그리니치 표준시
import time

fsec = time.time()
total_sec = int(fsec)
total_min = total_sec//60
minute = total_min % 60  # 현재 분
total_hour = total_min // 60  # 전체
hour = total_hour % 24 + 9
print("현재 한국 시간:", str(hour)+"시"+str(minute)+"분")