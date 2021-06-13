# test5.py

# 함수 : 여러가지 실행문을 한번에 실행

'''
def 함수명(매개변수):
    실행문1
    실행문2
    pass
'''

# 숫자 2개를 전달받아서 사칙연산의 결과를 모두 출력하는 함수
# ( + - * / )

def sum(x,y):
    print("+ : ",x+y)
    print("- : ",x-y)
    print("* : ",x*y)
    print("/ : ",x/y)

# 함수명 사용 호출
sum(2,3)



# 절대값을 계산하는 함수 myABS, 전달인자 1개
# 양수 -> 양수, 음수 -> 양수 결과 리턴

def myABS(x):
    if x<0:
        x=-x
    return x

print("절대값 : ",myABS(100))
print("절대값 : ",myABS(-100))

# 리턴값 없는 리턴문 => 함수의 종료
def test():
    return

# 리스트 값 체크 함수 - listck()
# 리스트 하나를 전달받아서, 리스트 안에 100 숫자 확인
# 숫자 있음! or 숫자 없음! << 메세지 출력

list3 = [1,2,3,100,200,300]

def listick(v):
    print("전달값 : ",v)
    check = "없음"

    for i in v:
        if i == 100:
            check="있음"
            break    # 100일때 멈추기 위해서
        else:
            check = "없음"
    print("숫자 "+check)
    
listick(list3)


# 내가 한 방법
def listck2(v):
    if 100 in v:
        print("숫자 있음!")
    else:
        print("숫자 없음!")

listck2(list3)

####################################################

# def 함수명(*매개변수):
#     실행문

def test(*v):
    print(v)

test(1)
test(1,2)

# 함수의 매개변수의 값을 초기화
# -> 초기화 코드는 마지막에만 사용 (컴파일에러 발생)
def test2(name, age, tel="010-1234-1234"):
    print("name",name)
    print("age",age)
    print("tel",tel)

test2("홍길동",20)
test2("홍길동",20,"010-4321-4321")

####################################################

# 🔻 클래스
# class 클래스:
#     변수1
#     변수2
#
#     함수1()
#     함수2()

# 클래스 생성 -> 객체 생성 (생성자 호출)
class Itwill:
    classroom = 5
    def study(self):
        print("자습")

# 객체 생성 (생성자 호출하면 알아서 생성됨)
will = Itwill()
will.study()
print(will.classroom)


# 계산기 객체를 사용해서 사칙연산 처리
class MyCalc:
    def mySum(self,a,b):
        print(" + : ",a+b)
    def mySub(self,a,b):
        print(" - : ",a-b)
    def myMul(self,a,b):
        print(" * : ",a*b)
    def myDiv(self,a,b):
        print(" / : ",a/b)

c = MyCalc()
c.mySum(1,2)
c.mySub(1,20)

# 생성자 : 객체 생성 시 변수를 초기화
# self : 객체 자신의 정보를 가지고 있는 레퍼런스(this)
# class 클래스명:
#     def __init__(self):
#         pass
#     def __int__(self,name,age):
#         self.name = name
#         pass


# 객체를 생성 시 본인의 이름, 전화번호 초기화 가능한 객체 생성
# ItwillStudent
class ItwillStudent:
    name = ""
    tel = ""

    # 생성자
    # def __int__(self):
    #     self.name = "기본학생"
    #     self.tel = "010-1111-1111"
    def __init__(self,name,tel):
        self.name = name
        self.tel = tel

    def showMyInfo(self):
        print("이름 : "+self.name+", 전화번호 : "+self.tel)

i = ItwillStudent("박가빈","010-2222-2222")
i.showMyInfo()

####################################################

#  상속

# class 클래스명(상속할 클래스명):
# class 클래스명(상속할 클래스명1, 상속할 클래스명2):     다중상속 가능
class Parent:
    def pprn(self):
        name = "홍길동"  # 클래스변수(인스턴스 변수)
        print("부모-pprn()")

class Child(Parent):
    def cprn(self):
        print("자식-cprn()")
    def pprn(self):
        super().pprn()      # super() 부모 객체의 생성자 호출
        print("자식-pprn()")

p = Parent()
p.pprn()
# p.cprn()     호출 불가

c = Child()
c.cprn()
c.pprn()        # 상속했기 때문에 부모의 기능/속성을 사용 가능
# pprn()을 오버라이드 했을 시, 자식 클래스의 pprn이 호출됨 (메서드 오버라이딩 가능)



