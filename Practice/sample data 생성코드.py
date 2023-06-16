import pandas as pd

df = pd.read_csv('★new_naver_data.csv')
df = df.drop(['image_url','low_price'], axis=1)
# print(df)

sample_size = 1000
categories = df['cat_id'].unique()
sampled_df = pd.DataFrame()
for category in categories:
    category_data = df[df['cat_id'] == category]
    if len(category_data) >= sample_size:
        sampled_data = category_data.sample(sample_size, replace=False)
    else:
        sampled_data = category_data.sample(sample_size, replace=True)
    sampled_df = pd.concat([sampled_df, sampled_data])

sampled_df.reset_index(drop=True, inplace=True)
sampled_df.to_csv('sample_naver.csv', index=False)

df = pd.read_csv('sample_naver.csv')
print(len(df['cat_id'].unique()))
print(df)