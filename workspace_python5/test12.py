# test12.py

# 예외 처리
'''
try:
    예외가 발생할 수도 있는 코드
except 예외:
    예외 처리
'''

# print(4/0)

print("시작-----------------")

try:
    print(4 / 0)
# except IndexError:
#     print("예외발생!")
except (ZeroDivisionError,IndexError) as e:
    # pass 에러(예외) 발생 시 아무런 동작 없이 처리
    # raise FileNotFoundError 에러를 강제로 발생
    print("0으로 나누기 예외!",e)

print("끝--------------------")
