import pandas as pd

# 작업유형1

from sklearn.preprocessing import MinMaxScaler 
df = pd.read_csv('csv', index_col=0)
min = MinMaxScaler()
min.fit(df['qsec'])
df['qsec']= min.transform(df['qsec'])
print(len(df['qsec']>0.5))

from sklearn.preprocessing import MinMaxScaler 
scaler = ['qsec']
min = MinMaxScaler()
min.fit(df[scaler])
df[scaler] = min.transform(df[scaler])
result = df[(df['qsec'] > 0.5)]
print(len(result))

# 작업유형2

# 1. 결측치 제거
# print(X_train.isna().sum())
X_train['환불금액'] = X_train['환불금액'].fillna(0)
X_test['환불금액'] = X_test['환불금액'].fillna(0)

print(X_train.isna().sum)

# 2. 라벨 인코더
label=['주구매상품','주구매지점']
from sklearn.preprocessing import LabelEncoder 
X_train[label] = X_train[label].apply(LabelEncoder().fit_transform)
X_test[label] = X_test[label].apply(LabelEncoder().fit_transform)

print(X_train.head())

print(X_train['주구매상품'].value_counts())
print(X_train['주구매지점'].value_counts())

# 3. 카테고리, 더미
category = ['주구매지점']
for i in category:
    X_train[i] = X_train[i].astype('category')
    X_test[i] = X_test[i].astype('category')

X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

print(X_train.head())

# 4. 파생변수 생성 
X_train['총구매액_qcut'] = pd.qcut(X_train['총구매액'], 5, labels=False)
X_test['총구매액_qcut'] = pd.qcut(X_test['총구매액'], 5, labels=False)

print(X_train.head())

# 5. 스케일링
from sklearn.preprocessing import MinMaxScaler
scaler = ['총구매액','최대구매액','환불금액','내점일수','내점당구매건수','주말방문비율','구매주기']
min = MinMaxScaler()
min.fit(X_train[scaler])
X_train[scaler] = min.transform(X_train[scaler])
X_test[scaler] = min.transform(X_test[scaler])

print(X_train.head())

# 6. 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train['gender'], test_size=0.2, random_state=42, stratify=y_train['gender'])

print(X_train.shape)
print(X_valid.shape)

# 7. 모형 학습, 앙상블
from sklearn.linear_model import LogisticRegression 
model1 = LogisticRegression()
model1.fit(X_train, y_train)
pred1 = pd.DataFrame(model1.predcit_proba(X_valid))

from sklearn.ensemble import RandomForestClassifier 
model2 = RandomForestClassifier()
model2.fit(X_train, y_train)
pred2 = pd.DataFrame(model2.predict_proba(X_valid))

from sklearn.ensemble import VotingClassifier 
model3 = VotingClassifier(estimators=[('logistic', model1), ('rf', model2)], voting='soft')
model3.fit(X_train, y_train)
pred3 = pd.DataFrame(model3.predict_proba(X_valid))

# 8. 모형 평가
from sklearn.metrics import roc_auc_score
print('로지스틱: ', roc_auc_score(y_valid, pred1.iloc[:,1]))
print('랜포: ', roc_auc_score(y_valid, pred2.iloc[:,1]))
print('보팅: ', roc_auc_score(y_valid, pred3.iloc[:,1]))

# 하이퍼파라미터 튜닝 
from sklearn.model_selection import GridSearchCV 
params = {'n_estimators':[50,100], 'max_depth':[4,6]}
model4 = RandomForestClassifier()
clf = GridSearchCV(estimator=model4, param_grid=params, cv=3)
clf.fit(X_train, y_train)

print('최적의 파라미터: ', clf.best_params_)

# 파일 저장
result = pd.DataFrame(model3.predict_proba(X_test))
result = result.iloc[:,1]
pd.DataFrame({'cust_id':X_test['cust_id'], 'gender':result}).to_csv('0010.csv', index=False)

# 확인 
check = pd.read_csv('0010.csv')
print(check.head())
