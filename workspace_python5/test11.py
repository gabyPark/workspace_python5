# test11.py

# 모듈 : 변수, 함수, 클래스를 모아놓은 파일
# => 다른 파이썬 파일에서 실행할 수 있게 만들어진 파이썬 파일

# mod1.py 모듈을 가져와서 사용
# import 모듈명 ->👉 해당 모듈 전체를 추가
# import mod1
# > 이렇게 부르면 mod1.함수명 해야함

# from 모듈명 import 모듈함수 ->👉 해당 모듈의 특정 함수만 추가
# from mod1 import add
# from mod1 import add,mul  # 해당 함수만 사용 가능
from mod1 import *
# > 이렇게 부르면 함수명만 호출해도 사용가능

# 실행
# print(mod1.add(100,200))
# print(mod1.mul(300,400))

# print("모듈 실행 결과",mod1.add(100,200))
# print("모듈 실행 결과",add(100,200))
print("모듈 실행 결과",mul(100,200))  # 해당 모듈의 함수를 추가 없이 사용X


print("-"*50)

import mod2
print("변수 값 출력",mod2.PI)
print("함수 호출",mod2.add(20,10))

# 모듈 안에 있는 객체를 생성 후 사용
myMath = mod2.Math()
print(myMath.solv(5))


# 패키지 : (.) 연산자를 사용해서 파이썬 모듈을 관리하는 묶음
#         비슷한 기능들끼리 묶어서 사용

#       패키지.모듈
import itwill.info
itwill.info.sayHello()

from itwill.info import sayHello  # 특정 함수만 호출
sayHello()

# ----------------------------------------------------------
# 직접 해보기
import itwill.class5.TeamProject
itwill.class5.TeamProject.project()

from itwill.class5.TeamProject import project
project()
# ----------------------------------------------------------

# alias 로 간단하게 사용 가능!!
import itwill.class5.TeamProject as tp
# itwill.class5.TeamProject.project()
tp.project()

from itwill.class5.TeamProject import project as pj
# project()
pj()

# ----------------------------------------------------------

# 내장함수 : 기본 패키지에 있는 모듈
# 외장함수 : 외부 패키지에 있는 모듈  => 파이썬 라이브러리

import random as r
print(r.random())
print(r.randint(1,10))  # 1~10 사이의 값 랜덤으로 출력

# ----------------------------------------------------------
print("-"*50)

import calendar as cal
# print(cal.calendar(2021))

import webbrowser as web
# web.open("http://www.naver.com")

# ----------------------------------------------------------
print("-"*50)

# 패키지 생성 시 자동으로 __init__.py 파일이 생성됨
# -> __init__.py : '해당 디렉토리가 패키지의 일부다' 라는 의미로 사용됨.
# 3.3버전 이전의 경우 해당 파일이 없을 경우 에러 발생.

# itwill/class1/hello 실행
import itwill.class1.hello as h
h.hello()

