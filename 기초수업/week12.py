# infile = open("week12/phones.txt", "r")
#
# for line in infile :
#     line = line.rstrip()
#     print(line)
#
# infile.close()

# outfile = open("week12/phones1.txt", "w")
# outfile.write("강감찬 010-1234-5681\n")
# outfile.write("김유신 010-1234-5682\n")
# outfile.write("정약용 010-1234-5683\n")
# outfile.close()

# a = "All's well that ends well"
# print(a.split())

# import csv
# f = open("week12/input.csv", "r")
# data = csv.reader(f)
#
# for line in data:
#     print(line)
# f.close()

# import csv
# # 입력 파일 출력 파일 열기
# infile = open("week12/weather_input.csv", "r")
# data = csv.reader(infile)
# count = 0
# sum = 0
#
# for line in data :
#     count+=1
#     sum+=float(line[2])
#
# print("강원도 2009년 01월 부터 2022년 11월까지의 총 강수량: %.3f" %sum)
# print("강원도 2009년 01월 부터 2022년 11월까지의 평균 강수량: %.3f" %(sum / count))
# infile.close()

# class Counter:
#     def __init__(self, initValue=0):
#         self.count = initValue
#
#     def increment(self):
#         self.count+=1
# a = Counter(0)
# b = Counter(100)
# print(a)

import math
class Circle:
    def __init__(self, radius=0):
        self.radius = radius
    def getArea(self):
        return math.pi * self.radius * self.radius
    def getPerimeter(self):
        return 2 * math.pi * self.radius
c = Circle(10)
print("원의 면적", c.getArea())
print("원의 면적", c.getPerimeter())