import pandas as pd

# 1. 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다.
# url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
# df = pd.read_csv(url, sep='\t')   # sep 해줘야해!!
# print(df)

# 2. 데이터의 상위 5개 행을 출력하라
# print(df.head(5))

# 3. 데이터의 행과 열의 갯수를 파악하라
# print(df.shape)
# print('행: ', df.shape[0])  # shape 기억행
# print('열: ', df.shape[1])

# 4. 전체 컬럼을 출력하라
# print(df.columns)

# 5. 6번째 컬럼명을 출력하라
# print(df.columns[5])

# 6. 6번째 컬럼의 데이터 타입을 확인하라
# print(type(df.iloc[5])) ## 틀린답
# print(df.iloc[:,5].dtype) ## 정답

# 7. 데이터셋의 인덱스 구성은 어떤가
# print(df.index)

# 8. 6번째 컬럼의 3번째 값은 무엇인가?
# print(df.iloc[2,5])

# 9. 데이터를 로드하라. 컬럼이 한글이기에 적절한 처리해줘야함
# url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/Jeju.csv'
# df = pd.read_csv(url, encoding = 'euc-kr')  # euc-kr 기억행
# print(df)

# 10. 데이터 마지막 3개행을 출력하라
# print(df.tail(3))

# 11. 수치형 변수를 가진 컬럼을 출력하라
# ans = df.select_dtypes(exclude=object).columns  # 첨보는 식인데 기억행!!
# print(ans)

# 12. 범주형 변수를 가진 컬럼을 출력하라
# ans = df.select_dtypes(include='object').columns # 따옴표 없이 그냥 object도 가능.
# print(ans)

# 13. 각 컬럼의 결측치 숫자를 파악하라
# print(df.isna().sum())

# 14. 각 컬럼의 데이터수, 데이터타입을 한번에 확인하라
# print(df.info())

# 15. 각 수치형 변수의 분포(사분위, 평균, 표준편차, 최대 , 최소)를 확인하라
# print(df.describe())

# 16. 거주인구 컬럼의 값들을 출력하라
# print(df['거주인구'].values) # 내가 쓴 답
# print(df['거주인구'])

# 17. 평균 속도 컬럼의 4분위 범위(IQR) 값을 구하여라
# a = df['평균 속도'].quantile(0.75) - df['평균 속도'].quantile(0.25)
# print(a)    # 이 문제 기억행 함수 기억행!!

# 18. 읍면동명 컬럼의 유일값 갯수를 출력하라
# print(len(df['읍면동명'].unique()))

# 19. 읍면동명 컬럼의 유일값을 모두 출력하라
# print(df['읍면동명'].unique())

# 20. 데이터를 로드하라.
# url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
# df = pd.read_csv(url)
# print(df)

# 21. quantity컬럼 값이 3인 데이터를 추출하여 첫 5행을 출력하라
# print(df[df['quantity'] == 3].head(5))
# print(df.loc[df['quantity'] == 3].head(5))   동일 결과

# 22. quantity컬럼 값이 3인 데이터를 추출하여 index를 0부터 정렬하고 첫 5행을 출력하라
# adf = df[df['quantity'] == 3]
# adf = adf.reset_index(drop=True) # drop True 꼭!!
# print(adf.head())

# 23. quantity , item_price 두개의 컬럼으로 구성된 새로운 데이터 프레임을 정의하라
# adf = df[['quantity', 'item_price']]
# print(adf)

# 24. item_price 컬럼의 달러표시 문자를 제거하고 float 타입으로 저장하여 new_price 컬럼에 저장하라
# df['new_price'] = df['item_price'].str[1:].astype('float')
# print(df['new_price'])
## df['item_price'] = df['item_price'].str.replace('$', '') 내가 하고자 한 코드..
# object 객체는 str메소드 적용 가능!!!
## 그리고 타입 바꾸는 건 astype !

# 25. new_price 컬럼이 5이하의 값을 가지는 데이터프레임을 추출하고, 전체 갯수를 구하여라
# adf = df[df['new_price'] <= 5]
# print(adf)
# print(len(adf))

# 26. item_name명이 Chicken Salad Bowl 인 데이터 프레임을 추출하고 index 값을 초기화 하여라
# adf = df[df['item_name'] == 'Chicken Salad Bowl']
# adf = adf.reset_index(drop=True)
# print(adf)

