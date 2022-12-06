print("소금물의 농도를 구하는 프로그램입니다")
a= int(input("소금의 양은 몇 g입니까? "))
b= int(input("물의 양은 몇 g입니까? "))
c = (a/(a+b))*100
print("소금물의 농도: "+str(c)+"%")