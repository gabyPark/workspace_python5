# test6.py

# import 추가라이브러리 as 이름(alias)
# pandas : 데이터분석(많은 데이터 처리), csv 파일 리드
# matplotlib.pyplot : 시각화

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('franchise.csv')
# print(df)

# 한글을 쓰고 싶다면
plt.rcParams['font.family']="Malgun Gothic"
plt.rcParams['axes.unicode_minus']=False
# 그리고 label 값을 "치킨", "커피" 로 바꾸면 실행된다

ind = np.arange(len(df))

plt.plot(df['chicken'],"r:.",label="chicken")
plt.plot(df['coffee'],"b:.",label="coffee")

plt.xticks(ind,df['year'])
plt.legend()  # 라벨 표시

plt.show()