# 27. new_price값이 9 이하이고 item_name 값이 Chicken Salad Bowl 인 데이터 프레임을 추출하라
# adf = df[(df['new_price'] <= 9) & (df['item_name'] == 'Chicken Salad Bowl')]
# print(adf)  ## & 만 사용 가능. 

# 28. df의 new_price 컬럼 값에 따라 오름차순으로 정리하고 index를 초기화 하여라
# adf = df.sort_values(by='new_price') ## sort_values  !!!!!!!!!
# adf = adf.reset_index(drop=True)
# print(adf)

# 29. df의 item_name 컬럼 값중 Chips 포함하는 경우의 데이터를 출력하라
# adf = df[df['item_name'].str.contains('Chips')]
# print(adf)  # 문자열 함수 contains  !!!!

# 30. df의 짝수번째 컬럼만을 포함하는 데이터프레임을 출력하라
# adf = df.loc[:,::2]  # 슬라이싱 잘 알기!!
# print(adf)

# 31. df의 new_price 컬럼 값에 따라 내림차순으로 정리하고 index를 초기화 하여라
# adf = df.sort_values('new_price', ascending = False)  # help 함수 사용할 때 데이터프레임 함수이면 df.sort_values 이렇게 검색해야 함.
# adf = adf.reset_index(drop=True)
# print(adf)

# 32. df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 인덱싱하라
# adf = df[(df['item_name'] == 'Steak Salad') | (df['item_name'] == 'Bowl')]
# print(adf)

# 33. df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 첫번째 케이스만 남겨라
# adf = adf.drop_duplicates('item_name') # 함수 기억~~
# print(adf)

# 34. df의 item_name 컬럼 값이 Steak Salad 또는 Bowl 인 데이터를 데이터 프레임화 한 후, item_name를 기준으로 중복행이 있으면 제거하되 마지막 케이스만 남겨라
# adf = adf.drop_duplicates('item_name', keep='last') 
# print(adf)

# 35. df의 데이터 중 new_price값이 new_price값의 평균값 이상을 가지는 데이터들을 인덱싱하라
# adf = df[df['new_price'] >= df['new_price'].mean()]
# print(adf)

# 36. df의 데이터 중 item_name의 값이 Izze 데이터를 Fizzy Lizzy로 수정하라
# df['item_name'] = df['item_name'].str.replace('Izze', 'Fizzy Lizzy')  # 시리즈 형태를 데이터프레임에 넣는 것 
# print(df)
## df.loc[df.item_name =='Izze','item_name'] = 'Fizzy Lizzy'  # 또 다른 정답

# 37. df의 데이터 중 choice_description 값이 NaN 인 데이터의 갯수를 구하여라
# a = df['choice_description'].isna().sum()  ## 틀렸음 주의!!
# print(a)

# 38. df의 데이터 중 choice_description 값이 NaN 인 데이터를 NoData 값으로 대체하라(loc 이용)
# a = df.loc[df['choice_description']].fillna('NoData')  ## 내 오답
# df.loc[df['choice_description'].isna(), 'choice_description'] = 'NoData'
# print(df)

# 39. df의 데이터 중 choice_description 값에 Black이 들어가는 경우를 인덱싱하라
# adf = df[df['choice_description'].str.contains('Black')]
# print(adf)

# 40. df의 데이터 중 choice_description 값에 Vegetables 들어가지 않는 경우의 갯수를 출력하라
# adf = len(df[df['choice_description'].str.contains('Vegetable', na=False)])  ## 들어가는 경우의 수 
# print(adf)
# adf = df[~df['choice_description'].str.contains('Vegetables', na=False)]  ##  na=False 이 인자가 없으면 에러 남!!!!
# print(len(adf))

# 41. df의 데이터 중 item_name 값이 N으로 시작하는 데이터를 모두 추출하라
# adf = df[df['item_name'].str.startswith('N')]  ## startswith 기억하기~~
# print(adf)

# 42. df의 데이터 중 item_name 값의 단어갯수가 15개 이상인 데이터를 인덱싱하라
# adf = df[df['item_name'].str.len() >= 15]
# print(adf)  ## str.len() 은 판다스의 시리즈나 데이터프레임에만 적용 가능

# 43. df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라 
#lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
# lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
# adf = df[df['new_price'].isin(lst)]  ## isin 함수 기억!! 리스트형식으로 넣어야 함
# print(adf)
# print(len(adf))

# 44. 데이터를 로드하고 상위 5개 컬럼을 출력하라
# url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/AB_NYC_2019.csv'
# df = pd.read_csv(url)
# print(df)

