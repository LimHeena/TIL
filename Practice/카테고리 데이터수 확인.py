import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sample_bj.csv')

category_counts = df['cat_id'].value_counts()
categories = category_counts.index
counts = category_counts.values

print(category_counts)
print('---------------------')
print(categories)
print('---------------------')
print(counts)
