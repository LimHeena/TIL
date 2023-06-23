# 문제1 (유형1)
# 데이터셋(basic1.csv)의 'f5' 컬럼을 기준으로 상위 10개의 데이터를 구하고, 'f5'컬럼 10개 중 최소값으로 데이터를 대체한 후, 'age'컬럼에서 80 이상인 데이터의'f5 컬럼 평균값 구하기
import pandas as pd
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df = df.sort_values('f5', ascending=False)
mymin = df.iloc[:10, -1].min()
df.iloc[:10, -1] = mymin
result = df[df['age'] >= 80]['f5'].mean()
print(result)

# 문제2 (유형1)
# 데이터셋(basic1.csv)의 앞에서 순서대로 70% 데이터만 활용해서, 'f1'컬럼 결측치를 중앙값으로 채우기 전후의 표준편차를 구하고 두 표준편차 차이 계산하기

import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df70, df30 = np.split(df, [int(0.7 * len(df))])
before = df70['f1'].std()
df70['f1'] = df70['f1'].fillna(df70['f1'].median())
after = df70['f1'].std()
result = before - after
print(result)
## 랜덤으로 샘플링 하라고 한다면,
data70 = df.sample(frac = 0.7)
data30 = df.drop(data70.index)

# 문제 3 (유형1)
# 데이터셋(basic1.csv)의 'age'컬럼의 이상치를 더하시오! 단, 평균으로부터 '표준편차*1.5'를 벗어나는 영역을 이상치라고 판단함
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
std = df['age'].std() * 1.5
mean = df['age'].mean()
maxx = mean + std
minn = mean - std
result = ((df['age'] > maxx) | (df['age'] < minn)).sum()
print(result)

# 문제 4 유형1
# 데이터에서 IQR을 활용해 Fare컬럼의 이상치를 찾고, 이상치 데이터의 여성 수를 구하시오
import pandas as pd
df = pd.read_csv('titanic/train.csv')
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
# 이상치는 Q1 - IQR * 1.5, Q3 + IQR * 1.5
max = Q3 + IQR * 1.5
min = Q1 - IQR * 1.5
mydf = df[(df['Fare'] > max) | (df['Fare'] < min)]
result = len(mydf[mydf['Sex'] == 'female'])
print(result)

# 문제 5 유형1
# 주어진 데이터에서 이상치(소수점 나이)를 찾고 올림, 내림, 버림(절사)했을때 3가지 모두 이상치 'age' 평균을 구한 다음 모두 더하여 출력하시오
## 내림과 버림의 차이: 양수에서는 같지만 음수에서는 -5.5에서 내림을 하면 -6, 버림을하면 -5가 된다
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
# 소수점 데이터 찾기
df = df[(df['age']-np.floor(df['age']))!= 0]
# 이상치를 포함한 데이터 올림, 내림, 버림의 평균값 
m_ceil = np.ceil(df['age']).mean() # 올림
m_floor = np.floor(df['age']).mean() # 내림
m_trunc = np.trunc(df['age']).mean() # 버림
print(m_ceil + m_floor + m_trunc) # 평균값 더한 다음 출력

# 문제 6 유형1
# 주어진 데이터에서 결측치가 80%이상 되는 컬럼은(변수는) 삭제하고, 80% 미만인 결측치가 있는 컬럼은 'city'별 중앙값으로 값을 대체하고 'f1'컬럼의 평균값을 출력하세요!
import pandas as pd
import numpy as np
df = pd.read_csv('../input/bigdatacertificationkr/basic1.csv')
df.isnull().sum()
df.shape
df.isnull().sum()/df.shape[0] # EDA - 결측비율 확인
df = df.drop(['f3'], axis=1) # f3 컬럼 삭제
# 결측치가 있는 컬럼을 제거하는 2가지 방법
# df.drop(['B', 'C'], axis=1)
# df.drop(columns=['B', 'C'])
df['city'].unique() # 도시 확인
# 도시별 중앙값 계산
s=df[df['city']=='서울']['f1'].median()
k=df[df['city']=='경기']['f1'].median()
b=df[df['city']=='부산']['f1'].median()
d=df[df['city']=='대구']['f1'].median()
#방법2
# k, d, b, s = df.groupby('city')['f1'].median()
# f1결측치 city별 중앙값으로 대체
df['f1'] = df['f1'].fillna(df['city'].map({'서울':s,'경기':k,'부산':b,'대구':d}))
# 만약 그냥 f1 중앙값으로 대체 한다면 
# df['f1'] = df['f1'].fillna(df['f1'].median())
print(df['f1'].mean())

# 문제7 유형1
# 주어진 데이터 중 train.csv에서 'SalePrice'컬럼의 왜도와 첨도를 구한 값과, 'SalePrice'컬럼을 스케일링(log1p)로 변환한 이후 왜도와 첨도를 구해 모두 더한 다음 소수점 2째자리까지 출력하시오
import pandas as pd
import numpy as np
df = pd.read_csv("../input/house-prices-advanced-regression-techniques/train.csv")
df['SalePrice'].head()
# 'SalePrice'컬럼 왜도와 첨도계산
s1 = df['SalePrice'].skew() # 왜도
k1 = df['SalePrice'].kurt() # 첨도
# 'SalePrice'컬럼 로그변환
df['SalePrice'] = np.log1p(df['SalePrice'])
s2 = df['SalePrice'].skew()
k2 = df['SalePrice'].kurt()
print(round(s1+s2+k1+k2,2))

# 문제8 유형1
# 주어진 데이터 중 basic1.csv에서 'f4'컬럼 값이 'ENFJ'와 'INFP'인 'f1'의 표준편차 차이를 절대값으로 구하시오
en = df[df['f4'] =='ENFJ']
enst = en['f1'].std()
inn = df[df['f4'] =='INFP']
inst = inn['f1'].std()
print(np.abs(enst-inst))
## 표준편차에 모표본편차와, 표본표준편차가 있어.
## 판다스에서 하는건 표본표준편차. 시험에서는 판다스를 이용하라. 
## 지금 내가 위에서 한 게 판다스 거.