# 45. 데이터의 각 host_name의 빈도수를 구하고 host_name으로 정렬하여 상위 5개를 출력하라
# adf = df.groupby('host_name').size().sort_index()
# adf = df['host_name'].value_counts().sort_index()
## size() 함수. nan값 포함. 시리즈로 출력. 
## counts() 함수는 nan값 미포함. 데이터프레임으로 출력.
## value_counts 함수는 시리즈에서 사용. 각 고유한 값의 등장 횟수 내림차순으로 정렬.
## size 함수는 df,시리즈 사용. 데이터의 총 개수 반환.
# print(adf)

# 46. 데이터의 각 host_name의 빈도수를 구하고 빈도수 기준 내림차순 정렬한 데이터 프레임을 만들어라. 빈도수 컬럼은 counts로 명명하라
# adf = df.groupby('host_name').size() # 내가 해본 정답
# adf = pd.DataFrame({'counts': adf}).sort_values('counts', ascending=False)
# print(adf)
## df.groupby('host_name').size().to_frame().rename(columns={0:'counts'}).sort_values('counts',ascending=False)
## sort_values('컬럼명') 함수 기억 ~~

# 47. neighbourhood_group의 값에 따른 neighbourhood컬럼 값의 갯수를 구하여라
# adf = df.groupby(['neighbourhood_group','neighbourhood'], as_index=False).size()
# print(adf)  ## as_index 기억

# 48.neighbourhood_group의 값에 따른 neighbourhood컬럼 값 중 neighbourhood_group그룹의 최댓값들을 출력하라
# adf = df.groupby(['neighbourhood_group','neighbourhood'], as_index=False).size().groupby(['neighbourhood_group'], as_index=False).max()
# print(adf)

# 49. neighbourhood_group 값에 따른 price값의 평균, 분산, 최대, 최소 값을 구하여라
# adf = df.groupby('neighbourhood_group')['price'].agg(['mean', 'var', 'max', 'min'])
# print(adf)  ## price라고 위에 안나옴.
# Ans = df[['neighbourhood_group','price']].groupby('neighbourhood_group').agg(['mean','var','max','min'])
# print(Ans)  ## 두가지 방법이 결과가 살짝 다르게 나옴.. price 위에 나옴.

# 50. neighbourhood_group 값에 따른 reviews_per_month 평균, 분산, 최대, 최소 값을 구하여라
# adf = df[['neighbourhood_group','reviews_per_month']].groupby('neighbourhood_group')['reviews_per_month'].agg(['mean','var','max','min'])
# print(adf)

# 51. neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 구하라
# adf = df.groupby(['neighbourhood','neighbourhood_group'])['price'].mean()
# print(adf)

# 52. neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하라
# adf = df.groupby(['neighbourhood_group', 'neighbourhood'])['price'].mean().reset_index()
# print(adf) ## 지피치가 말한 계층적 인덱싱 없이 구한 결과
# Ans = df.groupby(['neighbourhood','neighbourhood_group']).price.mean().unstack()
# print(Ans)  ## 문제 정답

# 53. neighbourhood 값과 neighbourhood_group 값에 따른 price 의 평균을 계층적 indexing 없이 구하고 nan 값은 -999값으로 채워라
# adf = df.groupby(['neighbourhood','neighbourhood_group'])['price'].mean().unstack().fillna(-999)
# print(adf)  ## unstack() 함수~~ 인덱싱 하나 풀어주는 것. 

# 54. 데이터중 neighbourhood_group 값이 Queens값을 가지는 데이터들 중 neighbourhood 그룹별로 price값의 평균, 분산, 최대, 최소값을 구하라
# adf = df[df['neighbourhood_group'] == 'Queens']
# adf = adf.groupby('neighbourhood')['price'].agg(['mean','var','max','min'])
# print(adf)

# 55. 데이터중 neighbourhood_group 값에 따른 room_type 컬럼의 숫자를 구하고 neighbourhood_group 값을 기준으로 각 값의 비율을 구하여라
# adf = df[['neighbourhood_group','room_type']].groupby(['neighbourhood_group','room_type']).size().unstack()
# adf.loc[:,:] = adf.values/adf.sum(axis=1).values.reshape(-1,1)
# print(adf)  ## 이건 걍 외워..ㅎㅎ

