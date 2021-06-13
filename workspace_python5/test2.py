# test2.py

# 제어문 if

# if 조건문:
#     실행코드
#     실행코드
#     ...
# else:
#     실행코드
#     실행코드

# if 제어문에서 실행코드는 들여쓰기를 1칸이상 무조건 해야한다
# 보통 스페이스 4칸 (탭 1칸)

if 10 > 2:
    print("참")

# 조건문 : 참, 거짓 결과를 확인가능한 구문
# == != > >= < <=
# 비교연산자의 결과는 항상 boolean

# time = 9 9시 일 때 학원을 간다 (9시 이전), 안간다 (9시 이후)
# time = input("시간 입력 : ")
# if int(time) >= 9:
#     print("안간다")
# else:
#     print("간다")

# int(), float(), str()
# 숫자가 아닌 데이터를 숫자로 변경시 오류
int(10)
int("100")
# int("hello")
int(3.1234)
# int("3.123")  "소수점이 표현된 숫자"

# type(값) : 해당 데이터의 타입을 리턴
print("-" * 50)

if 100 > 50:
    print("참1")
    print("참2")
    if 100 > 30:
        print("참3")

# 조건문에서 사용가능한 연산자
# and(둘 다 참일때), or(둘 중 하나라도 참일 때), not(부정)
# if 100>0 and 200>0:
# if 100>0 or 200>0:

card = True;
money = 3000;

# 만약에 5천원 이상이면서 카드가 있으면 "택시를 탄다",
# 5천원 미만이거나, 카드가 없으면 "버스를 탄다"

if card and money >= 5000:
    # print("택시")
    pass
else:
    print("버스를 탄다")
# if 제어문에서 아무런 동작 없이 넘어가기 위해서는 [pass] 문법 사용
# A가 B 안에 있는지/없는지 비교 연산 => T/F
print(1 in [1, 2, 3, 4, 5])  # True
print(6 not in [1, 2, 3, 4, 5])  # True
print('a' in "itwill busan")  # True

str1 = "itwill busan class"

# 문자 안에 a 있을경우 "있다"
#            없을경우 "없다"

if 'a' in str1:
    print("있다")
else:
    print("없다")

if str1.find("busan") > 0:
    print("있다")

'''
if 조건문:
    실행코드
elif 조건문:
    실행코드
elif 조건문:
    실행코드
else:
    실행코드         
'''

if 10 > 0:
    pass
else:
    pass

# 학생의 성적 입력받아서 input() 학점으로 변경후 출력
# 100~90 : A, 89~80 : B, 79~70 : C, 69~60 : D, 59~0 : F

# grade = int(input("성적 : "));

# if 90 <= grade and grade <= 100:
#     print("A")
# elif 80 <= grade and grade <= 89:
#     print("B")
# elif 70 <= grade and grade <= 79:
#     print("C")
# elif 60 <= grade and grade <= 69:
#     print("D")
# elif 0 <= grade and grade <= 59:
#     print("F")
# else:
#     print("잘못된 값입니다")

# 조건부 표현식 : 제어문 코드를 간결하게 표현
if 10 > 0:
    tmp = "pass"
else:
    tmp = "pass"

#   [참일때값] if 조건문 else [거짓일때값]
tmp = "pass" if 10>0 else "pass"


###################


# [책 72p] 리스트 자료형
# 배열과 유사하게 데이터를 저장
# 변수 = [요소,요소,요소,...]
ls = []
ls2 = [1,2,3,4,5,6] # 숫자
ls3 = ['a','b','c','d'] # 문자
ls4 = [1,2,'a','b'] # 숫자, 문자
ls5 = [1,2,'a','b',[1,2]] #숫자, 문자, 리스트

print(type(ls))
print(type(ls2))

# ls2 리스트의 3번 인덱스의 정보 출력
print("3번 인덱스 정보 : ",ls2[3])
# -n 은 뒤에서부터 세는 인덱스
# 인덱스 번호 양수(왼쪽에서 0부터 시작), 음수(오른쪽에서 -1부터 시작)
print(ls2[-1]," // ",ls2[-4])  # 6  //  3
print(ls2[3]," // ",ls2[4])  # 4  //  5


print(ls4)
# print(ls4[0]+ls4[-1])
print(str(ls4[0])+ls4[-1])  # 1b 출력. 숫자 + 문자열

print("-"*50)
print(ls5)

# 이중리스트의 값을 접근하는 방법
print(ls5[1], ls5[4], ls5[4][1])  # 2 [1,2] 2

