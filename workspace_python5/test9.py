# test9.py

import pandas as ps
import numpy as np
import matplotlib.pyplot as plt


plt.rcParams['font.family']="Malgun Gothic"
plt.rcParams['axes.unicode_minus']=False

df =ps.read_csv('birth.csv',encoding='euc-kr')

w = 0.3
idx = np.arange(len(df))
# print(idx)

plt.bar(idx-w,df['서울특별시'],width=w ,label="서울")
plt.bar(idx,df['부산광역시'],width=w,label="부산")
plt.bar(idx+w,df['제주특별자치도'],width=w,label="제주")

plt.xticks(idx,df['시점'])
plt.ylabel(" 인구수 ")
plt.legend()

plt.show()

