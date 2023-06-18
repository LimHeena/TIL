import pandas as pd

# 1. 데이터를 로드하라. 데이터는 \t을 기준으로 구분되어있다.
url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(url, sep='\t')   # sep 해줘야해!!
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
url = 'https://raw.githubusercontent.com/Datamanim/pandas/main/chipo.csv'
df = pd.read_csv(url)
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

# 43. df의 데이터 중 new_price값이 lst에 해당하는 경우의 데이터 프레임을 구하고 그 갯수를 출력하라 lst =[1.69, 2.39, 3.39, 4.45, 9.25, 10.98, 11.75, 16.98]