# 56. 데이터를 로드하고 데이터 행과 열의 갯수를 출력하라
# url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/BankChurnersUp.csv'
# df = pd.read_csv(url, index_col = 0)
# print(df)
# print(df.shape)

# 57. Income_Category의 카테고리를 map 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라 
# Unknown : N
# Less than $40K : a
# $40K - $60K : b
# $60K - $80K : c
# $80K - $120K : d
# $120K +’ : e
# dic = {'Unknown'        : 'N',
#     'Less than $40K' : 'a',
#     '$40K - $60K'    : 'b',
#     '$60K - $80K'    : 'c',
#     '$80K - $120K'   : 'd',
#     '$120K +'        : 'e'}
# df['newIncome'] = df['Income_Category'].map(lambda x: dic[x])
# adf = df['newIncome']  ## map(lambda x: dic[x]) 이렇게도 사용 가능!!
# print(adf)

# 58. Income_Category의 카테고리를 apply 함수를 이용하여 다음과 같이 변경하여 newIncome 컬럼에 매핑하라
# Unknown : N
# Less than $40K : a
# $40K - $60K : b
# $60K - $80K : c
# $80K - $120K : d
# $120K +’ : e
# def changeCategory(x):
#     if x =='Unknown':
#         return 'N'
#     elif x =='Less than $40K':
#         return 'a'
#     elif x =='$40K - $60K':   
#         return 'b'
#     elif x =='$60K - $80K':    
#         return 'c'
#     elif x =='$80K - $120K':   
#         return 'd'
#     elif x =='$120K +' :     
#         return 'e'
# df['newIncome'] = df['Income_Category'].apply(changeCategory)
# adf = df['newIncome']  ## apply 함수에는 함수명만~
# print(adf)

# 59. Customer_Age의 값을 이용하여 나이 구간을 AgeState 컬럼으로 정의하라. (0~9 : 0 , 10~19 :10 , 20~29 :20 … 각 구간의 빈도수를 출력하라
# df['AgeState'] = df['Customer_Age'].map(lambda x: x//10 * 10)
# adf = df['AgeState'].value_counts().sort_index()
# print(adf)

# 60. Education_Level의 값중 Graduate단어가 포함되는 값은 1 그렇지 않은 경우에는 0으로 변경하여 newEduLevel 컬럼을 정의하고 빈도수를 출력하라
# df['newEduLevel'] = df['Education_Level'].map(lambda x: 1 if 'Graduate' in x else 0)
# adf = df['newEduLevel'].value_counts().sort_index()
# print(adf)  ## 람다 함수에 들어가는 식 기억하기!!

# 61. Credit_Limit 컬럼값이 4500 이상인 경우 1 그외의 경우에는 모두 0으로 하는 newLimit 정의하라. newLimit 각 값들의 빈도수를 출력하라
# df['newLimit'] = df['Credit_Limit'].map(lambda x: 1 if x >= 4500 else 0)
# adf = df['newLimit'].value_counts()
# print(adf)

# 62. Marital_Status 컬럼값이 Married 이고 Card_Category 컬럼의 값이 Platinum인 경우 1 그외의 경우에는 모두 0으로 하는 newState컬럼을 정의하라. newState의 각 값들의 빈도수를 출력하라
# def check(x):
#     if x.Marital_Status == 'Married' and x.Card_Category == 'Platinum':
#         return 1
#     else:
#         return 0
# df['newState'] = df.apply(check, axis=1)
# adf = df['newState'].value_counts()
# print(adf)

# 63. Gender 컬럼값 M인 경우 male F인 경우 female로 값을 변경하여 Gender 컬럼에 새롭게 정의하라. 각 value의 빈도를 출력하라
# df['Gender'] = df['Gender'].map(lambda x: 'male' if x == 'M' else 'female')
# adf = df['Gender'].value_counts()
# print(adf) ## 내가 푼 정답
# def changeGender(x):
#     if x =='M':
#         return 'male'
#     else:
#         return 'female'
# df['Gender'] = df.Gender.apply(changeGender)
# Ans = df['Gender'].value_counts() ## 책 정답 

# 64. 데이터를 로드하고 각 열의 데이터 타입을 파악하라
# url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/timeTest.csv'
# df = pd.read_csv(url)
# print(df)
# print(df.info())

# 65. Yr_Mo_Dy을 판다스에서 인식할 수 있는 datetime64타입으로 변경하라
# df['Yr_Mo_Dy'] = pd.to_datetime(df['Yr_Mo_Dy'])
# print(df['Yr_Mo_Dy'])  ## to_datetime() 기억하기!!

