## 작업유형1

import pandas as pd
from sklearn.preprocessing import minmax_scale

# 문제1. 컬럼을 최소최대척도로 변환한 후, 0.5보다 큰 값 가지는 레코드 수 구하라.
df = pd.read_csv('data/mtcars.csv')
# print(df)

# 1번째 방법 
df['qsec'] = minmax_scale(df['qsec'])
result = sum(df['qsec'] > 0.5) # true는 1 따라서 sum으로 구해도 됨.
# print(result)

# 2번째 방법
def minmax(x):
    data = (x-min(x)) / (max(x)-min(x))
    return data
df['qsec'] = minmax(df['qsec'])
result = len(df[df['qsec'] > 0.5])
# print(result)

## 작업유형2

import pandas as pd
X = pd.read_csv('X_train')
y = pd.read_csv('y_train')
test = pd.read_csv('X_test')

print(X.isna().sum())

X = X.fillna(0)
X = X.drop(['cust_id'], asix=1)
cust_id = test.pop('cust_id')

from sklearn.preprocessing import LabelEncoder
label = ['주구매상품', '주구매지점']
X[label] = X[label].apply(LabelEncoder().fit_transform)

from sklearn.ensemble import RandomForestClassifier
model1 = RandomForestClassifier()
model1.fit(X, y['gender'])
pred1 = model1.predict_proba(test)

result = pd.DataFrame({'cust_id':cust_id, 'gender':pred1[:,1]}).to_csv('000121.csv', index=False)
