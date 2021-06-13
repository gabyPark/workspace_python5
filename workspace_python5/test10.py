# test10.py
#  산점도

import pandas as ps
import matplotlib.pyplot as plt

df = ps.read_csv('online.csv',encoding='euc-kr')

idx = range(len(df))

plt.figure( figsize=(12,9) )

plt.scatter(df['시점'],df['컴퓨터 및 주변기기'],label="electric")
plt.scatter(df['시점'],df['신 발'],label="shoes")
plt.scatter(df['시점'],df['가 방'],label="bag")
plt.scatter(df['시점'],df['패션용품 및 악세사리'],label="acc")
plt.scatter(df['시점'],df['가 구'],label="furniture")
plt.scatter(df['시점'],df['애완용품'],label="pet")
plt.scatter(df['시점'],df['기 타'],label="etc")

plt.xlabel("year")
plt.ylabel("money")

plt.legend()

plt.show()
