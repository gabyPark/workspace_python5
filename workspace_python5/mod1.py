# mod1.py

# 사칙 연산 모듈

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

# __name__ : 파이썬 내부에서 사용하는 변수
#            해당 파일을 실행시 __main__ 값 저장
#            다른 파이썬 파일(모듈)에서 실행 시, 추가한 모듈의 이름이 저장.

# 모듈(해당 파일에서는) __name__ 값 : __main__
# 모듈을 추가하는 파일에서는 __name__ 값 : __main__ (X)
if __name__== "__main__":
    print("모듈 실행!")
    print(add(10,20))
    print(div(30,10))