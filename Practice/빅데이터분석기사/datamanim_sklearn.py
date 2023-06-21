import pandas as pd
pd.set_option('display.max_columns', None)

import pandas as pd
train = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_train.csv')
test = pd.read_csv('https://raw.githubusercontent.com/Datamanim/datarepo/main/airline/x_test.csv')

## MinMaxScaler

# 1. train 데이터의 Flight Distance 컬럼을 사이킷런 모듈을 이용하여 최솟값을 0 최댓값을 1값로 하는 데이터로 변환하고 scaling을 이름으로 하는 컬럼으로 데이터프레임에 추가하라
from sklearn.preprocessing import MinMaxScaler
train = train[:500]
min = MinMaxScaler()
scaler = ['Flight Distance']
min.fit(train[scaler])  ## 이 상태로 들어가면 데이터프레임으로 들어가는 것. fit 함수에는 1차원이 들어갈 수 없음. 
train['scaling'] = min.transform(train[scaler])

# 2. train 데이터의 Flight Distance 컬럼을 pandas의 내장함수만을 이용하여 최솟값을 0 최댓값을 1값로 하는 데이터로 변환하고 scaling을 이름으로 하는 컬럼으로 데이터프레임에 추가하라
## (데이터값- 최소값) / (최대값 - 최소값)
scaling = (train['Flight Distance'] - train['Flight Distance'].min()) /(train['Flight Distance'].max() - train['Flight Distance'].min())
train['scaling'] = scaling

## StandardScaler

# 1. train 데이터의 Age컬럼을 sklearn 모듈을 이용하여 정규화 스케일링을 진행 하고 age_scaling컬럼에 추가하고 train셋과 같은 기준으로 test데이터의 Age를 스케일링하여 age_scaling에 추가하라
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
scaler = ['Age']
sc.fit(train[scaler])
train['age_scaling'] = sc.transform(train[scaler])
test['age_scaling'] = sc.transform(train[scaler])

# 2. 내장함수 이용한거
## (데이터 - 평균) / 표준편차
scaling_ddof1 = (train['Age'] - train['Age'].mean()) /(train['Age'].std())
train['scaling'] = scaling_ddof1

