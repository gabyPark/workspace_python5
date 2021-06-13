print("안녕하세요")

# 주석문 ctrl + /
"""
 여러줄짜리 주석문
"""

'''
  식별자 선언
  - 예약어를 사용할 수 없음.
  - 특수문자는 (_)언더바 만 사용 가능
  - 숫자로 시작할 수 없음
  - 공백을 포함 X
  - 영문자를 사용해서 처리(대소문자 구분)
  
  ItwillBusan : 카멜 표기법 (이름의 시작, 연결되는 단어의 시작은 대문자)
  itwill_busan : 스네이크 표기법
  
  식별자 - 카멜 표기법 (대문자로 시작) -> 클래스
        - 스네이크 표기법(소문자로 시작) -> ( O ) -> 함수
                                    -> ( X ) -> 변수
                                    
  출력문 : print()
'''

import keyword
print(keyword.kwlist)

print("안녕하세요")
print(1000)
print(4.123)
print("안녕하세요","저는","사용자","입니다")
print()
print("te\nst")

# "Mary's cosmetics" 출력해보기
print('Mary\'s Cosmetics')

# 홍길동이 인사를 합니다. "안녕하세요"
print("홍길동이 인사를 합니다. \"안녕하세요\" ")
print("홍길동이 인사를 합니다.\n \"안녕하세요\" ")

# C:\Users\ITWILL\AppData\Local\Programs\Python\Python39 경로 출력
print("C:\\Users\\ITWILL\\AppData\\Local\\Programs\\Python\\Python39")

# data!data!data!
print("data!"*3)
# 문자 출력시 공백 대신 다른 문자를 사용해서 연결 가능
print("data","data","data", sep="!")
print("010","1234","5678",sep="-")
print("010","1234","5678",sep="/")

# 세미콜론의 사용 : 한 줄에 하나 이상의 코드를 실행할 때 코드의 끝을 의미
print("1"); print("2")
print("1234")

# 데이터형 (리터럴)

# 숫자(Number)
#   - 정수, 실수, 8진수, 16진수
# 사칙연산 ( + - * / % ** // )
# x ** y : x^y 제곱연산
print(2 ** 4)
# x // y = 나눗셈 후 몫을 반환
print(5 // 2)


# 문자열 (String) :
"""
    1. "" 사용
    2. '' 사용
    3. """ """ 사용
    4. ''' ''' 사용
"""

name = "홍길동"
print(name)

# 여러줄의 문자열데이터를 저장할 때 """ / ''' 사용
tmp = """안녕하세요
      저는 부산에 사는
      홍길동입니다"""
print(tmp)


# 문자열 연결 [문자열 + 문자열]
print("안녕"+"하세요")
# print("안녕"+1) [문자열+숫자] (X)

tmp1 = "Hello"
tmp2 = "Itwill"
print(tmp1+tmp2)
print(tmp1, tmp2)
print(tmp1, 2)   # 문자+숫자 연결이 가능

# 문자열 곱하기
print("A" * 5)
print("-" * 50)

# 문자열 길이
print(len("Hello"))     # 5 출력

# 문자열 데이터는 배열에 저장 (인덱싱)
# |H|E|L|L|O|
#  0 1 2 3 4
str="Hello"
# 0~ 증가 인덱스 : 문자 데이터를 왼쪽에서 오른쪽으로 읽기
print(str[0])
# -1~ 증가 인덱스 : 문자 데이터를 오른쪽에서 왼쪽으로 읽기
print(str[-1],str[-2],str[-3],str[-4],str[-5])

# print(str[6]) 인덱스 오류

# 문자열 슬라이싱 : 문자열 자르기
str = "Life is too short, You need Python"
# Life 만 출력
print(str[0]+str[1]+str[2]+str[3])
print(str[0],str[1],str[2],str[3])

# [시작번호, 끝번호]   시작번호 <= x < 끝번호
print(str[0:4])
print(str[8:11])

# 지점~끝
print(str[8:])  # 8번~끝까지 출력됨

# 시작~지점
print(str[:5])

# 처음~끝
print(str[:])

# str 에서 10번 인덱스의 값을 A 로 바꾸기
print(str[10])
# 문자열 데이터타입은 해당 요소의 값을 변경 X
# str[10] = "A"
print(str[10])
print("="*50)
print(str[:10]+"A"+str[11:])


# 문자열 포매팅
#   %s - 문자열 (String)
#   %c - 문자 1개 (Character)
#   %d - 정수(Integer)
#   %f - 부동소수점(Floating-point)
#   %o - 8진수
#   %x - 16진수
#   %% - % 문자값

number = 10
print("오후 5시")
print("오후 %d시" % 3)
print("오후 %d시" % number)

# 포매팅을 여러개 사용
print("%s %d시" % ("오전", number))

# "강수 확률 50%" 출력 (50% 포매팅으로 출력)
print("강수 확률 %d%%" % 50)

# 포매팅 여백 (글자 왼쪽에 여백 생성 후 글자는 오른쪽에서 채우기)
print(" hi %10s " % "홍길동")
# 글자를 왼쪽에 적고 나머지 공간을 여백으로 채우기
print(" hi %-10s " % "홍길동")

# {숫자} 순차적으로 접근, {이름} 이름으로 접근
tmp = "hello {0} {1} {name}".format(100,300,name="홍길동")
print(tmp)


# 3/17 수업
# 문자열 내장함수
str = "itwill"

# 문자열의 길이
# print("문자열 길이 : "+len(str))
#         문자열    +   숫자     => 파이썬에선 실행되지 않음
print("문자열 길이 : ",len(str))
# 문자열과 숫자를 결합할 때, + 대신 ,(콤마) 를 쓰면 된다.
print("문자열 길이(특정 문자 개수) : ",str.count('w'))  # => 1 출력 (itwill 에는 w가 하나만 들어가기 때문)

print("특정 문자의 위치 : ",str.index('w'))  # => 2 출력 (itwill 에서 w 는 0 1 2, 2번 인덱스에 있기 때문)
print("특정 문자의 위치 : ",str.index('i'))  # => 0 출력
print("특정 문자의 위치 : ",str.rindex('i'))  # => 3 출력. 뒤에서부터 읽어오는 인덱스
# print("특정 문자의 위치 : ",str.index('a'))  => 없는 문자 입력 시 오류

print("특정 문자의 위치 : ",str.find('i'))  # => 0 출력. index 와 같다
print("특정 문자의 위치 : ",str.find('a'))  # => -1 출력. 해당 요소가 없을 경우 -1 출력


print(str.upper())
print(str)
print(str.lower())

str2 = "    hello"
print(str2)
print(str2.lstrip())
str2 = "hello    "
print(str2.rstrip())
str2 = "  hello  "
print(str2.strip())

str2 = " itwill busan class "
print(str2.replace("busan","jeju"))

print(str2.split())  # 공백 기준
print(str2.split(","))  # 구분자를 기준으로 split
# 리스트타입으로 결과를 리턴