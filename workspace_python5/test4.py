'''
  반복문

  초기식
  while 조건문:
    실행문
    증감식
'''

# 1~10까지 while 사용 출력

i = 1
while i<11:
    print(i) # (세로 출력)
    # print(i, end="\n")
    print(i,end=" ")  # (가로 출력)
    i+=1


# 1~100까지 합 출력
i = 1;
sum = 0;

while i<=100:
    sum+=i
    i+=1

print("총 합 : ",sum)

#### 코드로 자판기 만드는 프로그램 만들어보기


# 🔻 무한루프
# while True:
#     print("반복문 실행")

# 보조제어문 : break문, continue문


# 🔻 for문
# for 변수 in 리스트(튜플,문자열):
#     실행문
#     실행문

list1 = "1234567"
for data in list1:
    print("data : ",data)

data1 = [(1,2),(3,4),(5,6)]
data2 = {(1,2),(3,4),(5,6)}
print(type(data1))
print(type(data2))

for d in data1:
    print(d)

for d in data2:
    print(d)

for (k,v) in data1:
    print("k : ",k,end=", ")
    print("v : ",v)


# 1부터 10까지 숫자 출력
# range(시작값,끝값,증가치) : 숫자 리스트를 생성하는 함수
#       시작값~끝값-1

print(range(1,5,1))
r = range(1,5,1)
print(type(r))

# for + range
for i in range(1,5,1):
    print(i)  # 1,2,3,4 출력

# 1~10까지의 숫자를 가로 출력
r = range(1,11,1)  # 혹은 range(1,11). 기본적으로 1씩 올라가도록 카운팅
for i in r:
    print(i,end=" ")

print()
# 1~10 까지 숫자 중에서 홀수만 출력
for i in range(1,11,2):
    print(i,end=" ")

print()
# 10~1 까지 숫자 가로 출력
for i in range(10,0,-1):
    print(i,end=" ")

print()
# for 누적합 (1~10 누적합 계산하기)
sum = 0
for i in range(1,11):
    sum += i

print("sum : ",sum)


# 구구단 2단 출력
for i in range(1,10):
    print("2 * ",i," = ",(2*i))

# 포매팅을 사용해보기!
dan = 2
print(str(dan)+"단")
for i in range(1,10):
    print(" %d * %d = %d" %(dan,i,dan * i))


# 2~9단 세로찍기
print(">>>>>>>>>2~9단 세로 찍기<<<<<<<<")
for dan in range(2,10,1):
    print(dan,"단")
    for i in range(1,10,1):
        print(" %d * %d = %d" %(dan,i,dan * i))


# 2~9단 가로찍기
print(">>>>>>>>>2~9단 가로 찍기<<<<<<<<")
for i in range(1,10):
    for dan in range(2,10):
        print(" %d * %d = %d" %(dan,i,dan * i),end=" ")
    print()   # ⭐⭐⭐ 띄어쓰기 주의해서 볼 것!


######################################################

# 리스트 - for
# 리스트 안에 for문 사용
list2 = [1,2,3,4,5]
result = []
print("-"*50)

# 리스트 안의 데이터를 각각 5씩 증가해서 추가
for i in list2:
    result.append(i+5)

print(result)

# 리스트 안에 for문 사용
# 리스트 변수 = [표현식 for 값 in 반복객체]
# 리스트 변수 = [표현식 for 값 in 반복객체 if 조건]
result = [(num+5) for num in list2]
print(result)

result2 = [ (num*10) for num in list2 if num%2 == 0]
print(result2)

result = [ (num+5) for num in range(1,10,1) ]
print(result)


result3 = [ (x * y) for x in range(1,6,1)
                    for y in range(1,5,1) ]
print(result3)

