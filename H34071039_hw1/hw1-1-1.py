import pandas as pd

print('Q1')
df = pd.read_csv (r'IMDB-Movie-Data.csv')
df.fillna(-1)


df_year = df[df['Year'] ==2016] #2016的條件

df_rate = df_year.groupby('Title')[['Rating']].mean().sort_values(['Rating'],ascending=False) #依照title分類並算rating的平均並排序
print(df_rate.head(3))
