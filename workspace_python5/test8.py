# test8.py


import pandas as ps
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family']="Malgun Gothic"
plt.rcParams['axes.unicode_minus']=False

df = ps.read_csv('population.csv')

# print(df)

w = 0.4
idx = np.arange(len(df))


plt.bar(idx-w/2, df['men'] ,width=w,color='b',label="남성")
plt.bar(idx+w/2, df['women'] ,width=w,color='r',label="여성")

plt.xticks(idx,df['local'])
plt.title(" 도시별 인구수 ")

plt.legend()

plt.show()

