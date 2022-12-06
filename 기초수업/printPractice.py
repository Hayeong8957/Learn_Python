print("안녕하세요")
a = input("이름이 뭐예요? ")
print("만나서 반갑습니다. %s 님" %a)
# print(a+" 님, 이름의 길이는 다음과 같군요: "+str(len(a)))
print(a+" 님, 이름의 길이는 다음과 같군요.", end=' ')
print(len(a))

c=int(input("나이가 어떻게 돼요? "))
print("내년이면 "+str(c+1)+"세가 되시는 군요")