# 66. Yr_Mo_Dy에 존재하는 년도의 유일값을 모두 출력하라
# adf = df.Yr_Mo_Dy.dt.year.unique()
# print(adf)

# 67. Yr_Mo_Dy에 년도가 2061년 이상의 경우에는 모두 잘못된 데이터이다. 해당경우의 값은 100을 빼서 새롭게 날짜를 Yr_Mo_Dy 컬럼에 정의하라
# df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].map(lambda x: x.year - 100 if x.year >= 2061 else x.dt.year)
# print(df['Yr_Mo_Dy'])  ## 이거 불가. 날짜 계산하려면 datetume 써야함.
# def fix(x):
#     import datetime
#     year = x.year - 100 if x.year >= 2061 else x.year
#     return pd.to_datetime(datetime.date(year, x.month, x.day))
# df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix)
# print(df)

# 68. 년도별 각컬럼의 평균값을 구하여라
# adf = df.groupby(df['Yr_Mo_Dy'].dt.year).mean()
# print(adf)

# 69. weekday컬럼을 만들고 요일별로 매핑하라 ( 월요일: 0 ~ 일요일 :6)
# df['weekday'] = df['Yr_Mo_Dy'].dt.weekday
# print(df['weekday'])

# 70. weekday컬럼을 기준으로 주말이면 1 평일이면 0의 값을 가지는 WeekCheck 컬럼을 만들어라
# df['WeekCheck'] = df['weekday'].map(lambda x : 1 if x in [5,6] else 0)
# print(df['WeekCheck'])

# 71. 년도, 일자 상관없이 모든 컬럼의 각 달의 평균을 구하여라
# adf = df.groupby(df['Yr_Mo_Dy'].dt.month).mean()
# print(adf)

# 72. 모든 결측치는 컬럼기준 직전의 값으로 대체하고 첫번째 행에 결측치가 있을경우 뒤에있는 값으로 대채하라
# adf = df.fillna(method = 'ffill').fillna(method='bfill')
# print(adf)  ## ffill: 위값과 동일, bfill: 아래값과 동일 

# 73. 년도 - 월을 기준으로 모든 컬럼의 평균값을 구하여라
# adf = df.groupby(df['Yr_Mo_Dy'].dt.to_period('M')).mean()
# print(adf) ## to_period() 기억~ M:월, D:일, Q:분기, A:년도  !!!!!

# 74. RPT 컬럼의 값을 일자별 기준으로 1차차분하라
# adf = df['RPT'].diff()
# print(adf)  ## diff 함수 기억 

# 75. RPT와 VAL의 컬럼을 일주일 간격으로 각각 이동평균한값을 구하여라
# adf = df[['RPT','VAL']].rolling(7).mean()
# print(adf)  ## rolling 함수 기억~

# 76. 년-월-일:시 컬럼을 pandas에서 인식할 수 있는 datetime 형태로 변경하라. 서울시의 제공데이터의 경우 0시가 24시로 표현된다
# url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/seoul_pm.csv'
# df = pd.read_csv(url)
# print(df)
# def mytime(x):
#     import datetime
#     hour = x.split(':')[1]
#     date = x.split(':')[0]
#     if hour == '24':
#         final = pd.to_datetime(date + ' ' + '00:00:00') + datetime.timedelta(days=1)
#     else:
#         final = pd.to_datetime(date + ' ' + hour + ':00:00')
#     return final
# df['(년-월-일:시)'] = df['(년-월-일:시)'].apply(mytime)
## 위의 식 외우기...

# 77. 일자별 영어요일 이름을 dayName 컬럼에 저장하라
# df['dayName']  = df['(년-월-일:시)'].dt.day_name()
# print(df['dayName'])  ## day_name 외우기

# 78. 일자별 각 PM10등급의 빈도수를 파악하라
# adf = df.groupby(['dayName','PM10등급'], as_index=False).size()
# print(adf)

# 79. 시간이 연속적으로 존재하며 결측치가 없는지 확인하라
# 시간을 차분했을 경우 첫 값은 nan, 이후 모든 차분값이 동일하면 연속이라 판단한다.  ## 외워
# check = len(df['(년-월-일:시)'].diff().unique())
# if check == 2:
#     adf = True
# else:
#     adf = False
# print(adf)

