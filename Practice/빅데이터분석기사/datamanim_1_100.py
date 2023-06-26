import pandas as pd

# 1. 인기동영상 제작횟수가 많은 채널 상위 10개명을 출력하라 (날짜기준, 중복포함)
df = pd.read_csv("https://raw.githubusercontent.com/Datamanim/datarepo/main/youtube/youtube.csv",index_col=0)
print(df.columns)
b = df['channelId'].value_counts().head(10).index
c = list(df[df['channelId'].isin(b)]['channelTitle'][:10])
print(c)
# 다른 방법
a = df['channelId'].value_counts().head(10).index  ## 상위 10개 채널아이디.
print(a)
b = df.loc[df['channelId'].isin(a)]['channelTitle'].unique()
print(b)  ## 그 채널아이디의 채널명

# 2. 논란으로 인기동영상이 된 케이스를 확인하고 싶다. dislikes수가 like 수보다 높은 동영상을 제작한 채널을 모두 출력하라
a = df.loc[df['dislikes'] > df['likes']]['channelTitle'].unique()
print(a)

# 3. 채널명을 바꾼 케이스가 있는지 확인하고 싶다. channelId의 경우 고유값이므로 이를 통해 채널명을 한번이라도 바꾼 채널의 갯수를 구하여라
print(df.shape)
a = df[['channelTitle','channelId']].drop_duplicates()  
print(a)  ## 중복 제거
b = a['channelId'].value_counts()
print(b)  ## 채널명 바꾼 횟수 
print(type(b))  ## 시리즈 
c = b[b>1]
print(len(c))  ## 정답

# 4. 일요일에 인기있었던 영상들 중 가장많은 영상 종류(categoryId)는 무엇인가?
print(df.info())
df['trending_date2'] = pd.to_datetime(df['trending_date2'])
b = df.loc[df['trending_date2'].dt.day_name()=='Sunday'].categoryId.value_counts().index[0]
print(b)

# 5. 각 요일별 인기 영상들의 categoryId는 각각 몇개 씩인지 하나의 데이터 프레임으로 표현하라
a = df.groupby([df['trending_date2'].dt.day_name(), 'categoryId'], as_index=False).size()
b = a.pivot(index='categoryId', columns='trending_date2')
print(b)
## print(help(pd.Series.dt)) 검색할 때 이렇게!!!!!!!!!

# 6. 댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다. viewcount대비 댓글수가 가장 높은 영상을 확인하라 (view_count값이 0인 경우는 제외한다)
a = df.loc[df.view_count != 0]
a['ratio'] = (a['comment_count'] / a['view_count']).dropna()
b = a.sort_values('ratio', ascending=False).iloc[0].title
print(b)

# 7. 댓글의 수로 (comment_count) 영상 반응에 대한 판단을 할 수 있다.viewcount대비 댓글수가 가장 낮은 영상을 확인하라 (view_counts, ratio값이 0인경우는 제외한다.)
a = df.loc[df.view_count != 0]
a['ratio'] = a['comment_count'] / a['view_count']
a = a.loc[a.ratio != 0]
b = a.sort_values('ratio', ascending=True).iloc[0].title
print(b)  ## 내가 푼 정답
ratio = (df['comment_count'] / df['view_count']).dropna().sort_values()
print(df.iloc[ratio[ratio!=0].index[0]].title)
# 책 정답 

# 8. like 대비 dislike의 수가 가장 적은 영상은 무엇인가? (like, dislike 값이 0인경우는 제외한다)
a = df.loc[(df['likes'] != 0) & (df['dislikes'] != 0)]
a['ratio'] = (a.dislikes / a.likes).dropna()
a = df.iloc[a.sort_values('ratio').index[0]].title
print(a)

# 9. 가장많은 트렌드 영상을 제작한 채널의 이름은 무엇인가? (날짜기준, 중복포함)
a = df.groupby('channelTitle').size().sort_values(ascending=False).index[0]
print(a)  ## 내 답
a = df.loc[df.channelId == df.channelId.value_counts().index[0]].channelTitle
print(a)

# 10. 20회(20일)이상 인기동영상 리스트에 포함된 동영상의 숫자는?
a = sum(df[['title', 'channelId']].value_counts() >= 20)
print(a)  ## 중복 포함인듯 

