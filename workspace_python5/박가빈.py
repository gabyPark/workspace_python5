# 아이티윌 5강 박가빈 시험답안입니다



###############################################################
# 1번 문제
# def cnt(x,y):
#     print("sum : ",x+y)
#     print("avg : ",(x+y)/2)
#
# cnt(1,2)
###############################################################

###############################################################
# 2번 문제
# list = range(1,100,1)
#
# for digit in list:
#     if digit % 3 == 0:
#         if digit % 5 == 0:
#             print(digit)
###############################################################

###############################################################
# 3번 문제
# def abs(a):
#     if a<0:
#         a=-a
#     return a
#
# print("절대값 : ",abs(-5))
###############################################################

###############################################################
# 4번 문제
# ls = [1,2,3,4,5,6,7,8,9,10]
#
# odd = 0
# even = 0
#
# for i in ls:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
#
# print('홀수:',odd,'\t짝수:',even)
###############################################################

###############################################################
# 5번 문제
# class Parent:
#     name = ""
#     age = ""
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def prn(self):
#         print("이름 : ",self.name,"나이 : ",self.age)
#
# p = Parent("박가빈","20")
# p.prn()
#
# class Student(Parent):
#     def prn(self):
#         print("이름 : ",self.name,"나이 : ",self.age," 학생입니다")
#
# s = Student("박가빈", "20")
# s.prn()

###############################################################

###############################################################
# 6번 문제
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# df = pd.read_csv('franchise.csv')
# # print(df)
#
# plt.rcParams['font.family']="Malgun Gothic"
# plt.rcParams['axes.unicode_minus']=False
#
# ind = np.arange(len(df))
#
# plt.plot(df['chicken'],"r:.",label="chicken")
# plt.plot(df['coffee'],"b:.",label="coffee")
#
# plt.xticks(ind,df['year'])
# plt.legend()  # 라벨 표시
#
# plt.show()
###############################################################

###############################################################
# 7번 문제

# import pandas as ps
# import matplotlib.pyplot as plt
# import numpy as np
#
# plt.rcParams['font.family']="Malgun Gothic"
# plt.rcParams['axes.unicode_minus']=False
#
# df = ps.read_csv('population.csv')
#
# w = 0.4
# idx = np.arange(len(df))
#
# plt.bar(idx-w/2, df['men'] ,width=w,color='b',label="남성")
# plt.bar(idx+w/2, df['women'] ,width=w,color='r',label="여성")
#
# plt.xticks(idx, df['local'])
# plt.title("도시별 인구수")
#
# plt.legend()
#
# plt.show()

###############################################################

###############################################################
# 8번 문제

# import pandas as ps
# import matplotlib.pyplot as plt
#
# df = ps.read_csv('online.csv',encoding='euc-kr')
#
# idx = range(len(df))
#
# plt.figure( figsize=(12,9) )
#
# plt.scatter(df['시점'],df['컴퓨터 및 주변기기'],label="electric")
# plt.scatter(df['시점'],df['신 발'],label="shoes")
# plt.scatter(df['시점'],df['가 방'],label="bag")
# plt.scatter(df['시점'],df['패션용품 및 악세사리'],label="acc")
# plt.scatter(df['시점'],df['가 구'],label="furniture")
# plt.scatter(df['시점'],df['애완용품'],label="pet")
# plt.scatter(df['시점'],df['기 타'],label="etc")
#
# plt.xlabel("year")
# plt.ylabel("money")
#
# plt.legend()
#
# plt.show()

###############################################################


###############################################################
# 9번 문제
# import pandas as ps
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# plt.rcParams['font.family']="Malgun Gothic"
# plt.rcParams['axes.unicode_minus']=False
#
# df =ps.read_csv('birth.csv',encoding='euc-kr')
#
# w = 0.3
# idx = np.arange(len(df))
# # print(idx)
#
# plt.bar(idx-w,df['서울특별시'],width=w ,label="서울")
# plt.bar(idx,df['부산광역시'],width=w,label="부산")
# plt.bar(idx+w,df['제주특별자치도'],width=w,label="제주")
#
# plt.xticks(idx,df['시점'])
# plt.ylabel(" 인구수 ")
# plt.legend()
#
# plt.show()
###############################################################


###############################################################
# 10번 문제
# import pandas as ps
# import matplotlib.pyplot as plt
#
# df = ps.read_csv("move_P.csv",encoding="euc-kr")
# # print(df)
#
# ind = range(len(df))
# print(ind)
#
# plt.plot(ind, df['서울특별시'],'b-',label="seoul")
# plt.plot(ind, df['부산광역시'],'g-',label="busan")
# plt.plot(ind, df['세종특별자치시'],'r-',label="sejong")
# plt.plot(ind, df['제주특별자치도'],'y-',label="jeju")
#
# plt.xticks(ind, df['시점'])
# plt.xlabel("year")
# plt.ylabel("number")
#
# plt.legend()
#
# plt.show()
###############################################################


