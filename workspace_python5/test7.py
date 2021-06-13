# test7.py

# 선 그래프

# csv 파일 불러오는 기능
import pandas as ps

# 그래프 그리는 기능
import matplotlib.pyplot as plt


# uft-8 은 에러나서 euc-kr 로 하기
df = ps.read_csv("move_P.csv",encoding="euc-kr")
# print(df)

ind = range(len(df))
print(ind)

plt.plot(ind, df['서울특별시'],'b-',label="seoul")
plt.plot(ind, df['부산광역시'],'g--',label="busan")
plt.plot(ind, df['세종특별자치시'],'r-.',label="sejong")
plt.plot(ind, df['제주특별자치도'],'y:',label="jeju")

plt.xticks(ind, df['시점'])
plt.xlabel("year")
plt.ylabel("number")

plt.legend()

plt.show()