# 80. 오전 10시와 오후 10시(22시)의 PM10의 평균값을 각각 구하여라
# adf = df.groupby(df['(년-월-일:시)'].dt.hour)['PM10'].mean().iloc[[10,22]]
# print(adf)

# 81. 날짜 컬럼을 index로 만들어라
# df.set_index('(년-월-일:시)', inplace = True, drop=True)
# print(df)  ## drop=false 하면 인덱스로 설정되면서도 데이터프레임의 컬럼으로 유지된다.

# 82. 데이터를 주단위로 뽑아서 최소,최대 평균, 표준표차를 구하여라
# adf = df.select_dtypes(exclude='object').resample('W').agg(['min','max','mean','std'])
# print(adf) ## str 제거해주고, 주단위로 리샘플. 

# 83. Indicator을 삭제하고 First Tooltip 컬럼에서 신뢰구간에 해당하는 표현을 지워라
# df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/under5MortalityRate.csv')
# print(df)
# df = df.drop('Indicator', axis=1)
# df['First Tooltip'] = df['First Tooltip'].map(lambda x: float(x.split('[')[0]))
# print(df)

# 84. 년도가 2015년 이상, Dim1이 Both sexes인 케이스만 추출하라
# adf = df[(df['Period'] >= 2015) & (df['Dim1'] == 'Both sexes')]
# print(adf)  ## and는 조건문이나 불리언 연산 때 사용.

# 85. 84번 문제에서 추출한 데이터로 아래와 같이 나라에 따른 년도별 사망률을 데이터 프레임화 하라
# adf = adf.pivot(index='Location', columns='Period', values='First Tooltip')
# print(adf)  ## pivot 테이블 적용 외워..

# 86. Dim1에 따른 년도별 사망비율의 평균을 구하라
# adf = df.pivot_table(index='Dim1', columns='Period', values='First Tooltip', aggfunc='mean')
# print(adf) 
## pivot_table은 그냥 피봇과 달리 데프에서 그룹화 및 집계를 수행. 기본은 평균. 

# 87. 데이터에서 한국 KOR 데이터만 추출하라
# df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/winter.csv')
# print(df)
# kr = df[df['Country']=='KOR']
# print(kr)

# 88. 한국 올림픽 메달리스트 데이터에서 년도에 따른 medal 갯수를 데이터프레임화 하라
# adf = df.groupby(['Year','Medal']).size().unstack()
# print(adf)  ## 내가 쓴 답
# adf = kr.pivot_table(index='Year', columns='Medal', aggfunc='size').fillna(0)
# print(adf)  ## 책 답

# 89. 전체 데이터에서 sport종류에 따른 성별수를 구하여라
# adf = df.pivot_table(index='Sport', columns='Gender', aggfunc='size')
# print(adf)

# 90. 전체 데이터에서 Discipline종류에 따른 따른 Medal수를 구하여라
# adf = df.pivot_table(index='Discipline', columns='Medal', aggfunc='size')
# print(adf)

# 91. df1과 df2 데이터를 하나의 데이터 프레임으로 합쳐라
df = pd.read_csv('https://raw.githubusercontent.com/Datamanim/pandas/main/mergeTEst.csv',index_col= 0)
# print(df)
df1 = df.iloc[:4,:]
df2 = df.iloc[4:,:]
# print(df1)
# print('-----------------------------')
# print(df2)
# df3 = pd.concat([df1,df2])
# print(df3)

# 92. df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 둘다 포함하고 있는 년도에 대해서만 고려한다
df3 = df.iloc[:2,:4]
df4 = df.iloc[5:,3:]
# df5 = pd.concat([df3,df4], join='inner')
# print(df5)

# 93. df3과 df4 데이터를 하나의 데이터 프레임으로 합쳐라. 모든 컬럼을 포함하고, 결측치는 0으로 대체한다
# df5 = pd.concat([df3,df4], join='outer').fillna(0)
# print(df5)

# 94. df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 두 데이터 모두 포함하는 데이터만 출력하라
df5 = df.T.iloc[:7,:3]
df6 = df.T.iloc[6:,2:5]
# df7 = pd.merge(df5, df6, on='Algeria', how='inner')
# print(df7)  ## merge 함수 문법 외워

# 95. df5과 df6 데이터를 하나의 데이터 프레임으로 merge함수를 이용하여 합쳐라. Algeria컬럼을 key로 하고 합집합으로 합쳐라
# df7 = pd.merge(df5, df6, on='Algeria', how='outer')
# print(df7)