# 리스트의 접근방법 -> 리스트도 타입 (객체)
# 삼중리스트 (이런거도 있긴 한데 잘 안씀)
ls6 = [1,2,[1,2,[1,2]]]
print(ls6[2][2][1])  # 2

print("리스트의 길이 : ",len(ls2))
print("값의 개수 : ",ls6.count(1))
print("값의 개수 : ",ls6[2].count(1))

# 리스트 슬라이싱

# ls2 3~5번 인덱스 값만 출력
print(ls2)
print(ls2[3:6])  # 문자열 슬라이싱과 동일 [시작:끝]
print(ls2[:])   # 모두
print(ls2[2:])  # 2번~끝
print(ls2[:2])  # 처음~2번

###################################

# 리스트 연산
print(ls2 + ls3)    # 리스트 연결
# print(ls2 - ls3)  에러
print(ls2 * 3)      # 리스트 반복하기

print("-"*50)
# 리스트 데이터 수정
ls_a = [1,2,3]
print(ls_a[1])
ls_a[1] = 100
print(ls_a[1])

# 리스트 요소 삭제
del ls_a[1]
print(ls_a)

ls_a *= 3
print(ls_a)

del ls_a[2:4]
print(ls_a)

# ls_a[4]
# ls_a[4] = 100  (데이터 추가 X)
ls_a.append(100)  #데이터 추가 O
print(ls_a)

# ls_a.append(1,2,3,4,5)    여러개를 동시에 넣을 순 없다
# 기존의 리스트에 1,2,3,4,5 를 추가하려면?
ls_a.append([1,2,3,4,5])
print(ls_a)

# print(ls_a.sort())
del ls_a[5]
print(ls_a)
print(ls_a.sort())  # 동일 데이터의 경우 정렬 불가능

ls_b = [1,2,3,6,4,5,7,8,9]
# ls_b_sort = ls_b.sort()
# print(ls_b_sort)

# sort() : 오름차순 정렬(숫자, 알파벳), reverse() : 리스트 뒤집기
# insert(a,b) : 요소 삽입   a 인덱스에 b의 값을 넣는다.

# 10을 ls_b 6과 4 사이에 넣어보기
ls_b.insert(4,10)
print(ls_b)

# del값, del(값), 리스트 요소 제거 remove(값)
ls_b.remove(10)
print(ls_b)

ls_b = ls_b * 2
print(ls_b)

# del() / remove()
del ls_b[2]     # 리스트의 위치로 접근
print(ls_b)

ls_b.remove(2)  # 지우고자 하는 값으로 접근 (제일 앞에 있는 하나만 지워짐)
print(ls_b)

ls_b.remove(2)
print(ls_b)

# pop() : 리스트 가장 마지막의 데이터를 꺼내기 (삭제)
ls_b.pop()
print(ls_b)

ls_b.pop(3)     # ls_b[3] 요소를 삭제

print(ls_b)
print("-"*50)

# ls_b.append(1,2,3,4) (X)
ls_b.append([1,2,3,4])
print(ls_b)
ls_b.pop()

ls_b.extend([1,2,3,4])  # 리스트 + 리스트 / 리스트 += 리스트
print(ls_b)


# in 연산자, not in 연산자
# => 주로 리스트와 같이 사용

pocket = ['phone', 'money', 'paper']

# 주머니에 전화기가 있으면 "전화"
#      "         없으면 "집으로 돌아가기"

if 'phone' in pocket:
    print("전화")
if 'phone' not in pocket:
    print("집으로 돌아가기")


# 다차원 리스트
score = [
    [90,79,56],
    [78,97,66],
    [40,80,70]
]

# 행 - 학생 : 각 학생별 총점 / 평균
# 열 - 과목 : 각 과목별 총점 / 평균

print("A 학생의 총 점 : ",str(score[0][0]+score[0][1]+score[0][2]))
print("A 학생의 평균 : ",str(score[0][0]+score[0][1]+score[0][2] / len(score[0])))

print("B 학생의 총 점 : ",str(score[1][0]+score[1][1]+score[1][2]))
print("B 학생의 평균 : ",str(score[1][0]+score[1][1]+score[1][2] / len(score[0])))

print("C 학생의 총 점 : ",str(score[2][0]+score[2][1]+score[2][2]))
print("C 학생의 평균 : ",str(score[2][0]+score[2][1]+score[2][2] / len(score[0])))
