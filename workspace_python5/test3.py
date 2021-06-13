# test3.py

# 튜플(tuple) 자료형
# () 사용해서 데이터를 저장
# 튜플의 데이터를 수정, 삭제 불가능(변경x)

t1 = ()
t2 = (1,)  # 튜플타입의 데이터를 1개만 생성 할 경우 , (콤마) 사용해야 함(필수)
t2_1 = (1) # 콤마가 없을 경우 int 타입

print(type(t2), type(t2_1))

t3 = (1,2,3,4,5)
t4 = 1,2,3,4,5 # 튜플은 () 생략 가능
print(type(t4))

t5 = (1,2,3,'a','b')
t6 = (1,2,3,'a','b',(1,2,3,4),[1,2,3,5])  # 이것도 튜플 가능!
print(type(t6))
print(t6)

t6[6][1] = 10
print(t6)
# 튜플 안의 리스트의 데이터는 바꿀 수 있으나,
# t6[6] = "test"
# print(t6)
# del(t6[0])
# 튜플 안의 데이터는 바꾸지 못한다

# 코드를 실행하면서 데이터를 여러개 저장
# 값 변경 가능 -> 리스트 타입
# 값 변경 불가 -> 튜플 타입

print("-"*50)
print("t3 : ",t3)
print(t3[2])  # 데이터 사용 가능 (인덱싱 가능)
print(t3[2:3])  # 데이터 슬라이싱 가능 -> 튜플의 형태로 리턴

# 튜플 연결(+)
print(t3 + t4)
t5 = t3+t4
print(t5)
print(t3[0:2]+t4)

# 튜플 복사(*)
print(t3 * 2)
print(t3[0:2] * 2)
# print(t3[0] * 2) 불가능

print("길이 : ",len(t3))

print(t3)
# t3 튜플에 6,7 추가
print(t3+(6,7))  # 일회성으로 튜플 뒤에 추가하고 사라지는 것
t3+=(8,9)  # 기존의 튜플 뒤에 누적되는 것
print(t3)

###################################################

# 딕셔너리 자료형 (순차적접근 x)
#  key값을 사용해서 value를 사용
#  key값은 변경 X, value값은 변경 O
#  key값은 중복데이터를 사용X (가장마지막의 key값만 불러다 사용가능)
#  key값 - 튜플(o), 리스트(x)

# {key:value, key:value ....}
dic = {"name":"itwill","tel":"0511231234","addr":"부산 진구"}
print(dic)

# 레퍼런스 ['key값']
print("dic['name'] = ",dic['name'])

# 전화번호, 주소
print(dic["tel"],dic["addr"])

dic["addr"] = "부산진구 동천로109"

print(dic["addr"])

# 딕셔너리 타입에 데이터 추가

# dic[4]="0518030979"
dic["fax"]="0518030979"   # fax 키값, 0518030979 value값  저장  {"fax":"0518030979"}
print(dic)

# dic["classroom"] = [1,2,3,4,5,6,7]
dic["classroom"] = (1,2,3,4,5,6,7)  # 튜플로도 저장 가능 (변경은 불가)
print(dic)

# fax 정보 삭제
del(dic['fax'])
print(dic)

# <class 'dict'>
print(type(dic))
# print(dic[1]) 에러! 딕셔너리 호출은 반드시 key 값만 사용
# 🔺 맵의 형태로 사용하는 것은 검색에 유용 (인덱스가 없지만, 키값으로만 움직일 수 있다)

dic["tel"]="0551231234"  # 같은 키값을 입력했을 때, 새로운 정보 추가가 아니라, 기존의 정보가 변경됨.
print(dic)

dic2 = {"k":"125455", "k":"111111"}
print( dic2["k"] )


print( dic.keys() )
print( type(dic.keys()) ) # <class 'dict_keys'> 타입

# <class 'dict_keys'> 타입 -> list 타입 변경후 사용
ls = list( dic.keys() ) # ⭐⭐⭐
print( type(ls),ls )

# value 값만 가져오기
print(dic.values())
print(type(dic.values()))  # <class 'dict_values'> 타입

# key, value 둘 다 쌍으로 가져오기
print(dic.items())
print((type(dic.items())))  # <class 'dict_items'> 타입  [책 94p 참조]


dic.clear()
print( dic )
# print( dic['name'] ) 에러 (key값이 없기 때문)

# 딕셔너리 안에 key값이 있는지 체크

print('name' in dic )

if 'name' in dic:
    print("key값이 있습니다",dic['name'])
else:
    print("key값이 없습니다. (key 생성)")
    dic["name"]=""

print(dic)

dic["tel"]="010-1234-1234"
#  딕셔너리의 값이 있는지 없는지 확인

print( dic.get("없는키") )  # 없는 key => None 리턴
print( dic.get("tel") )   # 있는 key => key에 해당하는 value를 리턴
# print( dic["addr"] ) -> key에러 발생


################################################

# 집합 자료형(set) 2.3~ 이후 지원
# 데이터 중복X, 데이터를 순서 없이 저장
# => 순서가 없으니 인덱싱을 사용 할 수 없음

s1 = set([1,2,3,4,5])
print(s1, type(s1))

s2 = set("itwill")
print(s2,type(s2))

# print( s1[0] )  순서가 없기 때문에 인덱싱 X
# => 리스트/튜플로 변경후 사용
l1 = list(s1)
print(l1[0])
t1 = tuple(s2)
print(t1[1])


###########################################

# 책 103p 자료형의 T/F

'''
 문자열 - "test" (T), "" (F)
 리스트 - [1,2] (T), [] (F)
 튜플 - ()(F)
 딕셔너리 - {} (F)
 숫자 - 0이 아닌 숫자(T), 0 (F)
       None (F)
'''

###########################################

ls = [1,2,3,4]
# id(객체) -> 객체의 메모리 주소
print(ls,id(ls))

ls2 = ls
print( id(ls2), id(ls))
#  A  is  B  : A와 B가 동일한 객체 인가? 물어보는 연산자 is
print( ls is ls2 )

from copy import copy

a = copy(ls2)

print(a, id(a),id(ls2))



#  변수 생성하기

a,b = ('1','2')
(a,b) = ('1','2')
[aa,bb] = [11,22]
a=b=100

a=100
b=200

a,b = b,a
print(a,b)